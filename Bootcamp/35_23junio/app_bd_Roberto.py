import pandas as pd
from flask import request, Flask, jsonify
import sqlite3
import os

app = Flask(__name__) # inicio Flask

def conexion():
    conexion = sqlite3.connect("books.db") # abro la conexión al archivo .db
    cursor = conexion.cursor() # creo el cursor (sirve como el dedo que apunta hacia las peticiones que haremos después)
    return conexion, cursor # devuelvo conexión y cursor


# 0. ruta para obtener todos los libros

@app.route("/books", methods=["GET"]) # le dice a Flask que cuando alguien visite la URL /books, ejecute la función de abajo
def todos_los_libros(): # creo la función 
    mi_conexion, cursor = conexion() # mi_conexion recibe el primer valor (la conexión) y cursor recibe el segundo valor (el cursor) 
    # le pido al cursor que busque todos los libros
    cursor.execute("SELECT * FROM books")
    # guardo las filas encontradas en la variable libros
    libros = cursor.fetchall()
    mi_conexion.close() # cierro la conexión, ya no la necesito
    # convierto cada fila en un diccionario para devolver JSON legible
    # se accede a cada elemento de la fila por su posición: el primero, el segundo, el tercero...
    resultado = [
        {
            "id": fila[0],
            "published": fila[1],
            "author": fila[2],
            "title": fila[3],
            "first_sentence": fila[4]
        }
        for fila in libros
    ]
    # devuelvo la lista de diccionarios en formato JSON
    return jsonify(resultado) 


# 1. ruta para obtener el conteo de libros por autor ordenados de forma descendente

@app.route("/books/conteo", methods=["GET"]) # cuando alguien visite /books/count con una petición GET, Flask ejecuta la función de abajo
def conteo_por_autor(): # se crea la función
    mi_conexion, cursor = conexion() # creo dos variables a partir de la función conexion 
    # El cursor ejecuta la query:
    # SELECT author, COUNT(*) → trae el nombre del autor y cuenta cuántas filas tiene
    # as conteo → le pone el nombre conteo a ese resultado
    # FROM books → de la tabla books
    # GROUP BY author → agrupa todas las filas del mismo autor en una sola
    # ORDER BY conteo DESC → ordena de mayor a menor por el conteo
    cursor.execute("""
        SELECT author, COUNT(*) as total
        FROM books
        GROUP BY author
        ORDER BY total DESC
    """)
    filas = cursor.fetchall() # recojo todos los resultados en filas (una lista de tuplas compuesta por autor y número de libros)
    mi_conexion.close() # cierro la conexión
    # convierto cada fila en un diccionario con autor y su conteo
    resultado = [{"author": fila[0], "total": fila[1]} for fila in filas]
    # devuelvo la lista de diccionarios en formato JSON
    return jsonify(resultado)


# 2. ruta para obtener los libros de un autor

@app.route("/books/author/<string:author>", methods=["GET"]) # cuando alguien visite /books/author/<string:author> con una petición GET, Flask ejecuta la función de abajo
def libros_por_autor(author): # se crea la función que recibe author como argumento
    mi_conexion, cursor = conexion() # creo dos variables a partir de la función conexion
    # uso parámetro posicional (?) para evitar inyección SQL
    cursor.execute("SELECT * FROM books WHERE author = ?", (author,)) # se filtran solo las filas en las que el author coincide con el argumento
    filas = cursor.fetchall() # recojo todos los resultados en filas
    mi_conexion.close() # cierro la conexión
    # si no encuentro nada, devuelvo 404 con mensaje claro
    if not filas:
        return jsonify({"error": f"no se encontraron libros del autor '{author}'"}), 404
    # convierto cada fila en un diccionario para devolver JSON legible
    # se accede a cada elemento de la fila por su posición: el primero, el segundo, el tercero...
    resultado = [
        {
            "id": fila[0],
            "published": fila[1],
            "author": fila[2],
            "title": fila[3],
            "first_sentence": fila[4]
        }
        for fila in filas
    ]
    # devuelvo la lista de diccionarios en formato JSON
    return jsonify(resultado)


# 3. ruta para añadir un libro
@app.route("/books", methods=["POST"]) # se usa la URL que la ruta 0 (/books) pero con el método POST (añadir)
def anadir_libro():  # se crea la función 
    mi_conexion, cursor = conexion() # creo dos variables a partir de la función conexion

    # recibo los datos enviados por el usuario en formato JSON
    datos = request.get_json()
    # extraigo los campos que necesito (con .get() para que no rompa si falta alguno)
    published = datos.get("published")
    author = datos.get("author")
    title = datos.get("title")
    first_sentence = datos.get("first_sentence")
    # inserto el nuevo libro (los ? sirven para evitar inyecciones SQL)
    cursor.execute("""
        INSERT INTO books (published, author, title, first_sentence)
        VALUES (?, ?, ?, ?) 
    """, (published, author, title, first_sentence))

    mi_conexion.commit() # guardo los cambios
    mi_conexion.close() # cierro la conexión
    # devuelvo la lista de diccionarios en formato JSON y envío mensaje al usuario para decir que está todo correcto
    return jsonify({"mensaje": f"libro '{title}' añadido correctamente"}), 201


if __name__ == "__main__": # arranca el servidor de Flask solo si ejecutamos este archivo directamente
    app.run(debug=True) # modo de pruebas

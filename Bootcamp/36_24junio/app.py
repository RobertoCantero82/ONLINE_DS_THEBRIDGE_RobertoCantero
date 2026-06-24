import os
import pickle
import sqlite3

import numpy as np
import pandas as pd
from flask import Flask, jsonify, request
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import PolynomialFeatures, StandardScaler

# inicio Flask
app = Flask(__name__)
# saco la carpeta donde vive app.py para que las rutas funcionen lance el script desde donde lo lance
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# ruta al modelo
MODEL_PATH = os.path.join(BASE_DIR, "data", "advertising_model.pkl")
# ruta al csv
CSV_PATH = os.path.join(BASE_DIR, "data", "Advertising.csv")
# ruta a la base de datos
DB_PATH = os.path.join(BASE_DIR, "data", "advertising.db")

# función para cargar el modelo 
def load_model():
    # abro el archivo pkl
    with open(MODEL_PATH, "rb") as f:
        # devuelvo el objeto pkl para usarlo
        return pickle.load(f)
    
# cargo el modelo una sola vez al arrancar, queda en memoria
model = load_model()    

# función para conectar a la base de datos
def get_db():
    # conecto (si el archivo .db no existe, sqlite lo crea)
    conn = sqlite3.connect(DB_PATH)
    # creo la tabla solo si no existe ya
    conn.execute(
        """CREATE TABLE IF NOT EXISTS records (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            tv REAL, radio REAL, newspaper REAL, sales REAL
        )"""
    )
    # confirmo el cambio para que quede guardado
    conn.commit()
    # devuelvo la conexión abierta para usarla fuera
    return conn

# nuevo endpoint para realizar predicciones
@app.route("/predict", methods=["GET"])
# creo la función de predicción
def predict():
    # recibo el json y lo leo
    body = request.get_json()
    # compruebo que llega algo y que trae la clave data
    if not body or "data" not in body:
        # si no, devuelvo error 400 (petición mal formada)
        return jsonify({"error": "Se requiere 'data'"}), 400
    # convierto los datos recibidos en un array
    X = np.array(body["data"])
    # hago la predicción y paso a lista 
    prediction = model.predict(X).tolist()
    # devuelvo la predicción en formato json
    return jsonify({"prediction": prediction})

# creo el endpoint para introducir datos en la base de datos
@app.route("/ingest", methods=["POST"])
# creo la función de ingesta
def ingest():
    # recibo el json y lo leo
    body = request.get_json()
    # compruebo que llega algo y que trae la clave data 
    if not body or "data" not in body:
        # error si falta data
        return jsonify({"error": "Se requiere 'data'"}), 400
    # abro conexión con la base de datos
    conn = get_db()
    # recorro cada fila de la base de datos
    for row in body["data"]:
        # inserto la fila usando ? para evitar inyección sql
        conn.execute(
            "INSERT INTO records (tv, radio, newspaper, sales) VALUES (?, ?, ?, ?)",
            row,
        )
    # confirmo todas las inserciones
    conn.commit()
    # cierro la conexión
    conn.close()
    # devuelvo el mensaje exacto que espera el test
    return jsonify({"message": "Datos ingresados correctamente"})

# creo el endpoint para reentrenar el modelo cargado
@app.route("/retrain", methods=["POST"])
# creo la función retrain
def retrain():
    # global para que el modelo nuevo lo use también /predict, no se quede aquí dentro
    global model
    # abro conexión a la base de datos
    conn = get_db()
    # leo todos los registros
    rows = conn.execute("SELECT tv, radio, newspaper, sales FROM records").fetchall()
    # cierro la conexión
    conn.close()
    # si hay registros en la base de datos
    if rows:
        # los meto en un dataframe
        db_df = pd.DataFrame(rows, columns=["TV", "radio", "newpaper", "sales"])
    # de lo contrario
    else:
        # creo un dataframe vacío (solo columnas, sin datos)
        db_df = pd.DataFrame(columns=["TV", "radio", "newpaper", "sales"])
    # leo el csv sin la columna de índice
    csv_df = pd.read_csv(CSV_PATH, index_col=0)
    # concateno el csv con los nuevos datos
    combined = pd.concat([csv_df, db_df], ignore_index=True)
    # fuerzo a numérico y elimino filas con huecos
    combined = combined.apply(pd.to_numeric, errors="coerce").dropna()
    # separo las variables predictoras
    X = combined[["TV", "radio", "newpaper"]].values
    # separo la variable objetivo (ventas)
    y = combined["sales"].values
    # # monto un pipeline nuevo desde cero
    new_model = Pipeline([
        # genero términos polinómicos de grado 2
        ("poly", PolynomialFeatures(degree=2, include_bias=False)),
        # escalo las features para que estén en rangos comparables
        ("scaler", StandardScaler()),
        # aplico la regresión lineal
        ("reg", LinearRegression()),
    ])
    # entreno el modelo
    new_model.fit(X, y)
    # reasigno model
    model = new_model
    # abro el .pkl
    with open(MODEL_PATH, "wb") as f:
        # guardo el modelo recién entrenado, reemplazando el archivo del modelo antiguo
        pickle.dump(model, f)
    # devuelvo el mensaje exacto del test (con el punto final)
    return jsonify({"message": "Modelo reentrenado correctamente."})

# solo arranco el servidor si ejecuto este archivo directamente
if __name__ == "__main__":
    # hago flask accesible desde fuera, en el puerto 8000
    app.run(host="0.0.0.0", port=8000, debug=False)

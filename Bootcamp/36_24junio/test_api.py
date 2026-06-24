# importo requests para lanzar peticiones http al servidor desde el test
import requests

# test para el endpoint de ingesta
def test_ingest_endpoint():
    # apunto al endpoint de ingesta
    url = 'http://localhost:8000/ingest'  
    # preparo dos filas con 4 valores cada una (tv, radio, newspaper, sales)
    data = {'data': [[100, 100, 200, 3000], [200, 230, 500, 4000]]}
    # mando un post con los datos en formato json
    response = requests.post(url, json=data)
    # compruebo que el servidor responde 200 (todo ok)
    assert response.status_code == 200
    # compruebo que el mensaje devuelto es exactamente el esperado
    assert response.json() == {'message': 'Datos ingresados correctamente'}

# test para el endpoint de predicción
def test_predict_endpoint():
    # apunto al endpoint de predicción
    url = 'http://localhost:8000/predict'  
    # aquí solo 3 valores por fila
    data = {'data': [[100, 100, 200]]} 
    # uso get
    response = requests.get(url, json=data)
    # compruebo que responde 200
    assert response.status_code == 200
    # me basta con que venga la clave prediction, no compruebo el valor exacto
    assert 'prediction' in response.json()

# test para el endpoint de reentreno
def test_retrain_endpoint():
    # apunto al endpoint de reentrenamiento
    url = 'http://localhost:8000/retrain' 
    # mando un post sin body, porque retrain no necesita datos de entrada 
    response = requests.post(url)
    # compruebo que responde 200
    assert response.status_code == 200
    # compruebo el mensaje exacto
    assert response.json() == {'message': 'Modelo reentrenado correctamente.'}
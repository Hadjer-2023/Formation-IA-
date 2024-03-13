# pip install fastapi
# pip install uvicorn

# Librairies:

from joblib import load
from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
from sklearn.datasets import load_iris

iris = load_iris()

# chargement du modèle : 

loaded_model = load('logreg.joblib')

# création-d'une_nouvelle_instance_fastapi:

app = FastAPI()

# définir_un_objet(une_classe) pour réalisée des requettes: 
# dot notation (.)

class request_body(BaseModel):
    sepal_length : float
    sepal_width : float
    petal_length : float
    petal_width : float

# Définition du chemin du point de terminaison (API): 
    

@app.post("/predict")  # locall : http://127.0.0.1:8000/predict

# definition_de_la_fonction_de_prédiction:

def predict(data :request_body ) : 
    # nouvelles_données_sur_les_quelles_on_fait_la_prédiction:

    new_data = [[
        data.sepal_length,
        data.sepal_width,
        data.petal_length,
        data.petal_width
    ]]

    # prediction:

    class_idx = loaded_model.predict(new_data)[0]

    # je_retourne_le_nom_de_l'espèce_iris:

    return {'class' : iris.target_names[class_idx]}


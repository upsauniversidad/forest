import pandas as pd
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble impor RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.processing import LabelEncoder
from sklearn.metrics import classification_report, confusion_matrix

#mostrar datos
ds = pd.read_csv("dataset_financiero_riesgo.csv")

#Colocar un título principal en la página web
st.title("Predicción de Riesgo Financiero")

#Cargar los datos en la memoriaCACHE para mejorar la velocidad del acceso 
#al conjunto de datos
@st.cache_data

#Hacemos una función q se llama cargar_datos. Leemos el archivo en una variable
#y retornamos la variable alq llama a la función. En este caso la variable
#que retornamos se llama "ds", abreviatura de "dataset"
def cargar_datos():
    ds = pd.read_csv("dataset_financiero_riesgo.csv")
    return ds

ds = cargar_datos()
st.write("Vista previa de los datos")
st.dataframe(ds.head())



    
    


import streamlit as st
# import pandas as pd
# from sklearn.neural_network import MLPClassifier
# from sklearn.pipeline import Pipeline
from joblib import dump, load
import warnings
warnings.simplefilter('ignore')

modelo = load('twitter.joblib')


st.title("Twitter Analysis Sentiment")
st.divider()

texto = st.text_input("Envie um Tweet: ")

if texto:
    txt = modelo.predict([texto])
    st.write(f"Seu tweet foi classificado como {txt}")
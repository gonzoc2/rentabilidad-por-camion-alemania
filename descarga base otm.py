import streamlit as st
import desarrollo_finanzas as ff
from datetime import date, timedelta

def rango_mes_pasado():
    hoy = date.today()
    primero_mes_actual = hoy.replace(day=1)
    ultimo_mes_pasado = primero_mes_actual - timedelta(days=1)
    primero_mes_pasado = ultimo_mes_pasado.replace(day=1)
    return primero_mes_pasado, ultimo_mes_pasado

fecha_ini, fecha_fin = rango_mes_pasado()

# Llama tu función
df = ff.reportes_otm_raw(fecha_ini, fecha_fin)
st.head(df)



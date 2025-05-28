import numpy as np
import altair as alt
import pandas as pd
import streamlit as st
st.header('st.write')
# Example 1
st.write('**Hola** :dizzy:')
# Example 2
st.write('_Primer df_')
# Example 3
df = pd.DataFrame({
    'Nombre': ['Ana', 'Luis', 'Carlos', 'Sofía'],
    'Edad': [23, 30, 25, 22],
    'Ciudad': ['CDMX', 'Monterrey', 'Guadalajara', 'Puebla'],
    'Calificación': [8.7, 9.1, 7.5, 9.3]
})
st.write(df)
# Example 4
df = pd.DataFrame(
    np.random.randn(200, 3),
    columns=['a', 'b', 'c'])
c = alt.Chart(df).mark_circle().encode(
    x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])
st.write(c)
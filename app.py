import streamlit as st
import pandas as pd

def extract_suppliers_from_excel(excel_file):
    try:
        df = pd.read_excel(excel_file)
    except Exception as e:
        st.write(f"Error reading the Excel file: {e}")
        return []
    
    df = df.rename(columns={
        'nom_proveedor': 'suppler_name',
        'producto': 'product',
        'costo_unitario': 'unit_cost'
    })

    df['unit_cost'] = df['unit_cost'].astype(float)

    df = df[['suppler_name', 'product','unit_cost']]

    st.write(df)

st.title("Upload suppliers information list Excel file")
uploaded_file = st.file_uploader("Choose a Excel file", type=["xls","xlsx"])
if uploaded_file is not None:
    extract_suppliers_from_excel(uploaded_file)
    st.write("Upload successful")
import streamlit as st
import pandas as pd

st.title('Inventory Discrepancy')

st.sidebar.header("Expected Data")
fileExpected = st.sidebar.file_uploader('Upload an expected data CSV file', type="csv")

st.sidebar.header("Counted Data")
fileCounted = st.sidebar.file_uploader('Upload a counted data CSV file', type="csv")

if fileExpected and fileCounted:

    df_expected = pd.read_csv(fileExpected, encoding="latin-1",dtype=str)
    st.text("Expected Data")
    st.dataframe(df_expected.head().T)
    st.markdown("---") 

    df_counted = pd.read_csv(fileCounted, encoding="latin-1",dtype=str)
    st.text("Counted Data")
    st.dataframe(df_counted.head().T)
    st.markdown("---") 

    try:
        df_counted=df_counted.drop_duplicates("RFID")
        df_B = df_counted.groupby("Retail_Product_SKU").count()[["RFID"]].reset_index().rename(columns={"RFID":"Retail_CCQTY"})
        columns =['Retail_Product_Level1Name',
            'Retail_Product_Color',
            'Retail_Product_Level2Name',
            'Retail_Product_Level3Name',
            'Retail_Product_Level4Name',
            'Retail_Product_Level5Name',
            'Retail_Product_Name',
            'Retail_Product_SKU',
            'Retail_Product_Size',
            'Retail_Product_Style',
            'Retail_SOHQTY']
        df_A = df_expected[columns]
        df_discrepancy = pd.merge(df_A, df_B, how='outer', left_on='Retail_Product_SKU',right_on='Retail_Product_SKU', indicator = True)
        df_discrepancy['Retail_CCQTY'] = df_discrepancy['Retail_CCQTY'].fillna(0).astype(int)
        df_discrepancy['Retail_SOHQTY'] = df_discrepancy['Retail_SOHQTY'].fillna(0).astype(int)
        df_discrepancy['Diff'] = df_discrepancy['Retail_CCQTY'] - df_discrepancy['Retail_SOHQTY']
        df_discrepancy.loc[df_discrepancy['Diff']<0,"Unders"] = df_discrepancy ["Diff"]*-1
        df_discrepancy['Unders'] = df_discrepancy['Unders'].fillna(0)

        st.text("Discrepancy Data")
        st.dataframe(df_discrepancy.head().T)
        st.markdown("---") 

        option = st.sidebar.selectbox('Analyzed by', ('Retail_Product_Level1Name',
            'Retail_Product_Color',
            'Retail_Product_Name',
            'Retail_Product_Size',
            'Retail_Product_Style'))

        df_results = df_discrepancy.groupby(option).sum()

        st.text("Analysis by " + option)
        st.dataframe(df_results)


    except Exception:
        st.sidebar.text('Please provide valid data files')
        

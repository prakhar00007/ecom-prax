import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns

def main():
    st.title("E-commerce Sales Data Analysis")
    st.sidebar.title("Upload your Excel file")
    upload_file=st.sidebar.file_uploader("Upload Your File here",type=['csv','xlsx'])

    if upload_file is not None:
        try:
            if upload_file.name.endswith('.csv'):
                data=pd.read_csv(upload_file)
            else:
                data=pd.read_excel(upload_file)

                st.sidebar.success("File Uploaded Successfully")

                st.subheader("Showing You Data Details")
                st.dataframe(data.head())

                st.write("Shape of your data is: {}".format(data.shape))
                st.write("Columns in your data are: {}".format(data.columns.tolist()))
                st.write('null data count',data.isnull().sum())
                st.write('more description about the data',data.describe())
        except Exception as e:
            print(e)
            


if __name__ == "__main__":
    main()
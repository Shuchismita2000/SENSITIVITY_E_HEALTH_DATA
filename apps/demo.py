import streamlit as st
import pandas as pd


def app():
    st.header("Sensitivity Of E-Health Data")
    st.caption("Maintaining Privacy of Patients & Utility of Data")
    uploaded_file = st.file_uploader("Upload raw data")
    transaction_user = pd.read_csv("data_csv/transaction-user.csv")

    if uploaded_file is not None:
        options = st.radio("Show", ('Database', 'Attributes', 'Quasi-Identifiers','weights'
                                    'Transformed Data', 'Sensitivity of Attribute'))
        df = pd.read_csv(uploaded_file)
        if options == 'Database':
            st.table(df.head())
        if options == 'Attributes':
            st.markdown("""name,Contact,age,gender,height,weight,ap_hi,ap_lo,cholesterol,gluc,
            smoke,alco,active,cardio,BMI,BMICat,pneumonia,diabetes,copd,asthma,inmsupr,city,
            Insurance_ID,InsuranceAmount,Married,Income,medicine""")

        if options == 'Quasi-Identifiers':
            st.markdown('name,Contact,,Insurance_ID,InsuranceAmount')

        if options == 'weights':
            st.table("data_csv/weights.csv")


        if options == 'Transformed Data':
            doctor = pd.read_csv("data_csv/Doctor_transaction.csv")
            pathologist = pd.read_csv("data_csv/pathologis_transaction.csv")
            pharmacist = pd.read_csv("data_csv/pharmasist_transaction.csv")
            researcher = pd.read_csv("data_csv/researcher_transaction.csv")
            st.table(doctor.head())
            st.table(pathologist.head())
            st.table(pharmacist.head())
            st.table(researcher.head())

        if options == 'Sensitivity of Attribute':
            sensitive = pd.read_csv("dataframe_csv/sensitive.csv")
            st.table(sensitive)

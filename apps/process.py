import streamlit as st
import pandas as pd


def app():
    global pathologist, doctor, pharmasist, researcher, H
    st.header("Sensitivity Of E-Health Data")
    st.caption("Maintaining Privacy of Patients & Utility of Data")

    st.subheader("The Process")
    st.caption("Try to divide the whole process into some steps")
    with st.expander("Input"):
        st.markdown("""
                As input we will take raw data of patients from hospitals where will present their name,personal 
                information,health data even payment information.
                """)
    with st.expander("Initial Analyse Attributes "):
        st.markdown("""
                From that raw data first we will pick the attributes and by analyzing them we can define identifiers 
                and quasi identifiers and other attributes.
                
                Explicit identifier attributes Q = {Ei1,…,Eik} ⊆ {Ai,…,An} are attributes that can be used to identify a 
                specific entity that the specific information is about. Basically Explicit identifiers are unique in 
                nature.  
                
                Quasi identifier attributes Q = {qi1,…,qik} ⊆ {Ai,…,An} are attributes that can be linked, possibly 
                using an external data source, to reveal a specific entity that the specific information is about. 
                In addition, any subset of the quasi-identifiers (consisting of one or more attributes of Q) is a 
                quasi-identifier itself.
                
                Now our main attention goes to other attributes to 
                predict sensitivity.
            """)
    with st.expander("Transformed Data"):
        st.image("image/Transactional_matrix.png")
        st.markdown("""
                We will extract remaining attributes from raw data and creating a new form of data.
                At first , we give attention who are the users of health data of patients.Then We get 4types of user as 
                answer: Doctor , Pathologist ,Pharmacist and Researcher. 
                If we can collect enough information from those users that which attributes they need for further then  
                we can generalize the format and using prediction model we can create transformed data.
                 
            """)
    with st.expander("Weights of Attributes"):
        st.markdown("""
                We will check which attribute makes more importance to the different users and that wise weights will 
                be given to the attributes which value varies between 0 to 1.
            """)
        if st.caption("CODE OF WEIGHT"):
            with st.echo():
                weight = pd.read_csv("data_csv/weights.csv")
                weight = weight.set_index('Unnamed: 0')
                weight.index.names = [None]


    with st.container():
        st.image("image/user_acces.png")
        st.markdown("""
                Ui = Represent the User i.
                RiUi = Represent the request j set by the user i.
                Di = represents the attribute i in dataset D.
                Ui;Dj = represent the attribute j has been requested by user i.
                RiDiDj = represent the data attribute i from dataset D, j from dataset D in the request i. 
        
                Data sensitivity is dependent on several factors. In the proposed entropy model, we consider three factors that
                contribute to data sensitivity. These factors and the reasons for using them are as follows.
            
                Shannon's entropy is adopted to estimate data sensitivity based on these three factors. Shannon's entropy for
                a discrete random variable X can be computed from Equation 
                    """)
        st.image("image/entropy.png")

    with st.expander("Entropy of Attributes"):
        st.markdown("""
                Data Quality – the higher the data quality of a dataset in terms of missing data and corrupted or erroneous
                data, the more sensitive it becomes.
            """)
        st.image("image/attribute.png")

        if st.caption("CODE OF ENTROPY"):
            with st.echo():
                def entropy_of_attribute():
                    s = 0
                    e = []
                    value1 = []
                    for c in weights.columns:
                        for i in range(0, weights.shape[0]):
                            s = s + (-(weights[c][i] * math.log(weights[c][i])))
                        e.append(s)
                        value1.append(s)
                        s = 0
                    H1 = {}
                    for key in weights.columns:
                        for value in value1:
                            H1[key] = value
                            value1.remove(value)
                            break

                    attribute_entropy_df = pd.DataFrame.from_dict(H1, orient='index').rename(
                        columns={0: 'Entropy of attribute'})

    with st.expander("Entropy of Usability "):
        st.markdown("""
                Data Usability– The more a data item is used, the more sensitive it is because of the probability that 
                the data item could be abused/misused increases with its usage.
                
            """)
        st.image("image/proba_usability.png")
        st.image("image/usability.png")

        if st.caption("CODE OF USABILITY"):
            with st.echo():
                def usability():
                    global doctor, pathologist, pharmasist, researcher

                    def counting_yes(dataset, column_a, column_b):
                        l = []
                        count = 0
                        c = dataset.columns[column_a:column_b]
                        for i in range(0, c.shape[0]):
                            for j in range(0, dataset.shape[0]):
                                if (dataset[c[i]][j] == 1):
                                    count = count + 1
                            l.append(count)
                            count = 0
                        b = {}
                        for key in c:
                            for value in l:
                                b[key] = value
                                l.remove(value)
                                break
                        return b

                    D_C_1 = counting_yes(doctor, 0, doctor.shape[1] - 1)
                    PA_C_1 = counting_yes(pathologist, 0, pathologist.shape[1] - 1)
                    PH_C_1 = counting_yes(pharmasist, 0, pharmasist.shape[1] - 1)
                    R_C_1 = counting_yes(researcher, 0, researcher.shape[1] - 1)

                    d_sum = 0
                    pa_sum = 0
                    ph_sum = 0
                    r_sum = 0
                    for i in D_C_1:
                        d_sum = d_sum + D_C_1[i]
                    for i in PA_C_1:
                        pa_sum = pa_sum + PA_C_1[i]
                    for i in PH_C_1:
                        ph_sum = ph_sum + PH_C_1[i]
                    for i in R_C_1:
                        r_sum = r_sum + R_C_1[i]

                    p_atr_pathologist = []
                    P_atr_pathologist = {}
                    for i in PA_C_1:
                        p = (PA_C_1[i]) / pa_sum
                        p_atr_pathologist.append(p)
                    for key in pathologist.columns:
                        for value in p_atr_pathologist:
                            P_atr_pathologist[key] = value
                            p_atr_pathologist.remove(value)
                            break

                    p_atr_pharmacist = []
                    P_atr_pharmacist = {}
                    for i in PH_C_1:
                        p = (PH_C_1[i]) / ph_sum
                        p_atr_pharmacist.append(p)
                    for key in pharmasist.columns:
                        for value in p_atr_pharmacist:
                            P_atr_pharmasist[key] = value
                            p_atr_pharmacist.remove(value)
                            break

                    p_atr_researcher = []
                    P_atr_researcher = {}
                    for i in D_C_1:
                        p = (R_C_1[i]) / r_sum
                        p_atr_researcher.append(p)
                    for key in researcher.columns:
                        for value in p_atr_researcher:
                            P_atr_researcher[key] = value
                            p_atr_researcher.remove(value)
                            break

                    doctor = pd.DataFrame.from_dict(P_atr_doctor, orient='index')
                    doctor = doctor.rename(columns={0: 'Doctor'})
                    pathologist = pd.DataFrame.from_dict(P_atr_pathologist, orient='index')
                    pathologist = pathologist.rename(columns={0: 'Pathologist'})
                    pharmasist = pd.DataFrame.from_dict(P_atr_pharmasist, orient='index')
                    pharmasist = pharmasist.rename(columns={0: 'Pharmasist'})
                    researcher = pd.DataFrame.from_dict(P_atr_researcher, orient='index')
                    researcher = researcher.rename(columns={0: 'Resercher'})

                    usability = pd.concat([doctor, pathologist, pharmasist, researcher], axis=1)
                    usability_attribute = usability.sum(axis=1)
                    usability_attribute_df = pd.DataFrame(usability_attribute).rename(columns={0: 'Usability'})

                    s = 0
                    e = []
                    for i in range(0, 22):
                        if (usability_attribute[i] != 0):
                            s = s + (-(usability_attribute[i] * math.log(usability_attribute[i])))
                            e.append(s)
                            s = 0
                        else:
                            e.append(0)
                    H2 = {}
                    for key in usability_attribute_df.T.columns:
                        for value in e:
                            H2[key] = value
                            e.remove(value)
                            break

                    usability_entropy_df = pd.DataFrame.from_dict(H2, orient='index').rename(
                        columns={0: 'Entropy of Usability'})

    with st.expander("Entropy of Associativity"):
        st.markdown("""
                Associativity – the more attributes in one relation that are used to connect or join to other data items in
other datasets, the more sensitive it is.
            """)
        st.image("image/proba_asso.png")
        st.image("image/Associativity.png")
        if st.caption("CODE OF ASSOCIATIVITY"):
            with st.echo():
                def associativity():
                    age_data = transaction_user.groupby('age').get_group(1).reset_index().drop(['index', 'User'],
                                                                                               axis=1)
                    age_1 = pd.DataFrame.from_dict(counting_yes(age_data, 0, 22), orient='index').rename(
                        columns={0: 'Age'})

                    associativity = pd.concat(
                        [age_1, gender_1, height_1, weight_1, ap_hi_1, ap_lo_1, cholesterol_1, gluc_1, smoke_1,
                         alco_1,
                         active_1, cardio_1, BMI_1, BMICat_1, pneumonia_1, diabetes_1, copd_1, asthma_1, inmsupr_1,
                         city_1, Married_1, Income_1, Medicine_1], axis=1)

                    s = 0
                    e = []
                    for i in range(0, 22):
                        for j in range(i, 22):
                            if (associativity.iat[i, j] != 0):
                                s = s + (-((associativity.iat[i, j] / associativity.iat[i, 22]) * math.log(
                                    (associativity.iat[i, j] / associativity.iat[i, 22]))))
                                e.append(s)
                                s = 0
                    H3 = {}
                    for key in associativity.T.columns:
                        for value in e:
                            H3[key] = value
                            e.remove(value)
                            break

                    associativity_entropy_df = pd.DataFrame.from_dict(H3, orient='index').rename(
                        columns={0: 'Entropy of associativity'})

    with st.expander("Combined Entropy"):
        st.markdown("""
                The combined entropy measure is the product of all the three entropy measures
            """)
        st.image("image/combined.png")

        if st.caption("CODE OF COMBINED ENTROPY"):
            with st.echo():
                def combined_entropy():
                    x = []
                    for i in range(0, 22):
                        Combined = attribute_entropy_df.iat[i, 0] * usability_entropy_df.iat[i, 0] * \
                                   associativity_entropy_df.iat[i, 0]
                        x.append(Combined)
                    H4 = {}
                    for key in usability_attribute_df.T.columns:
                        for value in x:
                            H4[key] = value
                            x.remove(value)
                            break

                    combined_entropy_df = pd.DataFrame.from_dict(H4, orient='index').rename(
                        columns={0: 'Combined Entropy'})

    with st.expander("Sensitivity of Attributes"):
        st.markdown("""
                Base on combined entropy we classify the attributes are sensitive or not.We will set a threshold which 
                help to predict from combined entropy
            """)

        if st.caption("CODE OF SENSITIVITY"):
            with st.echo():
                def sensitivity():
                    s = []
                    for i in range(0, 22):
                        if (combined_entropy_df.iat[i, 0] > 0.035):
                            s.append("Yes")
                        else:
                            s.append("No")
                    dataset = pd.concat(
                        [attribute_entropy_df, usability_entropy_df, linkability_entropy_df, combined_entropy_df],
                        axis=1)
                    dataset.to_csv("sensitive.csv")

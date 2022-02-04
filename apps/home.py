import streamlit as st


def app():
    st.header("Sensitivity Of E-Health Data")
    st.caption("Maintaining Privacy of Patients & Utility of Data")

    with st.container():
        st.subheader("Utility")
        st.markdown("""
            If we ask Why health data is important in research? Then as answer we get many points
            Diagnosis of rare diseases
            Improving the performance of health system
            Identifying disease early
            Studying the effects of immunisation
            Better understanding why certain populations are affected differently by the same disease 
            Accessing the safety of medical interventions
            Making connections between diseases and lifestyle choices

            """)


    with st.container():
        st.subheader("Data Leakage Possibility")
        st.image("image/data_usage.png")
        st.markdown("""
            Accidental disclosure : Healthcare personnel unintentionally disclose patient information 
            to others 
            Insider curiosity : An insider with data-access privilege pries upon a patient’s records 
            out of curiosity or for their own purpose
            Data breach by insider : Insiders access patient information and transmit it to outsiders 
            for profit or revenge.
            Data breach by outsider with physical intrusion : An outsider enters the physical facility 
            either by coercion or forced entry and gains access to the system. 
            Unauthorised intrusion of network system : An outsider, including former employees, 
            patients, or hackers, intrudes into an organisation’s network from the outside to gain 
            access to patient information or render the system inoperable.  

        """)
    with st.container():
        st.subheader("Privacy Concern")
        st.markdown("""
            Patients strongly believe that their information should 
            be shared only with people involved in their care. 

            Patients do identify with the need for information sharing among physicians, 
            though HIV patients are less likely to approve sharing of their health information. 

            Many patients who agree to information sharing among physicians reject the 
            notion of releasing information to third parties, including employers and family members. 

            The majority of patients who have undergone genetic testing believe that 
            patients should bear the responsibility of revealing test results to other at-risk family members. 

            Only about 28–35% of patients are neutral to their health information – such as age, gender, 
            ethnicity, reason for treatment, medical history, personal habits impacting health, type of treatment 
            obtained, side effects of treatment being used by physicians for other purposes. 

            Only about 5–21% of patients, however, expected to be asked for permission to use their information 
            by their physicians. 

            Only about 10% of the patients expected to be asked for permission if their doctors used their 
            health information for a wide variety of purposes, including combining data with other patients’ 
            data to provide better information to future patients, sharing treatment outcomes with other 
            physicians, teaching medical professionals and writing research articles about diseases and treatments. 

            """)

    with st.container():
        st.subheader("Main Goal")
        st.image("image/main_goal.png")
        st.markdown("""Now , our main goal is to maintain the balance between utility and privacy.We must want data 
            for analyzing and improving our health system.Other  hand, we have to respect the privacy of patients 
            with our humanity. 

             """)
    with st.container():
        st.subheader("Process")
        st.image("image/process.png")
        st.markdown("""Now , our main goal is to maintain the balance between utility and privacy.We must want data 
            for analyzing and improving our health system.Other  hand, we have to respect the privacy of patients 
            with our humanity. 

             """)


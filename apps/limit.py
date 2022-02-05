import streamlit as st


def app():
    st.header("Sensitivity Of E-Health Data")
    st.caption("Maintaining Privacy of Patients & Utility of Data")

    with st.container():
        st.subheader("Limitation & Future Goal")
        st.markdown("""
        
            1. We have no proper structure of data which can we get from hospitals even every type of user's need.So, for now , we assume and create the data
             
            2. We have to create a prediction model which can predict weights of attribute. But ,till we cannot able to create that model ,so we assume the weights
            
            3. We have to generalize the functions of usability and associativity, for now ,for limited no of attributes we do every line of code manually
            
            4. Setting the threshold value is not the proper way to predict sensitivity, we have to create a function or range which will applicable every unknown attributes
            
            """)

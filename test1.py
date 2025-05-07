import streamlit as st 

col1, col2 = st.columns([2,3])
tab1, tab2 = st.tabs(['Tab A','Tab B'])
with col1 :
    st.title("Here is column1 title")
    with tab1 : 
        st.write('Hello')
    with tab2 :
        st.write('hi')
    st.checkbox("this is checkbox1 in col1")

with col2 :
    st.title("Here is column2 title")
    st.checkbox("this is checkbox1 in col2")

col1.subheader("i am column1 subheader")
col2.checkbox("this is checkbox2 in col2")
with tab1 : 
        st.write('Hello')
with tab2 :
        st.write('hi')
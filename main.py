import streamlit as st
from streamlit_chat import message

from bardapi import Bard

token = '******************.'

#Function to generate the output
def generate_response(prompt):
    bard = Bard(token=token)
    response = bard.get_answer(prompt)['content']
    return response
#Fucntion to ecive user queries
def get_text():
    input_text=st.text_input('Ask Your Question Here:', "Hello", key='input')
    return input_text

#Title
st.title('My Personal Tutoring Bot')

#url= 'https://images.unsplash.com/photo-1567524667890-dba7c551ee1f?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=871&q=80'
#data-testid="stAppViewContainer"

changes='''
<style>
[data-testid="stAppViewContainer"]
    {
    background-image:url("https://images.unsplash.com/photo-1543722530-d2c3201371e7?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=2074&q=80");
    background-size: cover;
    }
    html{
    background: transparent;
    }
    div.esravye2 > iframe
    {
    background-color:transparent;
    }
</style>
'''
st.markdown(changes, unsafe_allow_html=True)

#print(st.session_state)
if 'generated' not in st.session_state:
    st.session_state['generated']=[]

if 'past' not in st.session_state:
    st.session_state['past']=[]



#Acception user input
user_input=get_text()
if user_input:
    print(user_input)
    output=generate_response(user_input)
    print(output)
    st.session_state['past'].append(user_input)
    st.session_state['generated'].append(output)

if st.session_state['generated']:
    for i in range(len(st.session_state['generated'])-1, -1, -1):
        message(st.session_state['generated'][i], key=str(i))
        message(st.session_state['past'][i], key="user_"+str(i), is_user=True)

#prompt=input('Write our text')
#response=generate_response(prompt)
#print(response)
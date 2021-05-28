import requests
import json
import streamlit as st

url = "https://mgmt590-rest-api-kprv24rveq-uc.a.run.app/answer"

st.title('Amazing Question Answering Thing!')

# Inputs
question = st.text_input('Question')
context = st.text_area('Context')

# Execute question answering on button press
if st.button('Answer Question'):

    payload = json.dumps({
        "question": question,
        "context": context
        })
    headers = {'Content-Type': 'application/json'}
    response = requests.request("POST", url, headers=headers, data=payload)
    answer = response.json()['answer']

    st.success(answer)

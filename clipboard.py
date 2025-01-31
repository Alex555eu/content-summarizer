from streamlit_paste_button import paste_image_button as pbutton
import time
import streamlit as st


# Someday may be useful 

def printClipboardData():
    for idx, image in enumerate(st.session_state.clipboard_data):
        col1, col2 = st.columns([1, 6])
        with col1:
            st.image(image)
        with col2:
            if st.button("", key=f"delete_{int(time.time() * 1000)}", icon=":material/close:", type="tertiary"):
                st.session_state.clipboard_data.remove(image)
                #st.rerun() 


def makeClipboard():
    if 'clipboard_data' not in st.session_state:
        st.session_state.clipboard_data = []
    paste_result = pbutton("Add from clipboard")
    if paste_result.image_data is not None:
        st.session_state.clipboard_data.append(paste_result.image_data)
    printClipboardData()
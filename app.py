import streamlit as st
from utils import media2text, chatreq


# removes data of files, which no longer exist in current session
def reduceSessionState(expected_keys):
    current_keys = list(st.session_state.extracted_data.keys())
    for key in current_keys:
        if key not in expected_keys:
            del st.session_state.extracted_data[key]

if 'extracted_data' not in st.session_state:
    st.session_state.extracted_data = {}

st.title("Content Summarizer")
st.write("Application providing a solution for generating summaries from various types of content, including images, audio, and video.")

st.divider()

uploaded_files = st.file_uploader("", type=["png", "jpg", "jpeg", "mp3", "mp4", "pdf"], accept_multiple_files=True)

if uploaded_files is not None and len(uploaded_files) > 0:
    uploaded_files_names = list(map(lambda x: x.name, uploaded_files))
    reduceSessionState(uploaded_files_names)
    st.write("Extracted text:")
    with st.spinner("Loading..."):
        for uploaded_file in uploaded_files:
            if uploaded_file.name in list(st.session_state.extracted_data.keys()):
                result = st.session_state.extracted_data[uploaded_file.name]
            else:
                try:
                    result = media2text.extractText(uploaded_file)
                    st.session_state.extracted_data[uploaded_file.name] = result
                    with st.expander(f"{uploaded_file.name}"):
                        st.write(result)
                except AttributeError as err:
                    st.toast(err)


choices = {'ENG': 'English', 'PL': 'Polski'}
selected_response_language = st.selectbox("Select summary language", options=list(choices.keys()), format_func=(lambda x: choices[x]))

if st.button("Generate summary", disabled=not st.session_state.extracted_data):
    st.divider()
    with st.spinner("Generating..."):
        request_content = ' '.join(st.session_state.extracted_data.values())
        stream = chatreq.llmRequest(request_content, selected_response_language)
        output = st.empty()
        full_response = ""
        for chunk in stream:
            if chunk.choices[0].delta.content is not None:
                full_response += chunk.choices[0].delta.content
                output.markdown(full_response, unsafe_allow_html=True)
        st.divider()
        if st.button("Clear all", key="delete-btn", icon=":material/delete_sweep:", type="primary"):
            output.empty()
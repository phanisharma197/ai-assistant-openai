import streamlit as st
from ai_client import ask_text 
from helpers import create_message

#setup config
st.set_page_config(
    page_title = "JARVIS AI",
    page_icon = "🤖",
    layout = "wide"
)

#session state intialization 
if "messages" not in st.session_state:
    st.session_state.messages = []

#previous response id initialization
if "previous_response_id" not in st.session_state:
    st.session_state.previous_response_id = None


#Sidebar
with st.sidebar:
    st.title("🤖 Jarvis")

    st.divider()
    st.write("### Features")
    st.write("✅ Chat")
    st.write("✅ Image Description")

#Main Page
st.title("🤖 Jarvis")

st.write("ask me anything and I will try to answer your questions or you can upload image and I will describe the image for you")

#Image Uploader
uploaded_image = st.file_uploader("upload an Image",
                 type = ["png", "jpg", "jpeg"])


if uploaded_image:
    st.image(uploaded_image, caption = "uploaded Image")


#session usage
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])


#chat input
prompt = st.chat_input("Ask anything....")

if prompt:
    #save user message in session state
    st.session_state.messages.append(
        create_message("user", prompt)
    )

    with st.chat_message("user"):
        st.write(prompt)

    #create assistant bubble
    with st.chat_message("assistant"):

        assistant_placeholder = st.empty()

        with st.spinner("Jarvis is thinking..."):

            stream = ask_text(prompt,st.session_state.previous_response_id)
            
            full_response = ""


        for event in stream:
            if event.type == "response.output_text.delta":
                full_response += event.delta
                assistant_placeholder.markdown(full_response)
            elif event.type == "response.completed":
                st.session_state.previous_response_id = event.response.id    
                
                

        


        st.session_state.messages.append(
            create_message("assistant", full_response)
    )

    st.rerun()


    
    

    
    
    

    
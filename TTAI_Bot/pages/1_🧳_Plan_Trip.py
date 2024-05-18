
from openai import OpenAI
import streamlit as st
from datetime import datetime
from PIL import Image  # this is for image to be added

st.set_page_config(
    page_title="Plan Trip",
    page_icon="🧳",
    layout="wide",
)

st.title("Trip Trouve AI")
st.write("Hello, :smile: Fellow Explorer!")
st.write(
    "Where shall our journey take us today? Let's map our adventure together. 🤝🏻")
st.write(" What's on your tarvel agenda? 🤔")

# Add a title to the sidebar
st.sidebar.title("Plan your trip 	:briefcase: ")

# Add a date selection widget for start date from datetime
start_date = st.sidebar.date_input(
    "Start Date 	:grey_question: ", datetime.today())

# Add a date selection widget for end date from datetime
end_date = st.sidebar.date_input(
    "End Date 	:grey_question:", datetime.today())

# Add a text input widget for entering text
user_text = st.sidebar.text_input(
    "Estimated Budget (Rs.)	:money_with_wings: ")


travel_preferences = ["Train 🚍", "Flight ✈️", "Car 🚗 "]

# Add radio button widget for selecting travel preferences
selected_preference = st.sidebar.radio(
    "Select Travel Preference 📌", travel_preferences)

if st.sidebar.button("Show Selected Options",  type="primary"):
    # Display the selected options
    st.sidebar.subheader("Selected options ✔️")
    st.sidebar.write("Start Date:", start_date)
    st.sidebar.write("End Date:", end_date)
    st.sidebar.write("Budget in Rs:", user_text)
    st.sidebar.write("Selected Travel Preference:", selected_preference)

    # soon pass prompt to gpt
    st.sidebar.button("Generate Itinerary ✔️", type="primary")

# if "total_budget" not in st.session_state:
#     # Replace 10000 with the actual total budget entered by the user
#     st.session_state.total_budget = 'user_text'
# st.chat_input() can't be used inside an st.expander, st.form, st.tabs, st.columns, or st.sidebar.
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-3.5-turbo"

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Enter your prompt here!"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        stream = client.chat.completions.create(
            model=st.session_state["openai_model"],
            messages=[
                {"role": m["role"], "content": m["content"]}
                for m in st.session_state.messages
            ],
            stream=True,
        )
        response = st.write_stream(stream)

    st.session_state.messages.append(
        {"role": "assistant", "content": response})



# st.write("Made by Harshita Verma❗")

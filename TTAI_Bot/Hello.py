import streamlit as st
from PIL import Image
import pydeck as pdk
from streamlit_carousel import carousel
# import streamlit.components.v1 as components
st.set_page_config(
    page_title="Trip_Trouve_AI",
    page_icon="✈️",
    layout="wide",
)


st.write("# Welcome to Trip Trouve AI bot 🤖")

st.sidebar.subheader("☝ Navigate to plan with us.")

st.write("We did the change, so you don't have to.")
st.write("Enter your budget as AI comes to help you out 🤑!")


test_items = [
    dict(
        title=" ",
        text=" ",
        img="https://images.unsplash.com/photo-1522093007474-d86e9bf7ba6f?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=764&q=80",
        # link=""
    ),
    dict(
        title=" ",
        text=" ",
        img="https://images.unsplash.com/photo-1522093007474-d86e9bf7ba6f?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=764&q=80",
        # link=" "
    ),
    dict(
        title=" ",
        text=" ",
        img="https://images.unsplash.com/photo-1522093007474-d86e9bf7ba6f?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=764&q=80",
        # link=" "
    ),
    dict(
        title=" ",
        text=" ",
        img="https://images.unsplash.com/photo-1522093007474-d86e9bf7ba6f?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=764&q=80",
        # link=" "
    ),
]

carousel(items=test_items, width=0.5)

# st.write("Made by Harshita Verma ❗")

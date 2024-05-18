import streamlit as st
from PIL import Image
import random

st.set_page_config(
    page_title="Pictures",
    page_icon="📸",
    layout="wide",
)


st.markdown(
    """
    <style>
    .container {
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0px 0px 10px 0px rgba(0,0,0,0.1);
    }
    .bg-color {
        background-color: #f0f0f0;
        padding: 10px;
        border-radius: 5px;
    }
    .image-container {
        border: 20px solid;
        border-radius: 10px;
        padding: 10px;
        margin-bottom: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True
)


def generate_hotel_stay_info():
    hotels = [
        {"name": "Hotel A", "price": "Rs 1500/-"},
        {"name": "Hotel B", "price": "Rs 1800/-"},
        {"name": "Hotel C", "price": "Rs 2000/-"}
    ]
    return random.choice(hotels)

# Generate random flight information


def generate_flight_info():
    flights = [
        {"name": "Flight A", "price": "Rs 5000/-"},
        {"name": "Flight B", "price": "Rs 5500/-"},
        {"name": "Flight C", "price": "Rs 6000/-"}
    ]
    return random.choice(flights)


# Insert containers separated into tabs: personalized plans generated
tab1, tab2, tab3 = st.tabs(["Plan 1", "Plan 2", "Plan 3"])
tab1.subheader("This is recommended Plan 1 ")
tab2.subheader("This is recommended Plan 2 ")
tab3.subheader("This is recommended Plan 3 ")

total_budget = 90000

with tab1:
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(
            '<div class="bg-color"><i class="icon fas fa-hotel"></i><b>Hotels and Stays 🏨</b></div>', unsafe_allow_html=True)
        image = Image.open('assets\historical1.jpg')
        st.image(image, width=300)
        # st.markdown("</div>", unsafe_allow_html=True)
        st.write("The name and price are as follows 👇:")
        hotel_info = generate_hotel_stay_info()
        st.write(f"Name: {hotel_info['name']}")
        st.write(f"Price: {hotel_info['price']}")

    with col2:

        st.markdown(
            '<div class="bg-color"><i class="icon fas fa-plane"></i><b>Flight ✈️</b></div>', unsafe_allow_html=True)
        image = Image.open('assets\historical2.jpg')
        st.image(image, width=300)
        st.write("The name and price are as follows 👇:")
        flight_info = generate_flight_info()
        st.write(f"Name: {flight_info['name']} ")
        st.write(f"Price: {flight_info['price']} ")

    if st.button("Select Plan 1", type="primary"):
        # Display results
        st.header("Results")
        st.subheader("Plan 1 selected")

        selected_hotel_price_numeric = int(
            hotel_info['price'].split("Rs ")[1].split("/-")[0])
        selected_flight_price_numeric = int(
            flight_info['price'].split("Rs ")[1].split("/-")[0])
# Calculating remaining budget after subtracting hotel and flight prices
        remaining_budget = int(
            total_budget)-(selected_flight_price_numeric + selected_hotel_price_numeric)

        st.write("Selected Hotel:", hotel_info['name'])
        st.write("Hotel Price in Rs:", selected_hotel_price_numeric)
        st.write("Selected Flight:", flight_info['name'])
        st.write("Flight Price in Rs:",  selected_flight_price_numeric)
        st.write("You saved Rs:", remaining_budget)


with tab2:
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(
            '<div class="bg-color"><i class="icon fas fa-hotel"></i><b>Hotels and Stays</b></div>', unsafe_allow_html=True)
        image = Image.open('assets\historical3.jpg')
        st.image(image, width=300)
        # st.markdown("</div>", unsafe_allow_html=True)
        st.write("The name and price are as follows 👇:")
        hotel_info = generate_hotel_stay_info()
        st.write(f"Name: {hotel_info['name']}")
        st.write(f"Price: {hotel_info['price']}")

    with col2:

        st.markdown(
            '<div class="bg-color"><i class="icon fas fa-plane"></i><b>Flight ✈️</b></div>', unsafe_allow_html=True)
        image = Image.open('assets\historical4.jpg')
        st.image(image, width=300)
        st.write("The name and price are as follows 👇:")
        flight_info = generate_flight_info()
        st.write(f"Name: {flight_info['name']} ")
        st.write(f"Price: {flight_info['price']} ")

    if st.button("Select Plan 2", type="primary"):
        # Display results
        st.header("Results")
        st.subheader("Plan 2 selected")

        selected_hotel_price_numeric = int(
            hotel_info['price'].split("Rs ")[1].split("/-")[0])
        selected_flight_price_numeric = int(
            flight_info['price'].split("Rs ")[1].split("/-")[0])
# Calculating remaining budget after subtracting hotel and flight prices
        remaining_budget = int(
            total_budget)-(selected_flight_price_numeric + selected_hotel_price_numeric)

        st.write("Selected Hotel:", hotel_info['name'])
        st.write("Hotel Price in Rs:", selected_hotel_price_numeric)
        st.write("Selected Flight:", flight_info['name'])
        st.write("Flight Price in Rs:",  selected_flight_price_numeric)
        st.write("You saved Rs:", remaining_budget)


with tab3:
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(
            '<div class="bg-color"><i class="icon fas fa-hotel"></i><b>Hotels and Stays</b></div>', unsafe_allow_html=True)
        image = Image.open('assets\historical5.jpg')
        st.image(image, width=300)
        # st.markdown("</div>", unsafe_allow_html=True)
        st.write("The name and price are as follows 👇:")
        hotel_info = generate_hotel_stay_info()
        st.write(f"Name: {hotel_info['name']}")
        st.write(f"Price: {hotel_info['price']}")

    with col2:

        st.markdown(
            '<div class="bg-color"><i class="icon fas fa-plane"></i><b>Flight ✈️</b></div>', unsafe_allow_html=True)
        image = Image.open('assets\historical6.jpg')
        st.image(image, width=300)
        st.write("The name and price are as follows 👇:")
        flight_info = generate_flight_info()
        st.write(f"Name: {flight_info['name']} ")
        st.write(f"Price: {flight_info['price']} ")
    if st.button("Select Plan 3", type="primary"):
        # Display results
        st.header("Results")
        st.subheader("Plan 3 selected")

        selected_hotel_price_numeric = int(
            hotel_info['price'].split("Rs ")[1].split("/-")[0])
        selected_flight_price_numeric = int(
            flight_info['price'].split("Rs ")[1].split("/-")[0])
# Calculating remaining budget after subtracting hotel and flight prices
        remaining_budget = int(
            total_budget)-(selected_flight_price_numeric + selected_hotel_price_numeric)

        st.write("Selected Hotel:", hotel_info['name'])
        st.write("Hotel Price in Rs:", selected_hotel_price_numeric)
        st.write("Selected Flight:", flight_info['name'])
        st.write("Flight Price in Rs:",  selected_flight_price_numeric)
        st.write("You saved Rs:", remaining_budget)


# st.write("Made by Harshita Verma ❗")

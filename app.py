import streamlit as st

## The logic for the calculation is stored in functions in mylibrary.py
import mylibrary

## User Interface ---------------------------------------------------------------------
## Data Entry  - widgets to get the number of adults, children and the ticket type
## Calculation - call mylibrary.calculate_total and display the result
## ------------------------------------------------------------------------------------

st.title("Ticket Price Calculator for Fun Land Theme Park")

st.write("Family package: 2 adults + 2 children at a discounted price!")

## Data Entry -------------------------------------------------------------------------
st.selectbox(
    label="Select your ticket type",
    options=["standard", "express"],
    key="ticket_type"
    )

st.number_input(
    label="Number of adults",
    min_value=0,
    max_value=20,
    step=1,
    key="num_adults"
    )

st.number_input(
    label="Number of children",
    min_value=0,
    max_value=20,
    step=1,
    key="num_children"
    )

### Define a function to clear the user's inputs
def reset_inputs():
    st.session_state.ticket_type = "standard"
    st.session_state.num_adults = 0
    st.session_state.num_children = 0

## Calculation ------------------------------------------------------------------------
if st.button("Calculate total price"):
    adults = st.session_state.num_adults
    children = st.session_state.num_children
    ticket_type = st.session_state.ticket_type

    ## Check the inputs before calculating
    if adults == 0 and children == 0:
        st.warning("Please enter at least one visitor.")
    elif adults == 0 and children > 0:
        st.error("Children must be accompanied by at least one adult.")
    else:
        breakdown, total, savings = mylibrary.calculate_total(adults, children, ticket_type)
        st.table(breakdown)
        st.subheader(f"Total price: ${total}")
        if savings > 0:
            st.success(f"You saved ${savings} with the family package!")

st.button("Reset", on_click=reset_inputs)

import streamlit as st
import datetime
from controllers.client_controller import ClientController
from models.client import ClientCreate
from pydantic import ValidationError


def create_client_view():
    st.subheader("Create New Client")
    controller = ClientController()

    with st.form(key="create_client_form", clear_on_submit=True):
        st.markdown("### Client Details")
        name = st.text_input("Name", help="Enter the client's full name.")
        birth_date = st.date_input(
            "Birth Date",
            help="Select the client's birth date.",
            max_value=st.session_state.get("today_date"),
            min_value=datetime.date(1900, 1, 1),
        )
        roles = controller.get_it_roles()
        role = st.selectbox("Role", options=roles, help="Select the client's IT role.")

        st.markdown("--- ")
        submit_button = st.form_submit_button(label="Create Client")

        if submit_button:
            try:
                client_data = ClientCreate(name=name, birth_date=birth_date, role=role)
                controller.create_client(client_data)
                st.success("🎉 Client created successfully!")
            except ValidationError as e:
                for error in e.errors():
                    st.error(f"Validation Error in {error['loc'][0]}: {error['msg']}")
            except Exception as e:
                st.error(f"An unexpected error occurred: {e}")

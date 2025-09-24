import streamlit as st
import datetime
from controllers.client_controller import ClientController
from models.client import ClientUpdate
from pydantic import ValidationError


def edit_client_view():
    st.subheader("Edit Client Details")
    controller = ClientController()

    client_id = st.session_state.get("edit_client_id")

    if not client_id:
        st.warning(
            "⚠️ No client selected for editing. Please go to 'List Clients' to select one."
        )
        return

    client = controller.get_client(client_id)

    if not client:
        st.error(f"❌ Client with ID {client_id} not found.")
        return

    st.info(f"Currently editing client: **{client.name} (ID: {client.id})**")

    with st.form(key=f"edit_client_form_{client_id}"):
        st.markdown("### Update Client Information")
        name = st.text_input(
            "Name", value=client.name, help="Edit the client's full name."
        )
        birth_date = st.date_input(
            "Birth Date",
            value=client.birth_date,
            help="Edit the client's birth date.",
            max_value=st.session_state.get("today_date"),
            min_value=datetime.date(1900, 1, 1),
        )
        roles = controller.get_it_roles()
        try:
            current_role_index = roles.index(client.role.value)
        except ValueError:
            current_role_index = 0
        role = st.selectbox(
            "Role",
            options=roles,
            index=current_role_index,
            help="Edit the client's IT role.",
        )

        st.markdown("--- ")
        submit_button = st.form_submit_button(label="Update Client")

        if submit_button:
            try:
                client_data = ClientUpdate(name=name, birth_date=birth_date, role=role)
                updated_client = controller.update_client(client_id, client_data)
                if updated_client:
                    st.success(
                        f"✅ Client **{updated_client.name}** updated successfully!"
                    )
                    del st.session_state.edit_client_id
                    st.session_state.page = "List Clients"
                    st.rerun()
                else:
                    st.error(
                        "❌ Failed to update client. Client might not exist or data was invalid."
                    )
            except ValidationError as e:
                for error in e.errors():
                    st.error(f"Validation Error in {error['loc'][0]}: {error['msg']}")
            except Exception as e:
                st.error(f"An unexpected error occurred: {e}")

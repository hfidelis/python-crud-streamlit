import streamlit as st

from controllers.client_controller import ClientController


def list_clients_view():
    st.subheader("List Clients")
    controller = ClientController()
    clients = controller.get_clients()

    if clients:
        client_data = []
        for client in clients:
            client_data.append(
                {
                    "ID": client.id,
                    "Name": client.name,
                    "Birth Date": client.birth_date,
                    "Role": client.role.value,
                }
            )

        col_id, col_name, col_birth_date, col_role, col_edit, col_delete = st.columns(
            [0.5, 2, 1.5, 1.5, 1, 1]
        )
        with col_id:
            st.write("**ID**")
        with col_name:
            st.write("**Name**")
        with col_birth_date:
            st.write("**Birth Date**")
        with col_role:
            st.write("**Role**")
        with col_edit:
            st.write("**Edit**")
        with col_delete:
            st.write("**Delete**")

        for client in clients:
            (
                col_id,
                col_name,
                col_birth_date,
                col_role,
                col_edit,
                col_delete,
            ) = st.columns([0.5, 2, 1.5, 1.5, 1, 1])
            with col_id:
                st.write(client.id)
            with col_name:
                st.write(client.name)
            with col_birth_date:
                st.write(client.birth_date)
            with col_role:
                st.write(client.role.value)
            with col_edit:
                if st.button("Edit", key=f"edit_{client.id}"):
                    st.session_state.edit_client_id = client.id
                    st.session_state.page = "Edit Client"
                    st.rerun()
            with col_delete:
                if st.button("Delete", key=f"delete_{client.id}"):
                    st.session_state.delete_client_id = client.id
                    st.rerun()
            st.markdown("---")

        if "delete_client_id" in st.session_state and st.session_state.delete_client_id:
            client_to_delete = controller.get_client(st.session_state.delete_client_id)
            if client_to_delete:
                st.warning(
                    f"Are you sure you want to delete client: **{client_to_delete.name} (ID: {st.session_state.delete_client_id})**?"
                )
                col_confirm, col_cancel = st.columns([0.7, 0.7])
                with col_confirm:
                    if st.button(
                        "Confirm Deletion",
                        key=f"confirm_delete_button_{st.session_state.delete_client_id}",
                    ):
                        try:
                            controller.delete_client(st.session_state.delete_client_id)
                            st.success(
                                f"✅ Client with ID {st.session_state.delete_client_id} deleted successfully!"
                            )
                            del st.session_state.delete_client_id
                            st.rerun()
                        except Exception as e:
                            st.error(f"❌ Error deleting client: {e}")
                with col_cancel:
                    if st.button(
                        "Cancel",
                        key=f"cancel_delete_button_{st.session_state.delete_client_id}",
                    ):
                        del st.session_state.delete_client_id
                        st.rerun()
            else:
                st.error(
                    f"❌ Client with ID {st.session_state.delete_client_id} not found."
                )
                del st.session_state.delete_client_id
                st.rerun()
    else:
        st.info("No clients found. Create one using the 'Create Client' tab.")

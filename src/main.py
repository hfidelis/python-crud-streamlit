import streamlit as st
from views.list_clients import list_clients_view
from views.create_client import create_client_view
from views.edit_client import edit_client_view

st.set_page_config(layout="centered", page_title="Client Management App")


def main():
    if "page" not in st.session_state:
        st.session_state.page = "List Clients"

    st.sidebar.title("Navigation")

    main_pages = ["List Clients", "Create Client"]

    if st.session_state.page in main_pages:
        current_radio_index = main_pages.index(st.session_state.page)
    else:
        current_radio_index = 0

    selected_main_page = st.sidebar.radio(
        "Go to", main_pages, index=current_radio_index
    )

    if st.session_state.page == "Edit Client":
        if selected_main_page != main_pages[current_radio_index]:
            st.session_state.page = selected_main_page
            st.rerun()
    elif selected_main_page != st.session_state.page:
        st.session_state.page = selected_main_page
        st.rerun()

    if st.session_state.page == "List Clients":
        list_clients_view()
    elif st.session_state.page == "Create Client":
        create_client_view()
    elif st.session_state.page == "Edit Client":
        edit_client_view()


if __name__ == "__main__":
    main()

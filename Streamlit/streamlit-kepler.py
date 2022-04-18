import streamlit as st
from streamlit_option_menu import option_menu
from apps import home, tableau, kepler



st.set_page_config(page_title="App Real estate", layout="wide")

apps = [
    {"func": home.app, "title": "Home", "icon": "house"},
    {"func": tableau.app, "title": "Tableau", "icon": "textarea-resize"},
    {"func": kepler.app, "title": "Kepler", "icon": "map"}]

titles = [app["title"] for app in apps]
icons = [app["icon"] for app in apps]

params = st.experimental_get_query_params()

if "page" in params:
    default_index = int(titles.index(params["page"][0].lower()))
else:
    default_index = 0

with st.sidebar:
    selected = option_menu(
        "Main Menu",
        options=titles,
        icons=icons,
        menu_icon="cast",
        default_index=default_index,
    )

    st.sidebar.title("About")
   

for app in apps:
    if app["title"] == selected:
        app["func"]()
        break
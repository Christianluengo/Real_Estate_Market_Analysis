import streamlit as st
from PIL import Image

def app():

    st.title("Home")

    st.markdown(
        """
    App that allows us to analyse the real estate market using visualisation tools such as [Tableau](https://www.tableau.com/es-es) and [Kepler](https://kepler.gl/).  In the [github](https://github.com/Christianluengo/Real_Estate_Market_Analysis) repository you can find all the documentation. 
    """
    )

    imagen = Image.open("images/home.jpg")
    st.image(imagen)
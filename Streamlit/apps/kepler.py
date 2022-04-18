import streamlit as st
import streamlit.components.v1 as components

#df = pd.read_csv("../Data/data_kepler.csv")

def app():

    st.title("Kepler")

    st.markdown(
        """
    Thanks to [Kepler.gl](https://kepler.gl/) we can make a geospatial analysis of the real estate market in Spain.
    """
    )


    HtmlFile = open("kepler.html", 'r', encoding='utf-8')
    source_code = HtmlFile.read() 

    components.html(source_code,height=900)
import streamlit as st
import streamlit.components.v1 as components

def app():

    st.title("Tableau")

    st.markdown(
        """
    [Streamlit](https://streamlit.io/) allows us to visualize and interact with the dashboard without having to access Tableau.
    """
    )

    html_temp = """<div class='tableauPlaceholder' id='viz1650235623912' style='position: relative'><noscript><a href='#'><img alt='Dashboard Global ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Re&#47;RealEstateMarket_16502266573030&#47;DashboardGlobal&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='RealEstateMarket_16502266573030&#47;DashboardGlobal' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Re&#47;RealEstateMarket_16502266573030&#47;DashboardGlobal&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='es-ES' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1650235623912');                    var vizElement = divElement.getElementsByTagName('object')[0];                    if ( divElement.offsetWidth > 800 ) { vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';} else if ( divElement.offsetWidth > 500 ) { vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';} else { vizElement.style.width='100%';vizElement.style.height='2477px';}                     var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>"""
    components.html(html_temp, height=1700)


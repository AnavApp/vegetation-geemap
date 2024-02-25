import streamlit as st
import geemap.foliumap as geemap
import ee


st.set_page_config(layout="wide")

# Customize the sidebar
markdown = """
Web App URL: <https://geemap.streamlit.app>
"""

st.sidebar.title("About")
st.sidebar.info(markdown)
logo = "https://i.imgur.com/UbOXYAU.png"
st.sidebar.image(logo)

# Customize page title
st.title("Earth Engine Web App")

st.markdown(
    """
    This multipage app template demonstrates various interactive web apps created using [streamlit](https://streamlit.io) and [geemap](https://geemap.org). It is an open-source project and you are very welcome to contribute to the [GitHub repository](https://github.com/giswqs/geemap-apps).
    """
)
st.balloons()
st.header("Instructions")

markdown = """
1. For the [GitHub repository](https://github.com/giswqs/geemap-apps) or [use it as a template](https://github.com/new?template_name=geemap-apps&template_owner=giswqs) for your own project.
2. Customize the sidebar by changing the sidebar text and logo in each Python files.
3. Find your favorite emoji from https://emojipedia.org.
4. Add a new app to the `pages/` directory with an emoji in the file name, e.g., `1_🚀_Chart.py`.
"""

st.markdown(markdown)

m = geemap.Map()
m.add_basemap("OpenTopoMap")
m.add_basemap('SATELLITE')
m.to_streamlit(height=500)

SA_C1_F1 = ee.Geometry.Polygon([[
    [-122.30873933302412,39.733553025787074],
    [-122.29966059951893,39.733490246690515],
    [-122.29963899613189,39.73739881238475],
    [-122.30867708267466,39.737436562645634],
    [-122.30873933302412,39.733553025787074],
  ]])

m.add_layer(SA_C1_F1, {'color': 'red'}, 'SA_C1_F1')
m.centerObject(SA_C1_F1,14)

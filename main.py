import streamlit as st
from streamlit_option_menu import option_menu
st.sidebar.image('raja.jpeg')
with st.sidebar:
    option = option_menu('Raja Sekhar Thota',['Profile summary','Experience','Education','Projects','Achievements','Contact'])
st.markdown("<h1 style='background-color:#FF4B4B;text-align:center; border-radius:5px;'>My Portfolio</h1>",unsafe_allow_html=True)
if option == 'Profile summary':
    st.markdown('')
    ps1 = "👋 Hello! I'm a highly experienced Python developer with over 6 years of experience in full-stack development using Flask. I'm also proficient in using artificial intelligence and machine learning in my work."
    st.markdown('<p>{}</p>'.format(ps1),unsafe_allow_html=True)
    ps2 = "💻 Currently, I'm the CTO at a blockchain security firm, AuditOne GmbH where I lead the technical direction of the company. I oversee the development of auditor pooling platform, trust layer APIs and the creation of automated audit tools in web3. I'm also responsible for setting the technical architecture of the company."
    st.markdown('<p>{}</p>'.format(ps2), unsafe_allow_html=True)
    st.markdown('<p>🎯 Skills : Python programming, Streamlit, Data science and AIML</p>', unsafe_allow_html=True)
    cols = st.columns(2)
    cols[0].markdown('<h6>Contact : +919010062133</h6>', unsafe_allow_html=True)
    cols[1].markdown('<h6>Email : rajaathota72@gmail.com</h6>', unsafe_allow_html=True)
if option == "Experience":
    st.markdown('')
    st.markdown('<h6>CTO & Cofounder at AuditOne GmbH, (March 2022 - Present)</h6>',unsafe_allow_html=True)
    st.markdown('*Cologne, Germany*')
if option == "Project":
    st.markdown('')
    st.markdown('Diabetes prediction using ML')
    st.markdown('*dates *')
    st.markdown('<p>Description</p>', unsafe_allow_html=True)



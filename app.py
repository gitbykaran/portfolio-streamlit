import streamlit as st

with open("style.css") as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

st.write('''
# Karandeep Singh
##### *Portfolio*''')

st.image('./image.png', width=160)

st.markdown('## Summary', unsafe_allow_html=True)

st.info('''
- As a dedicated Data Scientist, I bring a blend of technical expertise and strong soft skills to the table. Proficient in Python, R, and SQL, I excel in extracting, cleaning, and analyzing complex datasets to derive actionable insights.
- Overall, I am a results-driven professional who is not only capable of delivering impactful data-driven solutions but also of fostering a collaborative and inclusive work environment conducive to innovation and growth.
''')

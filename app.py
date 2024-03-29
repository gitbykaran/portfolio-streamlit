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


def txt(a, b):
    col1, col2 = st.columns([4, 1])
    with col1:
        st.markdown(a)
    with col2:
        st.markdown(b)


st.markdown('''
## Education
''')

txt('**Bachelor of Technology** (Information Technology), *CEC-CGC*, Landran',
    '2021-2025')
st.markdown('''
- GPA: `7.73`
- Coursework in `DSA`,`DBMS`,`ML`,`OOPS`, `BD` and statistical methods essential for data science proficiency.
- Possess a strong foundation and practical skills in *data manipulation*, *analysis*, and *visualization*, poised to contribute effectively to the dynamic field of data science.
- Commitment to Open Source Platforms like *Github*, *Leetcode*, *Hackerank* and *Kaggle*
''', unsafe_allow_html=True)

st.markdown('''
## Work Experience
''')

txt('**Python Training**, ICS Group, *Chandigarh Engineering College*, Landran',
    'July 2023')

st.markdown('''
- Employed Python for machine learning model training, leveraging libraries such as TensorFlow and PyTorch to implement deep learning architectures and optimize model performance
- Utilized NumPy and Pandas for *data preprocessing*, *feature engineering*, and *manipulation tasks*, ensuring the input data is appropriately structured for effective model training.
''', unsafe_allow_html=True)

txt('**Data Science Internship**, Plasmid Innovation, Bengaluru,Karnataka',
    'Feb-March 2024')

st.markdown('''
- Mastered foundational data science concepts like *statistical hypothesis testing*, *feature scaling*, and *dimensionality reduction* in the initial month, establishing a strong theoretical framework for subsequent project work.
- Implemented advanced machine learning algorithms, including ensemble methods like *Random Forests* and *Gradient Boosting*, during the second month's projects, demonstrating expertise in *model selection* and optimization for diverse data sets.            
''')

st.markdown('## Projects')

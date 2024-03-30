import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="My-Portfolio",
    page_icon="💻",
    layout="centered",)

with open("style.css") as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)


st.write('''
# Karandeep Singh
##### *Portfolio*''')


image = Image.open('image.png')
st.image(image, width=150)


st.markdown('## Summary', unsafe_allow_html=True)

st.info('''
- As a dedicated Data Scientist, I bring a blend of technical expertise and strong soft skills to the table. Proficient in Python, R, and SQL, I excel in extracting, cleaning, and analyzing complex datasets to derive actionable insights.
- Overall, I am a results-driven professional who is not only capable of delivering impactful data-driven solutions but also of fostering a collaborative and inclusive work environment conducive to innovation and growth.
''')

st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

st.markdown("""
<nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #16A2CB;">
  <a class="navbar-brand" href="#" target="_blank">Karandeep Singh</a>
  </button>
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item active">
        <a class="nav-link disabled" href="/">Home <span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#education">Education</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#work-experience">Work Experience</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#projects">Projects</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#social-media">Social Media</a>
      </li>
    </ul>
  </div>
</nav>
""", unsafe_allow_html=True)


def txt(a, b):
    col1, col2 = st.columns([4, 1])
    with col1:
        st.markdown(a)
    with col2:
        st.markdown(b)


def txt2(a, b):
    col1, col2 = st.columns([1, 4])
    with col1:
        st.markdown(f'`{a}`')
    with col2:
        st.markdown(b)


def txt3(a, b):
    col1, col2 = st.columns([1, 2])
    with col1:
        st.markdown(a)
    with col2:
        st.markdown(b)


st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)


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
    'March 2024')

st.markdown('''
- Mastered foundational data science concepts like *statistical hypothesis testing*, *feature scaling*, and *dimensionality reduction* in the initial month, establishing a strong theoretical framework for subsequent project work.
- Implemented advanced machine learning algorithms, including ensemble methods like *Random Forests* and *Gradient Boosting*, during the second month's projects, demonstrating expertise in *model selection* and optimization for diverse data sets.            
''')

st.markdown('## Projects')

txt('**End-to-End ML Project**, Student Performance Prediction', 'Jan 2024')

st.markdown('''
- Developed a machine learning model to predict student performance (e.g., grades).
- Utilized tools like Python, `pandas`, `scikit-learn`, and visualization libraries for data manipulation, model training, and evaluation.
- Aimed to provide educators with insights to identify at-risk students and implement early interventions, while acknowledging ethical considerations and data quality importance.                       
''')

txt('**Customer Segmentation ML Project**, Analyzing Customers', 'Feb 2024')

st.markdown('''
- Implemented customer segmentation using unsupervised machine learning techniques (e.g., `k-means clustering`) with Python libraries like `scikit-learn` and `pandas` to analyze customer data.
- Analyzed customer data, including demographics, purchase history, and behavior, to identify distinct customer segments, utilizing data visualization tools like `matplotlib` to understand segment characteristics.
- Aimed to improve marketing strategies by tailoring campaigns and offerings to specific customer segments, fostering increased effectiveness and personalization through targeted marketing efforts            
''')

st.markdown('''
## Skills
''')
txt3('Programming', '`Python`, `R`, `C++`')
txt3('Data processing/wrangling', '`SQL`, `pandas`, `numpy`')
txt3('Data visualization', '`matplotlib`, `seaborn`, `plotly`, `ggplot2`')
txt3('Machine Learning', '`scikit-learn`')
txt3('Deep Learning', '`TensorFlow`')
txt3('Web development', '`Flask`, `HTML`, `CSS`')
txt3('Model deployment', '`streamlit`, `gradio`, `R Shiny`, `Heroku`, `AWS`')


st.markdown('''
## Social Media
''')

txt2('LinkedIn', 'https://www.linkedin.com/in/karandeepsingh3451')
txt2('GitHub', 'https://github.com/gitbykaran')
txt2('Resume', 'https://drive.google.com/file/d/1mB9r_Y4cOQgjTvM4gVm2X5vmEcHNrQdM/view?usp=drive_link')

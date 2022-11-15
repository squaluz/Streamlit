import streamlit as st
import requests
import pycountry

#from newsapi import NewsApiClient
#from api import apiKEY <-- change api to variable and store in a file
#from summarizer import summarize

st.title('News App')

url = f"https://newsapi.org/v2/top-headlines?country=us&category=technology&apiKey=ca8cd2895b1445848a4767c3945d909b"

r = requests.get(url)
r = r.json()
articles = r['articles']
for article in articles:
    st.header(article['title'])
    st.write(article['source']['name'])
    st.write(article['description'])

'''
# Load data
#df_agg = pd.read_csv('Aggregated_Metrics_By_Video.csv').iloc[1:,:]

col1, col2 = st.columns([3,1])
with col1: 
    user = st.text_input('Enter Country Name')
with col2: 
    category = st.radio('Choose a news category',('General','Business','Science','Technology'))
    btn = st.button('Enter')

if btn:
    url = f"https://newsapi.org/v2/top-headlines?country=us&category=technology&apiKey=ca8cd2895b1445848a4767c3945d909b"

    r = requests.get(url)
    r = r.json()
    articles = r['articles']
    for article in articles:
        st.header(article['title'])
        st.write(article['source']['name'])
        st.write(article['description'])
'''
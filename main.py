import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
import streamlit as st
from datetime import datetime
from newsapi import NewsApiClient
from summarizer import summarize

st.write('Hello World')

# Load data
#df_agg = pd.read_csv('Aggregated_Metrics_By_Video.csv').iloc[1:,:]


class Aggregator:
    # Init
    newsapi = NewsApiClient(api_key='ca8cd2895b1445848a4767c3945d909b')

    # /v2/top-headlines
    top_headlines = newsapi.get_top_headlines(q='tesla',
                                            sources='bbc-news,the-verge',
                                            category='business',
                                            language='en',
                                            country='us')

    # /v2/everything
    all_articles = newsapi.get_everything(q='tesla',
                                        sources='bbc-news,the-verge',
                                        domains='bbc.co.uk,techcrunch.com',
                                        from_param='2021-12-01',
                                        to='2021-12-12',
                                        language='en',
                                        sort_by='relevancy',
                                        page=2)

    # /v2/top-headlines/sources
    sources = newsapi.get_sources()
    newsapi.Debug(sources)


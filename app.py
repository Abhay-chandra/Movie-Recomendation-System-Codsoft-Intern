import streamlit as st
import pickle
import pandas as pd
import numpy as np
import requests

def fetch_poster(movie_id):
     url = "https://api.themoviedb.org/3/movie/{}?api_key=c7ec19ffdd3279641fb606d19ceb9bb1&language=en-US".format(movie_id)
     data= requests.get(url)
     data=data.json()
     poster_path = data['poster_path']
     full_path = "https://image.tmdb.org/t/p/w500/"+poster_path
     return full_path

movies = pickle.load(open("movie_recm.pkl", 'rb'))
similarity = pickle.load(open("similarity.pkl", 'rb'))
movies_list=movies['title'].values

st.title("Movie Recommender System")
import streamlit.components.v1 as components

imageCarouselComponent = components.declare_component("image-carousel-component", path="frontend/public")


imageUrls = [
    fetch_poster(1632),
    fetch_poster(299536),
    fetch_poster(17455),
    fetch_poster(2830),
    fetch_poster(429422),
    fetch_poster(9722),
    fetch_poster(13972),
    fetch_poster(240),
    fetch_poster(155),
    fetch_poster(598),
    fetch_poster(914),
    fetch_poster(255709),
    fetch_poster(572154)
   
    ]


imageCarouselComponent(imageUrls=imageUrls, height=200)
movie_df=pickle.load(open("movie_recm.pkl","rb"))
similarity=pickle.load(open("similarity.pkl","rb"))
list_movie=np.array(movie_df["title"])
option = st.selectbox(
"Select Movie ",
(list_movie))

def show_url(movie):
     x=[]
     index = movie_df[movie_df['title'] == movie].index[0]
     distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
     for i in distances[1:6]:

          x.append(movie_df.iloc[i[0]].urls)
     return(x)
def movie_recommend(movie):
     index = movie_df[movie_df['title'] == movie].index[0]
     distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
     l=[]
     for i in distances[1:6]:
          l.append("{}".format(movie_df.iloc[i[0]].title))
     return(l)
if st.button('Recommend Me'):
     st.write('Movies Recomended for you are:')
     df = pd.DataFrame({
          'Movie Recommended': movie_recommend(option),
          'Movie Url': show_url(option)
     })

     st.table(df)


     
     
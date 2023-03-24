
import streamlit as st 
import pickle
import pandas as pd



movies_dict = pickle.load(open('movies_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)



def recommend(movie):
   
    movie_indx = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_indx]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movies = []
    for i in movies_list:
      
        recommended_movies.append(movies.iloc[i[0]].title)
       
    return recommended_movies #, movie_poster_recommend


movies_dict = pickle.load(open('movies_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl','rb'))
st.title('Movie Recommender System ')
selected_movies_name = st.selectbox(
    'Write down or scroll  movies',
    movies['title'].values
)

if st.button('Recommend'):
    recom = recommend(selected_movies_name)
    for i in recom:
        st.write(i)

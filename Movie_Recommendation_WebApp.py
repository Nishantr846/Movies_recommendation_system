# -*- coding: utf-8 -*-
"""
Created on Mon Jan 21 19:14:25 2025

@author: Nishant
"""

import pickle
import difflib
import streamlit as st

# Load the saved model
model_data = pickle.load(open("movie_recommendation_model.sav", 'rb'))
vectorizer = model_data['vectorizer']
similarity = model_data['similarity']
movies_data = model_data['movies_data']

# Function to recommend movies
def recommend_movie(movie_name):
    # Creating the list with all the movie names given in the dataset
    list_of_all_titles = movies_data['title'].tolist()
    
    # Finding the close match for the movie name given by the user
    find_close_match = difflib.get_close_matches(movie_name, list_of_all_titles)
    
    if not find_close_match:
        return ["Movie not found. Please check the spelling and try again."]
    
    close_match = find_close_match[0]
    
    # Finding the index of the movie with title
    index_of_the_movie = movies_data[movies_data.title == close_match]['index'].values[0]
    
    # Getting the list of similar movies
    similarity_score = list(enumerate(similarity[index_of_the_movie]))
    
    # Sorting the movies based on their similarity score
    sorted_similar_movies = sorted(similarity_score, key=lambda x: x[1], reverse=True)
    
    # Generating the top 10 recommended movies
    recommended_movies = []
    for movie in sorted_similar_movies[:10]:
        index = movie[0]
        title_from_index = movies_data[movies_data.index == index]['title'].values[0]
        recommended_movies.append(title_from_index)
    
    return recommended_movies

# Streamlit main function
def main():
    # Title of the web app
    st.title('Movie Recommendation Web App')
    
    # Getting user input
    movie_name = st.text_input("Enter the name of your favorite movie:")
    
    # Recommendations result
    recommendations = []
    
    # Button for movie recommendations
    if st.button('Show Recommendations'):
        recommendations = recommend_movie(movie_name)
    
    if recommendations:
        st.success("Movies recommended for you:")
        for idx, movie in enumerate(recommendations, start=1):
            st.write(f"{idx}. {movie}")

if __name__ == '__main__':
    main()

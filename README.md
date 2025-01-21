# Movie Recommendation System

A machine learning-based recommendation system that suggests movies similar to the user's favorite choice. This project utilizes **TF-IDF vectorization** and **cosine similarity** to identify and recommend movies based on genres, keywords, cast, tagline, and directors.

## Features
- Recommends top 10 similar movies for a given movie title.
- Includes a Python-based CLI version and a web app powered by **Streamlit**.
- Uses a pre-trained model serialized with **Pickle** for efficient recommendations.

## Installation
1. Clone the repository:
- git clone https://github.com/Nishantr846/movie-recommendation-system.git
- cd movie-recommendation-system
2. Install the required Python libraries:
- pip install pickle-mixin
- pip install scikit-learn
- pip install numpy
- pip install pandas
- pip install streamlit
3. Place the movies.csv dataset in the project directory.
4. . Run the Streamlit app:
   - streamlit run Movie_Recommendation_WebApp.py

5. Open the app in your browser (Streamlit will provide a local URL).

## Dataset
The project uses a movie dataset in CSV format with the following fields:

- title: The name of the movie.
- genres: Categories of the movie.
- keywords: Relevant keywords.
- tagline: A short tagline of the movie.
- cast: Cast members.
- director: The movie's director.

  
## Technologies Used
- Python
- Machine Learning: TF-IDF Vectorizer, Cosine Similarity
- Streamlit: Web application framework
- Pickle: Model serialization


# Contributing
Feel free to fork this project, submit issues, or create pull requests. Contributions are always welcome!

## Contact : 
- Nishant Kumar
- nishantr846@gmail.com
- https://www.linkedin.com/in/nishantr846/



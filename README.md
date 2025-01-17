# Movie Recommendation System

This project is a simple **Movie Recommendation System** that suggests movies based on the similarity of features such as genres, keywords, tagline, cast, and director. The recommendation system uses **TF-IDF Vectorization** and **Cosine Similarity** for text-based feature comparison.

---

## Features

- Suggests movies similar to the user's favorite movie.
- Uses **TF-IDF** to convert textual data into feature vectors.
- Employs **Cosine Similarity** to find and rank similar movies.
- Handles missing data by replacing null values with an empty string.

---

## Prerequisites

Before running the program, ensure you have the following installed:

- Python 3.x
- Pandas
- NumPy
- Scikit-learn

Install the required libraries using:

pip install pandas numpy scikit-learn

git clone https://github.com/Nishantr846/movie-recommendation-system.git

cd movie-recommendation-system

python movie_recommendation.py

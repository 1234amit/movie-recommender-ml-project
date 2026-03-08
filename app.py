from flask import Flask, render_template, request
import pickle
import pandas as pd

app = Flask(__name__)

movies = pickle.load(open('movies.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))

def recommend(movie):

    movie_index = movies[movies['original_title'] == movie].index[0]

    distances = similarity[movie_index]

    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []

    for i in movie_list:
        recommended_movies.append(movies.iloc[i[0]].original_title)

    return recommended_movies


@app.route('/')
def home():
    movie_list = movies['original_title'].values
    return render_template("index.html", movies=movie_list)


@app.route('/recommend', methods=['POST'])
def get_recommendations():

    movie = request.form['movie']

    try:
        recommendations = recommend(movie)
        return render_template('index.html', movies=movies['original_title'].values, recommendations=recommendations)

    except:
        return render_template('index.html', movies=movies['original_title'].values, error="Movie not found")


if __name__ == '__main__':
    app.run(debug=True)
# 🎬 Movie Recommendation System (Machine Learning + Flask)

## 📌 Project Overview

This project is a **Movie Recommendation System** built using **Machine Learning, Natural Language Processing (NLP), and Flask**.
The system recommends similar movies based on a movie selected by the user.

It uses **Content-Based Filtering** and **Cosine Similarity** to find movies that are similar in terms of genres, keywords, and descriptions.

---

## 🚀 Features

* Movie recommendation using Machine Learning
* Content-based filtering algorithm
* Cosine similarity calculation
* Web interface using Flask
* Dropdown movie selection
* Error handling for invalid movie names
* Clean UI with HTML & CSS

---

## 🛠 Technologies Used

### Programming

* Python

### Libraries

* Pandas
* NumPy
* Scikit-learn
* Flask

### Machine Learning Techniques

* Natural Language Processing (NLP)
* Count Vectorization
* Cosine Similarity

### Frontend

* HTML
* CSS

---

## 📂 Project Structure

```
movie-recommender/
│
├── app.py
├── movie.ipynb
├── movies.csv
├── requirements.txt
├── README.md
│
├── templates/
│      index.html
│
└── static/
       style.css
```

---

## ⚙️ How the Recommendation System Works

1. Load the movie dataset.
2. Select important features:

   * genres
   * keywords
   * overview
3. Combine these features into one text column.
4. Convert text into numerical vectors using **CountVectorizer**.
5. Calculate similarity using **Cosine Similarity**.
6. When a user selects a movie, the system finds the most similar movies.

---

## ▶️ How to Run the Project

### 1️⃣ Clone the repository

```
git clone https://github.com/1234amit/movie-recommender-ml-project.git
```

### 2️⃣ Install dependencies

```
pip install -r requirements.txt
```

### 3️⃣ Run the Flask application

```
python app.py
```

### 4️⃣ Open the browser

```
http://127.0.0.1:5000
```

---

## 📊 Dataset

The dataset used in this project is from **Kaggle TMDB Movie Dataset**.

Main columns used:

* genres
* keywords
* overview
* original_title

---

## ⚠️ Note

Model files such as:

```
movies.pkl
similarity.pkl
```

are not included in the repository because they exceed GitHub's file size limit.

To generate them, run the **movie.ipynb notebook**.

---

## 🎯 Future Improvements

* Add movie posters using TMDB API
* Add search functionality
* Improve UI like Netflix
* Deploy the application online

---

## 👨‍💻 Author

**Amit**

Machine Learning & Data Science Enthusiast

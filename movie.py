import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Sample Movie Dataset
movies = pd.DataFrame({
    'title': [
        'The Shawshank Redemption', 'The Godfather', 'The Dark Knight',
        'Pulp Fiction', 'Forrest Gump', 'Inception', 'Fight Club',
        'The Matrix', 'Goodfellas', 'The Silence of the Lambs'
    ],
    'description': [
        'Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of common decency.',
        'The aging patriarch of an organized crime dynasty transfers control of his clandestine empire to his reluctant son.',
        'When the menace known as The Joker emerges from his mysterious past, he wreaks havoc and chaos on the people of Gotham.',
        'The lives of two mob hitmen, a boxer, a gangster and his wife, and a pair of diner bandits intertwine in four tales of violence and redemption.',
        'The presidencies of Kennedy and Johnson, the Vietnam War, the Watergate scandal and other history unfold through the perspective of an Alabama man with an IQ of 75.',
        'A thief who steals corporate secrets through the use of dream-sharing technology is given the inverse task of planting an idea into the mind of a CEO.',
        'An insomniac office worker and a devil-may-care soap maker form an underground fight club that evolves into much more.',
        'A computer hacker learns from mysterious rebels about the true nature of his reality and his role in the war against its controllers.',
        'The story of Henry Hill and his life in the mob, covering his relationship with his wife and his partners in crime.',
        'A young F.B.I. cadet must receive the help of an incarcerated and manipulative cannibal killer to catch another serial killer.'
    ]
})

# Build TF-IDF Vectorizer
vectorizer = TfidfVectorizer(stop_words='english')
tfidf_matrix = vectorizer.fit_transform(movies['description'])

# Function to Recommend Movies
def recommend_movies(movie_title, num_recommendations=5):
    if movie_title not in movies['title'].values:
        return []
    movie_idx = movies[movies['title'] == movie_title].index[0]
    cosine_sim = cosine_similarity(tfidf_matrix[movie_idx], tfidf_matrix).flatten()
    similar_indices = cosine_sim.argsort()[-(num_recommendations + 1):-1][::-1]
    return movies['title'].iloc[similar_indices].tolist()

# Custom CSS for Stylish UI with Black Font
st.markdown(
    """
    <style>
    body {
        background: linear-gradient(to right, #ff7e5f, #feb47b);
        font-family: Arial, sans-serif;
    }
    .title {
        font-size: 3em;
        color: #000; /* Changed to black */
        text-align: center;
        padding: 20px;
        text-shadow: 1px 1px 3px rgba(0, 0, 0, 0.2);
    }
    .subtitle {
        font-size: 1.2em;
        color: #000; /* Changed to black */
        text-align: center;
        margin-top: -10px;
    }
    .card {
        background-color: rgba(255, 255, 255, 0.9);
        border-radius: 10px;
        padding: 15px;
        margin: 10px 0;
        box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
    }
    .recommendations {
        font-size: 1.1em;
        font-weight: bold;
        color: #000; /* Changed to black */
    }
    .movie-title {
        color: #000; /* Changed to black */
        font-size: 1.5em;
        font-weight: bold;
    }
    .movie-description {
        color: #000; /* Changed to black */
        font-size: 0.9em;
        margin-top: 5px;
    }
    </style>
    """, unsafe_allow_html=True
)

# Title and Subtitle
st.markdown('<h1 class="title">🎥 Movie Recommendation System</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Discover movies tailored to your preferences</p>', unsafe_allow_html=True)

# Search Bar
search_query = st.text_input("🔍 Search for a movie you like", placeholder="Type a movie name here...")

if search_query:
    # Display matching movie options
    matching_movies = movies[movies['title'].str.contains(search_query, case=False, na=False)]
    
    if not matching_movies.empty:
        selected_movie = st.selectbox("🎞️ Select a movie:", matching_movies['title'])
        
        if selected_movie:
            # Show recommendations
            recommendations = recommend_movies(selected_movie)
            
            if recommendations:
                st.markdown('<h3 class="recommendations">✨ Movies similar to "{}":</h3>'.format(selected_movie), unsafe_allow_html=True)
                for rec in recommendations:
                    with st.container():
                        rec_description = movies[movies['title'] == rec]['description'].values[0]
                        st.markdown(f"""
                            <div class="card">
                                <p class="movie-title">📽️ {rec}</p>
                                <p class="movie-description">{rec_description}</p>
                            </div>
                        """, unsafe_allow_html=True)
            else:
                st.warning("No recommendations found. Try another movie!")
    else:
        st.error("No movies match your search query. Please refine your search!")
else:
    st.info("Start typing in the search box to find a movie.")
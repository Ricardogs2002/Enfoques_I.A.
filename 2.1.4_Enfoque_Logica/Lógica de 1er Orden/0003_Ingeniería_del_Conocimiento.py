import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Cargar los datos de películas y calificaciones
movies = pd.read_csv('movies.csv')
ratings = pd.read_csv('ratings.csv')

# Calcular la calificación promedio de cada película
avg_ratings = ratings.groupby('movieId')['rating'].mean()

# Concatenar el título y los géneros de cada película en una sola cadena de texto
movies['text'] = movies['title'] + ' ' + movies['genres']

# Crear una matriz de características TF-IDF a partir de los textos de las películas
tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(movies['text'])

# Calcular las similitudes entre pares de películas utilizando la similitud coseno
similarity_matrix = cosine_similarity(tfidf_matrix)

# Definir una función para recomendar películas similares a una película dada
def recommend(movie_title):
    # Obtener el ID de la película a partir del título
    movie_id = movies.loc[movies['title'] == movie_title, 'movieId'].iloc[0]
    
    # Obtener las similitudes de la película con todas las demás películas
    sim_scores = list(enumerate(similarity_matrix[movie_id]))
    
    # Ordenar las películas por similitud y obtener las 10 más similares
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:11]
    
    # Obtener los títulos de las películas recomendadas y su calificación promedio
    movie_indices = [i[0] for i in sim_scores]
    movie_titles = movies.iloc[movie_indices]['title']
    movie_ratings = avg_ratings.iloc[movie_indices]
    
    # Crear un DataFrame con las películas recomendadas y su calificación promedio
    recommendations = pd.DataFrame({'title': movie_titles, 'avg_rating': movie_ratings})
    
    # Ordenar las películas por calificación promedio y mostrarlas
    recommendations = recommendations.sort_values('avg_rating', ascending=False)
    print(recommendations)

# Ejemplo de uso: recomendar películas similares a "The Dark Knight"
recommend('The Dark Knight')

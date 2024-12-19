from flask import Flask, jsonify, request

app = Flask(__name__)

# Simulando um banco de dados em memória
movies = []

# Listar todos os filmes
@app.route('/movies', methods=['GET'])
def get_movies():
    return jsonify(movies)

# Adicionar um novo filme
@app.route('/movies', methods=['POST'])
def add_movie():
    data = request.get_json()
    movie = {
        "id": len(movies) + 1,  # ID auto-incremental
        "title": data.get("title"),
        "director": data.get("director"),
        "year": data.get("year")
    }
    movies.append(movie)
    return jsonify({"message": "Filme adicionado com sucesso!", "movie": movie}), 201

# Atualizar um filme existente
@app.route('/movies/<int:movie_id>', methods=['PUT'])
def update_movie(movie_id):
    data = request.get_json()
    for movie in movies:
        if movie["id"] == movie_id:
            movie.update({
                "title": data.get("title", movie["title"]),
                "director": data.get("director", movie["director"]),
                "year": data.get("year", movie["year"])
            })
            return jsonify({"message": "Filme atualizado com sucesso!", "movie": movie})
    return jsonify({"error": "Filme não encontrado"}), 404

# Remover um filme
@app.route('/movies/<int:movie_id>', methods=['DELETE'])
def delete_movie(movie_id):
    global movies
    movies = [movie for movie in movies if movie["id"] != movie_id]
    return jsonify({"message": "Filme removido com sucesso!"})

if __name__ == '__main__':
    app.run(debug=True)

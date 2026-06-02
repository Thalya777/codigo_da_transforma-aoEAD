'''


'''


import sqlite3
from flask import Flask, request, jsonify

app = Flask(__name__)

# Inicializar banco
conn = sqlite3.connect("blog.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    email TEXT NOT NULL
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS posts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT NOT NULL,
    conteudo TEXT NOT NULL,
    autor_id INTEGER,
    FOREIGN KEY (autor_id) REFERENCES usuarios(id)
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS comentarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    conteudo TEXT NOT NULL,
    post_id INTEGER,
    FOREIGN KEY (post_id) REFERENCES posts(id)
)
""")

conn.commit()
conn.close()

# Rotas
@app.route("/usuarios", methods=["POST"])
def cadastrar_usuario():
    data = request.get_json()
    conn = sqlite3.connect("blog.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO usuarios (nome, email) VALUES (?, ?)", (data["nome"], data["email"]))
    conn.commit()
    conn.close()
    return jsonify({"mensagem": "Usuário cadastrado!"})

@app.route("/posts", methods=["POST"])
def criar_post():
    data = request.get_json()
    conn = sqlite3.connect("blog.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO posts (titulo, conteudo, autor_id) VALUES (?, ?, ?)", 
                   (data["titulo"], data["conteudo"], data["autor_id"]))
    conn.commit()
    conn.close()
    return jsonify({"mensagem": "Post criado!"})

@app.route("/comentarios", methods=["POST"])
def adicionar_comentario():
    data = request.get_json()
    conn = sqlite3.connect("blog.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO comentarios (conteudo, post_id) VALUES (?, ?)", 
                   (data["conteudo"], data["post_id"]))
    conn.commit()
    conn.close()
    return jsonify({"mensagem": "Comentário adicionado!"})

@app.route("/posts", methods=["GET"])
def listar_posts():
    conn = sqlite3.connect("blog.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM posts")
    posts = cursor.fetchall()
    conn.close()
    return jsonify(posts)

if __name__ == "__main__":
    app.run(debug=True)
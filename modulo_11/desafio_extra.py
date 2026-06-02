'''



'''



import sqlite3

conn = sqlite3.connect("tarefas.db")
cursor = conn.cursor()

# Criar tabela de tarefas
cursor.execute("""
CREATE TABLE IF NOT EXISTS Tarefas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    descricao TEXT NOT NULL
)
""")

# Funções CRUD para tarefas
def adicionar_tarefa(descricao):
    cursor.execute("INSERT INTO Tarefas (descricao) VALUES (?)", (descricao,))
    conn.commit()

def listar_tarefas():
    cursor.execute("SELECT * FROM Tarefas")
    return cursor.fetchall()

def excluir_tarefa(id_tarefa):
    cursor.execute("DELETE FROM Tarefas WHERE id=?", (id_tarefa,))
    conn.commit()

# Exemplo de uso
adicionar_tarefa("Estudar Python")
adicionar_tarefa("Praticar SQL")

print("Lista de tarefas:", listar_tarefas())

excluir_tarefa(1)
print("Lista após exclusão:", listar_tarefas())

conn.close()
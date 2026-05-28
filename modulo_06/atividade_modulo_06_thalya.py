import json
import csv

# 1. Criar arquivo TXT
with open("informacoes.txt", "w", encoding="utf-8") as txt_file:
    txt_file.write("Copiloto no VS Code\n")
    txt_file.write("Este arquivo contém informações gerais sobre o sistema de armazenamento de dados.\n")
    txt_file.write("Inclui arquivos .txt, .json e .csv para diferentes tipos de dados.\n")

# 2. Criar arquivo JSON
dados_json = {
    "projeto": "Sistema de Armazenamento de Dados",
    "arquivos": ["informacoes.txt", "informacoes.json", "notas.csv"],
    "descricao": "Este sistema armazena informações gerais, dados estruturados e notas de alunos."
}

with open("informacoes.json", "w", encoding="utf-8") as json_file:
    json.dump(dados_json, json_file, indent=4, ensure_ascii=False)

# 3. Sistema de notas em Python
notas_alunos = {
    "Ana": [8.5, 9.0, 7.5],
    "Bruno": [6.0, 7.0, 8.0],
    "Carlos": [9.5, 9.0, 10.0],
    "Daniela": [7.0, 6.5, 8.0]
}

# 4. Criar arquivo CSV
with open("notas.csv", "w", newline="", encoding="utf-8") as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(["Nome", "Nota 1", "Nota 2", "Nota 3"])
    for nome, notas in notas_alunos.items():
        writer.writerow([nome] + notas)

print("Arquivos TXT, JSON e CSV criados com sucesso!")

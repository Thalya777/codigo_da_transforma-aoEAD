'''


'''


import requests

def buscar_filme(titulo):
    API_KEY = "sua_chave_aqui"  # substitua pela sua chave da TMDB
    url_busca = f"https://api.themoviedb.org/3/search/movie?api_key={API_KEY}&query={titulo}&language=pt-BR"

    try:
        resposta = requests.get(url_busca, timeout=5)
        resposta.raise_for_status()
        dados = resposta.json()

        if dados["results"]:
            filme = dados["results"][0]  # pega o primeiro resultado
            titulo_filme = filme["title"]
            sinopse = filme["overview"]

            # Buscar gêneros usando outro endpoint
            url_generos = f"https://api.themoviedb.org/3/genre/movie/list?api_key={API_KEY}&language=pt-BR"
            resposta_generos = requests.get(url_generos, timeout=5)
            resposta_generos.raise_for_status()
            lista_generos = resposta_generos.json()["genres"]

            # Mapear IDs de gênero para nomes
            generos = [g["name"] for g in lista_generos if g["id"] in filme["genre_ids"]]

            print(f"🎬 Título: {titulo_filme}")
            print(f"📖 Sinopse: {sinopse}")
            print(f"🏷️ Gêneros: {', '.join(generos)}")
        else:
            print("Nenhum filme encontrado.")

    except requests.exceptions.HTTPError as e:
        print("Erro HTTP:", e)
    except requests.exceptions.ConnectionError:
        print("Erro de conexão. Verifique sua internet.")
    except requests.exceptions.Timeout:
        print("A requisição demorou demais.")
    except Exception as e:
        print("Erro inesperado:", e)

# Exemplo de uso
buscar_filme("Inception")
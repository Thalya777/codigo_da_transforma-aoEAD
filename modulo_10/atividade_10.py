'''


'''


import requests

def obter_previsao(cidade):
    API_KEY = "sua_chave_aqui"  # substitua pela sua chave da OpenWeatherMap
    url = f"http://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={API_KEY}&units=metric&lang=pt_br"

    try:
        resposta = requests.get(url, timeout=5)
        resposta.raise_for_status()  # lança erro se status != 200
        dados = resposta.json()

        # Filtrando informações relevantes
        temperatura = dados["main"]["temp"]
        condicao = dados["weather"][0]["description"]
        umidade = dados["main"]["humidity"]

        print(f"📍 Cidade: {cidade}")
        print(f"🌡️ Temperatura: {temperatura}°C")
        print(f"☁️ Condição: {condicao}")
        print(f"💧 Umidade: {umidade}%")

    except requests.exceptions.HTTPError as e:
        print("Erro HTTP:", e)
    except requests.exceptions.ConnectionError:
        print("Erro de conexão. Verifique sua internet.")
    except requests.exceptions.Timeout:
        print("A requisição demorou demais.")
    except Exception as e:
        print("Erro inesperado:", e)

# Exemplo de uso
obter_previsao("São Paulo")
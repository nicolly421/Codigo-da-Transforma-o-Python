import requests
url = "API_TMDB"
try:
    r = requests.get(url)
    print(r.json())
except:
    print("Erro API")

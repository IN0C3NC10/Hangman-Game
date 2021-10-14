import json
import requests
def getData():
    response = requests.get("https://api.dicionario-aberto.net/random")
    content = json.loads(response.text)
    data = content['word']
    return data

from Objects.Mod import Mod
import requests

file_types = {
    'Mods' : Mod,
    'Resource Packs' : None
}

# puxar api url
def get_api_url(id, version, modloader):
    api_url = f"https://api.cfwidget.com/{id}?version={version}&loader={modloader}"
    return api_url

# Salva o arquivo .jar no filePath padrão
def get_json(api_url):
    response = requests.get(api_url)
    json = response.json()
    return json

# Verifica se qual é a classe correta e cria o objeto
def create_object_from_json(json):
    file_type = json['type']
    if file_type in file_types:
        file_class = file_types[file_type]
        if file_class is not None: # verifica se não é nulo e cria 
            file = file_class(json)
            return file
    else:
        print('Tipo do arquivo não identificado, verifique o arquivo manualmente')
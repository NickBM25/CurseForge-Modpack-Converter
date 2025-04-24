from Objects.Download import Download
import requests
import os

class Mod:
    id: int
    title: str
    url: str
    download: Download
    
    def __init__(self, j):
        self.id = j['id']
        self.title = j['title']
        self.url = j['urls']['curseforge']
        # Criando o objeto Download com base no conteúdo de 'download' do JSON
        self.download = Download(
            j['id'],
            j['download']['id'],  
            j['download']['name'], 
            j['download']['type'],  
            j['download']['filesize'],
            j['download']['versions'] 
        )

    def __str__(self):
        return f"Mod ID: {self.id}" + "\n" + f"Mod Name: {self.title}" + "\n" + f"Mod Download Query:" + "\n" + f"{self.download}"

    # Baixa o .jar do Mod utilizando o padrão da API do CurseForge
    def download_file(self):
        response = requests.get(self.download.download_url) # Faz o download do arquivo
        if response.status_code == 200: # Verifica se o download foi bem sucedido
            self.save_file(response.content)
        else: 
            print(f"Failed to download the file. Status code: {response.status_code}")

    # Salva o arquivo .jar no file_path padrão
    def save_file(self, downloaded_file):
        os.makedirs('Mods', exist_ok=True) # Verifica se a pasta 'Mods' existe na pasta root do projeto
        file_path = f'Mods/{self.download.file_name}'
        with open(file_path, 'wb') as file: # Salva o arquivo no file_path
            file.write(downloaded_file)
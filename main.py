# from Objects.Mod import Mod # Importa a classe Mod do módulo Mod, no pacote "Download" 
from Utils import JsonUtils
from Utils.MenuUtils import MenuUtils
from Utils.ModpackUtils import ModpackUtils

# # Definições para fazer a requisição à API
MenuUtils.get_desired_version()
MenuUtils.get_desired_modloader()
MenuUtils.get_manifest_path()

manifest = ModpackUtils.read_manifest(MenuUtils.manifest_path)
ModpackUtils.extract_modpack_ids(manifest)

ids_list = ModpackUtils.project_ids_list
for id in ids_list:
    api_url = JsonUtils.get_api_url(id, MenuUtils.version, MenuUtils.modloader)
    # Fazendo requisição do JSON
    json = JsonUtils.get_json(api_url)
    file = JsonUtils.create_object_from_json(json)
    print(file)
    # baixa o arquivo da instancia se nao for nulo 
    if file is not None:
        file.download_file()
    



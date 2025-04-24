import json

class ModpackUtils:
    project_ids_list = []

    #puxa todos os ids de um manifest
    def extract_modpack_ids(manifest):
        modpack_list = manifest['files']
        for file in modpack_list:
            id = file['projectID']
            ModpackUtils.project_ids_list.append(id)
    
    #le o manifest.json
    def read_manifest(manifest_path):
        with open (manifest_path, 'r') as file:
            manifest = json.load(file)
            return manifest



class MenuUtils:
    version = None
    modloader = None
    manifest_path = None

    def get_desired_version():
        print('Para qual versão de Minecraft deseja converter o(s) mod(s)?')
        MenuUtils.version = input()
        

    def get_desired_modloader():
        print('Para qual versão de Mod Loader deseja converter o(s) mod(s)?')
        MenuUtils.modloader = input()

    def get_manifest_path():
        print('Digite o caminho do seu manifest.json:')
        MenuUtils.manifest_path = input()
        
from typing import List

class Download:
    project_id: str
    file_name: str
    status: str
    download_url: str
    file_id: int
    file_size: int
    versions: List[str]
    def __init__(self, project_id, id, name, type, file_size, versions):
        self.project_id = project_id
        self.file_id = id
        self.file_name = name
        self.status = type
        self.file_size = file_size
        self.versions = versions
        self.download_url = f"https://www.curseforge.com/api/v1/mods/{self.project_id}/files/{self.file_id}/download"

    def __str__(self):
        return f"File ID: {self.file_id}" + "\n" + f"File status: {self.status}" + "\n" + f"File Version: {self.versions}"

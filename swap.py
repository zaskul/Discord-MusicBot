import os
from dotenv import load_dotenv

def swap_backend_youtube_dl():
    load_dotenv()
    path = os.path.abspath(os.getenv('pathToBackendYoutubeDl'))
    with open('backend_youtube_dl-fix.txt', 'r+') as file1:
        file1_r = file1.read()
        with open(path, 'r+') as file2:
            file2.seek(0)
            file2.write(file1_r)
            file2.truncate()
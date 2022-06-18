import os
def swap_backend_youtube_dl():
    path = os.path.abspath(".\\Lib\\site-packages\\pafy\\backend_youtube_dl.py")
    with open('backend_youtube_dl-fix.txt', 'r+') as file1:
        file1_r = file1.read()
        with open(path, 'r+') as file2:
            file2.seek(0)
            file2.write(file1_r)
            file2.truncate()
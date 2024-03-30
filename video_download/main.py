from pytube import YouTube
from os import *
from pywebio.input import *
from pywebio.output import *


# pip install pytube pywebio


def video_download():
    while True:
        
        video_link = input("Informe o link do vídeo: ")
        
        if video_link.split("//")[0] == "https:":
            put_text("Fazendo donwload do vídeo ...".title()).style('color: red; font-size: 50px')
            video_url = YouTube(video_link)
            video = video_url.streams.get_highest_resolution()
            path_to_download = r'C:\Users\woqua\Downloads'
            video.download(path_to_download)
            put_text("Vídeo baixado com sucesso...".title()).style('color: blue; font-size: 50px')
            startfile(r'C:\\Users\\woqua\\Downloads')

if __name__ == "__main__":
    video_download()

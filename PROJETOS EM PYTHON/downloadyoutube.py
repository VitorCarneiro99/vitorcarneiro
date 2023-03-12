from pytube import YouTube

#INSIRA A URL DO VÍDEO DO YOUTUBE"
url = "https://www.youtube.com/watch?v=A47y1r0o3NI"

# Cria uma instância da classe YouTube com a URL do vídeo
yt = YouTube(url)

# Exibe informações sobre o vídeo
print(f"Título: {yt.title}")
print(f"Duração: {yt.length} segundos")
print(f"Descrição: {yt.description}")
print(f"Thumbnail URL: {yt.thumbnail_url}")

# Seleciona a melhor resolução disponível para o download
ys = yt.streams.get_highest_resolution()

# Faz o download do vídeo
print("Fazendo download...")
ys.download()
print("Download concluído!")

#LEMBRE-SE "pip install pytube" escreva em seu prompt de comando antes de utilizar este programa
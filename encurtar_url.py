import pyshorteners

# URL que você deseja encurtar
url = "acordo.me/df1lgaTqy"

# Criar um objeto Shortener
s = pyshorteners.Shortener()

# Encurtar a URL
short_url = s.tinyurl.short(url)

# Imprimir a URL encurtada
print("URL Original:", url)
print("URL Encurtada:", short_url)

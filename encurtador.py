import pyshorteners

url = str(input('Digite a URL: '))

link = pyshorteners.Shortener()
short_url = link.tinyurl.short(url)
print(short_url)

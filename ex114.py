import urllib.request
import urllib

try:
    site = urllib.request.urlopen(str(input('Digite o site: ')))
except urllib.error.URLError:
    print('\033[1;31mNão encontrado!')
else:
    print('\033[1;32mSite acessado com sucesso!')
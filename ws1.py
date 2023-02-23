import requests
from bs4 import BeautifulSoup
html_fichero = open("sw.html","r")
html_c= html_fichero.read()
html_fichero.close()
print("Analisis del html")
documento = BeautifulSoup(html_c,'html.parser')
imagen=documento.html.body.li.a.img
print (imagen)
listai=documento.find_all('img')
for i in listai:
    print (i)
print('\n')
print(imagen.parent)
print (documento.body.ul.li.text)
imagenehu=documento.find_all('img',{'id':'ehu'})
print(imagenehu)
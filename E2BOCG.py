#  Covarrubias Gutierrez Brayan Omar
from bs4 import BeautifulSoup as bs
import requests
import os
import sys
try:
    import webbrowser
except ImportError:
    os.system('pip install webbrowser')
    print('Installing webbrowser...')
    print('Ejecuta de nuevo tu script...')
    exit()

print("Este script navega en las páginas de noticas de la UANL")
#  Aqui coloque un while para que los datos se ingresen correctamente.
while True:
    #  Este try verifica que los datos sean int.
    try:
        #  Pedimos dos datos para usarlos como rango, cuando sean
        #  ingresados correctamente nos sacara del ciclo while.
        inicioRango = int(input("Pagina inicial para buscar: "))
        finRango = int(input("Pagina final para buscar: "))
        break
    except ValueError:
        print("\nEl número debe de ser entero positivo.")
dependencia = input("Ingrese las siglas de la Facultad a buscar: ")
#  Este if verifica que finRango sea mas grande que inicioRango.
if inicioRango > finRango:
    inicioRango, finRango = finRango, inicioRango
#  Este for ayuda a recorre r la pagina de noticias de la UANL, y
#  obtiene respuesta de la url y con el if verifica que exista,
#  una vez encontrado el contenido de la pagina se guarda en soup
#  y luego se selecciona cierta parte de soup esta pasa a un for en
#  donde verificamos cada una de los url2 para verificar que exista
#  despues se verifica que el url2 exista y busca que dependencia
#  coincida con algun elemento en el parrafo del contenido de url2,
#  si coincide abre el buscador con la url2 y sale del ciclo.
for i in range(inicioRango, finRango, 1):
    url = "https://www.uanl.mx/noticias/page/"+str(i)
    pagina = requests.get(url)
    if pagina.status_code != 200:
        raise TypeError("Pagina no encontrada")
    else:
        soup = bs(pagina.content, "html.parser")
        info = soup.select("h3 a")
        for etiqueta in info:
            url2 = etiqueta.get("href")
            pagina2 = requests.get(url2)
            if pagina2.status_code == 200:
                soup2 = bs(pagina2.content, "html.parser")
                parrafos = soup2.select("p")
                for elemento in parrafos:
                    if dependencia in elemento.getText():
                        print("Abriendo", url2)
                        webbrowser.open(url2)
                        break

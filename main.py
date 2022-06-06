url = 'bytebank.com/cambio?moedaOrigem=real'

indice_interrogação = url.find('?')

url_base = url[0:indice_interrogação]
print(url_base)




url_parametros = url[20:36]
print(url_parametros)
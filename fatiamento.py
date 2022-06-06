import re


class Extratorurl:

    def __init__(self, url):
        self.url = self.sanitiza_url(url)
        self.valida_url()

    def sanitiza_url(self, url: str) -> str:
        return url.strip()

    def valida_url(self):
        if self.url == '':
            raise ValueError('A url esta vazia')

        padrao_url = re.compile('(http(s)?://)?(www.)?bytebank.com(.br)?/cambio')
        match = padrao_url.match(self.url)

        if not match:
            raise ValueError('A url não é valida')

    def get_url_base(self):
        indice_interrogacao = self.url.find('?')
        url_base = self.url[:indice_interrogacao]

    def get_url_parametro(self):
        indice_interrogacao = self.url.find('?')
        url_parametro = self.url[indice_interrogacao + 1]
        return url_parametro

    def get_valor_parametro(self, parametro):
        indice_parametro = self.get_url_parametro().find(parametro)
        indice_valor = indice_parametro + len(parametro)
        indice_e_comercial = self.get_url_parametro().find('&', indice_valor)
        if indice_e_comercial == -1:
            valor = self.get_url_parametro()[indice_valor:]
        else:
            valor = self.get_url_parametro()[indice_valor:indice_e_comercial]

        return valor


if __name__ == '__main__':
    extrator_url = Extratorurl('bytebank.com/cambio?moedaOrigem=real')
    valor_quantidade = extrator_url.get_valor_parametro('quantidade')
    print(valor_quantidade)

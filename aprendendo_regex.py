import re
endereco = 'Rua das Flores 72, apartamento 1002, Laranjeiras, Rio de janeiro RJ, 23440-120'

padrao = re.compile('[0-9]{5}[-]?[0-9]{3}')
# regex para cep [0-9] indica que vai a de 0 ate 9 {5} repete 5 vezes exemplo 12345
# [-]? ponto de interrogação significa que pode ou não existir tal caracterer no caso [-]
# [0-9] indica que vai de 0 até 9 {3} e se repete 3 vezes exemplo 123

busca = padrao.search(endereco)

if busca:
    cep = busca.group()
    print(cep)
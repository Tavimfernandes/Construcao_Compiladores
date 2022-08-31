def mostra_tabela_simbolos():
    print('Tabela de símbolos - in e ct:')
    ct = 0
    for simbolo in tabela_simbolos:
        print(f"{ct} - {simbolo}")
        ct += 1

def verifica_tabela_simbolos(c):
    if c in tabela_simbolos:
        i2 = tabela_simbolos.index(c)
    else:
        i2 = 0
    return i2

if __name__ == '__main__':
    fluxo_tokens = ''
    posicao = 1
    operador = ('=', '+', '*')
    tabela_simbolos = list()
    tabela_simbolos.append('')
    #fluxo_caracteres = input('Digite uma expressão: ')
    fluxo_caracteres = 'a = a + r' #
    print(f'Entrada (fluxo de caracteres):\n{fluxo_caracteres}')
    for c in fluxo_caracteres:
        if c.isalpha():
            pos_tabela_simbolo = verifica_tabela_simbolos(c) #variavel =  chama def
            if pos_tabela_simbolo > 0:
                fluxo_tokens += f"<id,{pos_tabela_simbolo}" #atualiza
            else:
                fluxo_tokens += f"<id,{posicao}>"
                tabela_simbolos.append(c)
                posicao += 1
        elif c.isdigit():
            fluxo_tokens += "<{}>".format(c)
        elif c in operador:
            fluxo_tokens += "<{}>".format(c)
        elif c.isspace():
            pass
        else:
            fluxo_tokens += '<erro>'
    print(f'Entrada (fluxo de caracteres):\n{fluxo_caracteres}')
    print(f"Saída (fluxo de tokens):\n{fluxo_tokens}")
    mostra_tabela_simbolos()




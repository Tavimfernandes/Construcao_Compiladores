def mostra_tabela_simbolos():
    print('Tabela de símbolos - in e ct:')
    ct = 0
    for simbolo in tabela_simbolos:
        print(f"{ct} - {simbolo}")
        ct += 1


def verifica_tabela_simbolos(c_atual):
    if c_atual in tabela_simbolos:
        i2 = tabela_simbolos.index(c_atual)
    else:
        i2 = 0
    return i2


if __name__ == '__main__':
    fluxo_tokens = ''
    posicao = 1
    operador = ('=', '+', '*')
    tabela_simbolos = list()
    tabela_simbolos.append('')
    fluxo_caracteres = 'a = 323 + b' #Input
    lexema = ''
    tamanho = len(fluxo_caracteres)
    for i in range (0, tamanho):
        c_atual = fluxo_caracteres[i]

        if c_atual.isalpha():
            fluxo_tokens += f"<id,{posicao}>"
            tabela_simbolos.append(c_atual)
            posicao += 1
            pos_tabela_simbolo = verifica_tabela_simbolos(c_atual)

        elif c_atual.isdigit():
            lexema += c_atual
            if i < tamanho - 1:
                c_proximo = fluxo_caracteres[i+1]
            else:
                c_proximo = ' '
            if not c_proximo.isdigit():
                fluxo_tokens += f'<{lexema}>'
                lexema = ""

        elif c_atual in operador:
            fluxo_tokens += "<{}>".format(c_atual)

        elif c_atual.isspace():
            pass

        else:
            fluxo_tokens += f"<id,{posicao}>"
            tabela_simbolos.append(c_atual)
            posicao += 1

print(f'Entrada (fluxo de caracteres):\n{fluxo_caracteres}')
print(f"Saída (fluxo de tokens):\n{fluxo_tokens}")
mostra_tabela_simbolos()

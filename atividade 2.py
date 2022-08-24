from tabulate import tabulate

pri = -1
i = 0
operadores = []
tabela = []
caracteres = ["+", "=", "-"]

s = input("Digite uma expressão: ")
tamanho = len(s)

contador = 1

while i < tamanho:
    lexema = s[i]

    if lexema.isalpha():
        operadores.append("<id, %s>" % contador)
        pri += 1
        tabela.append("{0} {1}".format(contador, s[pri]))
        contador += 1
        i += 1

    elif lexema.isdigit():
        operadores.append("<%s>" % lexema)
        pri += 1
        i += 1

    elif lexema in caracteres:
        operadores.append("<%s>" % lexema)
        pri += 1
        i += 1

    elif lexema == "#":
        break

    elif lexema == " ":
        pri += 1
        i += 1

    else:
        print("<erro>")
        i += 1

print(tabulate(tabela))
print("Fluxo de tokens:",operadores)

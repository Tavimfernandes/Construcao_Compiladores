i = 0
operadores = []

s = input("Digite uma expressão: ")
# Esta variável percorre o tamanho do input
tamanho = len(s)

contador = 1

while i < tamanho:
    lexema = s[i]

    if lexema.isalpha():
        operadores.append("<id, %s>" %contador)
        contador += 1
        i += 1

    elif lexema.isdigit():
        operadores.append("<%s>" %lexema)
        i += 1

    elif lexema == "+" or lexema == "=" or lexema == "+":
        operadores.append("<%s>" %lexema)
        i += 1

    # Se o usuário digitar # o programa vai se encerrar
    elif lexema == "#":
        break

    # Esse elif permite que o usuário deixe um espaço ou não entre os caracteres
    elif lexema == " ":
        i += 1

    # Isso previne que o usuário digite algum caractere indesejado, sendo assim ele mostra que deu erro no caractere para o usuário
    else:
        print("<erro>")
        i += 1

print(operadores)

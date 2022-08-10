i = 1
operadores = []
caracteres = ["+", "=", "*"]

while i >= 1:
    s = input("Digite um lexema (uma tecla qualquer ou # para sair): ")
    lexema = s[0]

    if lexema.isalpha():
        print("<id, %s>" %i)
        operadores.append("<id, %s>" %i)
        print(lexema)
        print("Operadores:", operadores)
        i += 1

    elif lexema.isdigit():
        print("<num, %s>" %i)
        operadores.append("<num, %s>" %i)
        print(lexema)
        print("Operadores:", operadores)
        i += 1

    elif lexema == caracteres[0] or lexema == caracteres[1] or lexema == caracteres[2]:
        operadores.append("<%s>" %lexema)
        print("<%s>" %lexema)
        print("Operadores:", operadores)

    elif lexema == "#":
        print("Operadores:", operadores)
        break

    else:
        print("<erro>")




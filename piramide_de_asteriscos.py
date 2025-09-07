def piramide_asteriscos():
    num = int(input("Ingrese la altura de la pirámide: "))
    
    for i in range(1, num + 1):

        espacios = " " * (num - i)

        asteriscos = "*" * (2 * i - 1)
        print(espacios + asteriscos)


piramide_asteriscos()
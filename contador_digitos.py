def contador_digitos():
    num = int(input("Ingrese un número entero: "))
    contador = 0
    temp = abs(num)
    
    if temp == 0:
        contador = 1
    else:
        while temp > 0:
            contador += 1
            temp //= 10
    
    print(f"El número {num} tiene {contador} dígitos")

contador_digitos()
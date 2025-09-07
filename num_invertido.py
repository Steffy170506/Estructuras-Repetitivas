def numero_invertido():
    num = int(input("Ingrese un número entero: "))
    inv = 0
    temp = abs(numero)
    
    while temp > 0:
        digito = temp % 10
        inv = inv * 10 + digito
        temp //= 10
    
    if num < 0:
        inv = -inv
    
    print(f"Número original: {num}")
    print(f"Número invertido: {inv}")


numero_invertido()
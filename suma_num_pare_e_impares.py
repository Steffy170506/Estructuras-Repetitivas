def suma_pares_impares():
    num = int(input("Ingrese un número n: "))
    suma_pares = 0
    suma_impares = 0
    
    for i in range(1, num + 1):
        if i % 2 == 0:
            suma_pares += i
        else:
            suma_impares += i
    
    print(f"Suma de números pares hasta {num}: {suma_pares}")
    print(f"Suma de números impares hasta {num}: {suma_impares}")


suma_pares_impares()
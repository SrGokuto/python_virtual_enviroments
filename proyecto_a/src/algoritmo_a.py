primer_numero = int(input("Indica el primer número: "))
segundo_numero = int(input("Indica el segundo número: "))
print("La suma es:", primer_numero + segundo_numero)
print("La resta es:", primer_numero - segundo_numero)
print("La multiplicación es:", primer_numero * segundo_numero)
if segundo_numero != 0:
    print("La división es:", primer_numero / segundo_numero)
else:
    print("No se puede dividir entre cero.")
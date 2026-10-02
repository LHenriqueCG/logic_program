pares=0
impares=0

for numero in range(0,7):
 numero=float(input("Escreva um número: "))
 
 if numero % 2 == 0:
    pares+=1
 else:
   impares+=1

print(f"Existe {pares} números pares e {impares} números impares")
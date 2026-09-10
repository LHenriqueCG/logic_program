numero1 = float (input ("Digite o primeiro número:"))
numero2 = float (input ("Digite o segundo número:"))
numero3 = float (input ("Digite o terceiro número:"))

if numero1>numero2 and numero1>numero3:
    print(f"O primeiro número :{numero1} é o maior número entre os três")

elif numero2>numero1 and numero2>numero3:
    print(f"O segundo número:{numero2} é o maior número entre os três")

elif numero3>numero1 and numero3>numero2:
    print(f"O terceiro número:{numero3} é o maior número entre os três")

else:
    print(f"Os três números são iguais: {numero1} , {numero2} , {numero3}")
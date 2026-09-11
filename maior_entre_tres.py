numero1 = float (input ("Digite o primeiro número:"))
numero2 = float (input ("Digite o segundo número:"))
numero3 = float (input ("Digite o terceiro número:"))

if numero1 == numero2 == numero3:
     print(f"Não há maior , os números {numero1} , {numero2} , {numero3} são iguais")
     
elif numero1>numero2 and numero1>numero3:
    print(f"O primeiro número :{numero1} é o maior número entre os três")

elif numero2>numero3:
    print(f"O segundo número:{numero2} é o maior número entre os três")

else:
    print(f"O terceiro número:{numero3} é o maior número entre os três")
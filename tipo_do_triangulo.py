lado1 = float(input("Informe o comprimento do primeiro lado do triângulo -> "))
lado2 = float(input("Informe o comprimento do segundo lado do triângulo -> "))
lado3 = float(input("Informe o comprimento do terceiro lado do triângulo -> "))


if (lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado2 + lado3 > lado1):
   if (lado1 == lado2 == lado3): 
    print ("O triângulo é Equilátero")

   elif (lado1 != lado2 != lado3):
    print ("O triângulo é Escaleno")

   elif(lado1 == lado2 or lado1 == lado3 or lado2 == lado3):
    if (lado1 != lado2 or lado1 != lado3 or lado2 != lado3):
     print ("O triângulo é Isósceles")
else:
     print ("As medidas passadas não são válidas para a criação de um triângulo")


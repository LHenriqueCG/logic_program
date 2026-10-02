salario = 1000
# desconto inicial
desconto = 0
print (f"desconto inicial R${desconto}")

# desconto da passagem 
passagem = 6/100 * salario
desconto = passagem
print (f"desconto de passagem é de: R${desconto}")

# desconto do vr
vr = 2/100 * salario
desconto = desconto + vr
print (f"desconto de VR é de: R${desconto}")

# desconto pano de saude
plano = 10/100 * salario
desconto = desconto + plano
print (f"desconto de plano de saúde é de: R${plano}")
print (f"Seu desconto total é de: R${desconto}")


# salario liquido
liquido = salario - desconto
print  (f"Seu salário líquido é : R${liquido}")
"""
Programa que imprima una tabla que muestre la altura de los primeros 10 rebotes de una pelota de goma

rebota cada cien metros y cada rebote alcanza la altura de 3/5 de la inicial

"""
metros: int = 100

for rebotes in range(10):
    print(f"{metros:.2f}")
    metros = (metros*3) / 5
"""
Caso. Cree una función para precio unitario comparable. Dos paquetes pueden tener tamaños distintos;
no compare solo sus precios totales. Llame para dos paquetes y use los retornos para indicar el más
económico por gramo; si coinciden indique igualdad. Contrato: Precio unitario comparable: recibe
precio total real no negativo en pesos y cantidad real positiva en gramos y devuelve el precio real de un
gramo en pesos.
Fórmula o relación: Precio por gramo = precio total / cantidad de gramos.

"""


def precio_gramo(precio, gramos):
    precio_gramo = precio / gramos
    return precio_gramo



contador = 0

while True:
    precio = int(input("Ingrese el precio "))
    gramos = int(input("Ingrese los gramos "))
    for c in range(0+1,2):
        contador += 1


    if contador == 1:
        precio_por_gramo1 = precio_gramo(precio, gramos)      

        
    else:
        precio_por_gramo2 = precio_gramo(precio, gramos)      
        break
    
if precio_por_gramo1 > precio_por_gramo2:
    print("Precio por gramos: ",precio_por_gramo1," y ",precio_por_gramo2,"pesos ; conviene paquete 2")
    
elif precio_por_gramo1 == precio_por_gramo2:
    print("Precio por gramos: ",precio_por_gramo1," y ",precio_por_gramo2,"pesos ; ambos paquetes son convenientes")

else:
    print("Precio por gramos: ",precio_por_gramo1," y ",precio_por_gramo2,"pesos ; conviene paquete 1")





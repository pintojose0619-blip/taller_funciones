"""
Caso. Cree una función para área de un triángulo por base y altura. La altura es perpendicular a la base.
Use dos llamadas y muestre las dos áreas y su suma, calculada con los retornos. Contrato: Área de un
triángulo por base y altura: recibe base y altura, reales positivos expresados en centímetros y devuelve
el área real en centímetros cuadrados.
Fórmula o relación: Área = base × altura / 2. La división entre 2 obtiene la mitad del rectángulo de
igual base y altura.

"""


def area(base, altura):
    area = base * altura / 2 
    return area


def suma(area1, area2):
    suma = area1 + area2
    return suma
    
     

contador = 0

while True:
    base = int(input("Ingrese la base "))
    altura = int(input("Ingrese la altura "))
    for c in range(0+1,2):
        contador += 1


    if contador == 1:
        area1 = area(base, altura)      

        
    else:
        area2 = area(base, altura)      
        suma_total = suma(area1, area2)
        break
    


print("Areas", area1," y ", area2," cm² "," suma: ", suma_total, " cm² ")




        

            

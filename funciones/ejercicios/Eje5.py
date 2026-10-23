"""
Caso. Cree las funciones necesarias para descuento seguido de impuesto ficticio. El descuento se calcula
sobre la base. El impuesto se calcula sobre el subtotal ya descontado, no sobre la base original. Son
reglas ficticias, no normas tributarias. El escenario pasa el retorno del descuento a la función de
impuesto y muestra subtotal y total. Contratos en orden de parámetros: Subtotal descontado: recibe
base real no negativa en pesos, descuento real de 0 a 100 por ciento y devuelve real no negativo en
pesos. Total con impuesto: recibe subtotal real no negativo en pesos, impuesto real no negativo por
ciento y devuelve real no negativo en pesos.
Fórmula o relación: Subtotal = base × (1 − descuento / 100); total = subtotal × (1 + impuesto / 100).
Cada porcentaje se divide por 100.

"""

def subtotal(base,descuento):
    subtotal = base * (1 - descuento / 100)
    return subtotal

def total(subtotal,impuesto):
    total = subtotal * (1 + impuesto / 100) 
    return total



while True:
    base = float(input("Ingrese el valor de la base "))
    descuento = float(input("Ingrese el descuento "))
    impuesto = float(input("Ingrese el impuesto "))

    if base >= 0 and descuento >= 0 and impuesto >= 0:
        subtotal = subtotal(base,  descuento)
        total = total(subtotal,impuesto)
        break
    else:
        print("por favor dijite solo numeros positivos o iguales a cero")
        continue


print("Subtotal: ",subtotal,"; Total: ",total, " pesos")

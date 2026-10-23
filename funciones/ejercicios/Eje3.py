"""
Caso. Cree las funciones necesarias para tolerancia de una medición. Debe reutilizar una función de
valor absoluto que recibe un real y devuelve su distancia al cero. Los extremos de tolerancia se aceptan.
La función de aceptación utiliza el retorno de valor absoluto. El escenario consulta dos mediciones por
separado. Contratos en orden de parámetros: Valor absoluto: recibe real finito y devuelve real no
negativo. Aceptación: recibe medición y objetivo reales, tolerancia real no negativa y devuelve lógico.
Fórmula o relación: Error = valor absoluto de (medición − objetivo); aceptable cuando error ≤
tolerancia.

"""

def error(medicion,objetivo):
    error = medicion - objetivo
    return error    

def aceptable(aceptable1,aceptable2):
    aceptable = aceptable1 <= aceptable2
    return aceptable
objetivo = float(input("Ingrese el objetivo "))
tolerancia = float(input("Ingrese la tolerancia  "))

contador = 0

while True:
    contador += 1
    medicion = float(input("Ingrese la medicion "))


    
    if contador == 1:
        aceptable_resta = error(medicion, objetivo)
        aceptable1 = aceptable(aceptable_resta,tolerancia)

        
    else:
        aceptable_resta = error(medicion, objetivo) 
        aceptable2 = aceptable(aceptable_resta,tolerancia)     
        break
    
print("Aceptables: ",aceptable1," ; ",aceptable2)

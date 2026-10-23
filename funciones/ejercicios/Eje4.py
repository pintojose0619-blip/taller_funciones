"""
Caso. Cree una función para pago semanal con horas extra. Es un modelo ficticio: las primeras 40 horas
se pagan a la tarifa ordinaria; solo las horas que exceden 40 se pagan a 1,5 veces esa tarifa. Llame para
dos personas y sume los retornos, sin redondearlos antes de sumar. Contrato: Pago semanal con horas
extra: recibe horas semanales reales no negativas y tarifa real no negativa en pesos por hora y devuelve
el pago real semanal en pesos.
Fórmula o relación: Pago = horas × tarifa si horas ≤ 40; si horas > 40, pago = 40 × tarifa + (horas −
40) × tarifa × 1,5.

"""

def pago(horas,tarifa):
    if horas <= 40:
        pago = tarifa * horas
        return pago
    else:
        pago = 40 * tarifa + (horas - 40) * tarifa * 1.5
        return pago

def suma(pago1,pago2):
    suma = pago1 + pago2
    return suma


contador = 0

while True:
    contador += 1
    horas = float(input("Ingrese las horas "))
    tarifa = float(input("Ingrese la tarifa "))

    
    if contador == 1:
        pago1 = pago(horas,  tarifa)


        
    else:
        pago2 = pago(horas,  tarifa)
        suma_t = suma(pago1,pago2)     
        break
    
print("Pagos: ",pago1," y ",pago2, " pesos;total: ",suma_t)

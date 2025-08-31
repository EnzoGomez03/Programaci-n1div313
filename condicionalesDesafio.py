"""
Tarifa base:
Todas las facturas incluyen un cargo fijo de $7000 además del costo por consumo.
El costo por metro cúbico (m³) de agua es de $200/m³.

"""
#INPUT DEL CLIENTE
cantidadMetrosConsu = int(input("Por favor ingrese el consumo de metros que tuvo: "))
tipoCliente = input("Por favor ingrese su tipo de cliente(Residencial, Comercial o Industrial.): ").lower()

#PIDE ENUNCIADO
cargoFijo = 7000
costoMetro = 200 * cantidadMetrosConsu

#VARIABLES 
recargo= "No hay recargo."
bonificacion = "No hay bonificacion"
casoEspecial = ""

match tipoCliente:
    case "residencial":
        if cantidadMetrosConsu < 30:
            costoMetro -= costoMetro * 0.10
            bonificacion = "Bonificacion del 10%"
        elif cantidadMetrosConsu > 80:
            costoMetro += costoMetro * 0.15
            recargo = "Recargo del 15%"
    case "comercial":
        if cantidadMetrosConsu > 300:
            costoMetro -= costoMetro * 0.12
            bonificacion = "Bonificacion del 12%"
        elif cantidadMetrosConsu > 150:
            costoMetro -= costoMetro * 0.08
            bonificacion = "Bonificacion del 8%"
        elif cantidadMetrosConsu < 50:
            costoMetro += costoMetro * 0.05
            recargo = "Recargo del 5%"
    case "industrial":
        if cantidadMetrosConsu > 1000:
            costoMetro -= costoMetro * 0.30
            bonificacion = "Bonificacion del 30%"
        elif cantidadMetrosConsu > 500:
            costoMetro -= costoMetro * 0.20
            bonificacion = "Bonificacion del 20%"
        elif cantidadMetrosConsu < 200:
            costoMetro += costoMetro * 0.10
            recargo = "Recargo del 10%"

if tipoCliente == "residencial" and costoMetro < 35000:
    costoMetro -= costoMetro * 0.05
    casoEspecial = "Se le adiciona un 5% de descuento"


subtotalSinNada = 200 * cantidadMetrosConsu #ta bien
subtotal = costoMetro + cargoFijo
iva = subtotal * 0.21
total = subtotal + iva



print(f"Su subtotal de consumo sin bonificaciones ni recargo es de ${subtotalSinNada}") #Ta bien

print(f"Su subtotal con bonificaciones o recargos es de ${subtotal}")

if casoEspecial:
    print(f" {bonificacion} {casoEspecial}")
else:
    print(f"{bonificacion}")
    
print(f"{recargo}")

print (f"IVA aplicacion sin bonificaciones ni recargo es del ${iva}")

print(f"El monto final a pagar es de ${total} ")
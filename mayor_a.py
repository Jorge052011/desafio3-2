import sys
# definición del diccionario
ventas = {
    "Enero": 15000,
    "Febrero": 22000,
    "Marzo": 12000,
    "Abril": 17000,
    "Mayo": 81000,
    "Junio": 13000,
    "Julio": 21000,
    "Agosto": 41200,
    "septiembre": 25000,
    "Octubre": 21500,
    "Noviembre": 91000,
    "Diciembre": 21000,
}

# ingresamos la variable a comparar en la terminal

umbral = int(sys.argv[1])

# Crea un nuevo diccionario con los valores sobre umbral

ventas_filtradas = {mes:valor_venta for mes, valor_venta in ventas.items() if valor_venta > umbral}

# imprime resultado

print(ventas_filtradas)
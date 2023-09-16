# Solicitar el ingreso de los 4 textos
textos = []
for i in range(4):
    texto = input(f"Ingrese el texto {i + 1}: ")
    textos.append(texto)

# Calcular la suma de todas las longitudes
suma_longitudes = sum(len(texto) for texto in textos)

# Encontrar el texto con la mayor cantidad de caracteres
texto_mas_largo = max(textos, key=len)

# Calcular el promedio de las longitudes
promedio_longitudes = suma_longitudes / 4

# Comparar el promedio con la suma de las longitudes del segundo y cuarto texto
suma_segundo_cuarto = len(textos[1]) + len(textos[3])
resultado_comparacion = None

if promedio_longitudes > suma_segundo_cuarto:
    resultado_comparacion = "mayor"
elif promedio_longitudes < suma_segundo_cuarto:
    resultado_comparacion = "menor"
else:
    resultado_comparacion = "igual"

# Mostrar resultados
print(f"La suma de todas las longitudes es {suma_longitudes} caracteres.")
print(f"El texto con la mayor cantidad de caracteres es: '{texto_mas_largo}'")
print(f"El promedio de las longitudes es {promedio_longitudes} caracteres.")
print(f"El promedio es {resultado_comparacion} que la suma de las longitudes del segundo y cuarto texto.")

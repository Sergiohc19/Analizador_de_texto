# Analizador de texto
texto = input("Ingresa un texto: ")
# Contador de letras elegidas
letras_a_contar = []

texto_a_minusculas = texto.lower()

letras_a_contar.append(input("Indica que letras quieres buscar: ").lower())
letras_a_contar.append(input("Indica que letras quieres buscar: ").lower())
letras_a_contar.append(input("Indica que letras quieres buscar: ").lower())
palabra_a_buscar = input("¿Qué palabra quieres buscar en el texto? ").lower()


print("\n")
print("CANTIDAD DE LETRAS")

contador_de_letras1 = texto_a_minusculas.count(letras_a_contar[0])
contador_de_letras2 = texto_a_minusculas.count(letras_a_contar[1])
contador_de_letras3 = texto_a_minusculas.count(letras_a_contar[2])


print(f"Hemos encontrado la letra {letras_a_contar[0]} repetida '{contador_de_letras1}' veces")
print(f"Hemos encontrado la letra {letras_a_contar[1]} repetida '{contador_de_letras2}' veces")
print(f"Hemos encontrado la letra {letras_a_contar[2]} repetida '{contador_de_letras3}' veces")

# Contador de caracteres totales en el texto
print("\n")
print("CANTIDAD DE PALABRAS TOTALES DEL TEXTO")

contador_de_palabras = len(texto.split())
print(f"El texto contiene '{contador_de_palabras}' palabras")

# Cuál es la primera letra y la última del texto
print("\n")
print("LA PRIMERA LETRA Y LA ÚLTIMA DEL TEXTO")

primera_letra = texto[0]
ultima_letra = texto[-1]
print(f"La primera letra del texto es '{primera_letra}' y la última es '{ultima_letra}'")

# Invertir el texto
print("\nTEXTO INVERTIDO")
texto_invertido = texto[::-1]  # Invertimos el texto usando slicing
print(f"El texto escrito al revés es: '{texto_invertido}'")


# Encontrar la palabra Python en el texto
print("\n")
print("LA PALABRA ENCONTRADA O NO ENCONTRADA")


if palabra_a_buscar in texto_a_minusculas:
    print(f"La palabra '{palabra_a_buscar}' SÍ está en el texto.")
else:
    print(f"La palabra '{palabra_a_buscar}' NO está en el texto.")
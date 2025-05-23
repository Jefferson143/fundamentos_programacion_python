nombre = input("Escribe tu nombre completo porfa: ")

# Split se usa para separar un texto en partes
partes = nombre.split()

n = partes[0]
a = partes[2]

# f se utiliza para unir los textos
correo = f"{n}.{a}@keyinstitute.edu.sv"

print("El correo que se debe asignar al usuario ingresado es:")
print(correo)

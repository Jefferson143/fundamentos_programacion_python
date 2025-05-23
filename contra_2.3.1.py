
password = input("Escribe tu contraseña: ")

tiene_numero = False
tiene_mayuscula = False

for letra in password:
    if letra.isdigit():
        tiene_numero = True
    if letra.isupper():
        tiene_mayuscula = True
        
#Len ayuda a saber cuantos caracteres tiene la cadena de texto
if len(password) >= 8 and tiene_numero and tiene_mayuscula:
    print("Contraseña segura")
else:
    print("Contraseña no segura")

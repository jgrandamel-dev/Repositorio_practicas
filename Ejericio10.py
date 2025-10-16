#La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes. 
#Los ingredientes para cada tipo de pizza aparecen a continuación.

#Ingredientes vegetarianos: Pimiento y tofu.
#Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.

#Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, 
# y en función de su respuesta le muestre un menú con los ingredientes disponibles para que elija. 
# Solo se puede eligir un ingrediente además de la mozzarella y el tomate que están en todas la pizzas. 
# Al final se debe mostrar por pantalla si la pizza elegida es vegetariana o no y todos los ingredientes que lleva.

print("Bienvenido a la pizzería Bella Napoli")
tipo = input("¿Quieres una pizza vegetariana? (s/n): ").lower() 
if tipo == 's':
    print("Ingredientes vegetarianos disponibles: ")
    print("1. Pimiento")
    print("2. Tofu")
    ingrediente = input("Elige un ingrediente (1/2): ")
    if ingrediente == '1':
        ingrediente_elegido = "Pimiento"
    elif ingrediente == '2':
        ingrediente_elegido = "Tofu"
    else:
        ingrediente_elegido = "Ingrediente no válido"
    vegetariana = True
else:
    print("Ingredientes no vegetarianos disponibles: ")
    print("1. Peperoni")
    print("2. Jamón")
    print("3. Salmón")
    ingrediente = input("Elige un ingrediente (1/2/3): ")
    if ingrediente == '1':
        ingrediente_elegido = "Peperoni"
    elif ingrediente == '2':
        ingrediente_elegido = "Jamón"
    elif ingrediente == '3':
        ingrediente_elegido = "Salmón"
    else:
        ingrediente_elegido = "Ingrediente no válido"
    vegetariana = False
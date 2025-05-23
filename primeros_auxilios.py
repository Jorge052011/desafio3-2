print("inicio del proceso de emergencia, responda sólo s para SI y n para No")
respuesta = input("¿Responde a estimulos?(s/n):  ").lower()
if respuesta == 's':
    print("Valorar la necesidad de llevarlo al hospital más cercano")
    print("Fin")
else:
    print("Abrir la vía aérea")
    respuesta = input("¿Respira? (s/n): ").lower
    if respuesta == 's':
        print("Permitirle posición de suficiente ventilación")
        print("Fin")
    else:
        print("Administrar 5 ventilaciones y llamar a ambulancia")

# se inicia bucle para poder definir pasos segun llegada de ambulancia, definiendo en primera instancia que la ambulancia no ha llegado, para poder iniciar la iteración
        ambulancia = 'n'
        while ambulancia != 's':
            signos_vida = input("¿Tiene signos de vida? (s/n): ").lower
            
            if signos_vida == 's':
                print("Reevaluar a la espera de la ambulancia")
                ambulancia = input("¿ Llegó la ambulancia? (s/n): ").lower
                if ambulancia == 's':
                    print("Fin")
                    break
            else:
                print("Administrar compresiones torácicas hasta que llegue la ambulancia")
                ambulancia = input("¿Llegó la ambulancia? (s/n): ").lower
                if ambulancia == 's':
                    print("Fin")
                    break
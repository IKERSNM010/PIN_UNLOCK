import colorama
from colorama import Fore, Back, Style
import pyfiglet

# Inicializar Colorama
colorama.init()

# Establecer el menú
menu_options = ['Comenzar la fuerza bruta']
menu_selection = pyfiglet.show_menu("Menú de opciones", menu_options)

# Comprobar la selección de menú
if menu_selection == 0:
    # Iniciar el bucle de fuerza bruta
    for pin in range(0000, 9999):
        # Aquí va el código para intentar desbloquear el dispositivo con el PIN actual
        print(Fore.GREEN + "Intentando desbloquear con el PIN", pin)

        # Aquí va el código para verificar si el PIN es correcto
        # Si el PIN es correcto, mostrar un mensaje y salir del bucle
        if pin == 1234:
            print(Fore.GREEN + "El PIN es correcto, desbloqueo exitoso!")
            break

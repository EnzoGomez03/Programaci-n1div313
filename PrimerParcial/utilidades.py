import sys, time
import os
import csv
from colorama import init, Fore,Style 
#inicializar colorama
init(autoreset=True)


def mensaje_deteccion_archivo():
    print(Fore.RED +"===" * 20)
    print(Fore.BLACK +"\n ⚠️  Se detecto un archivo con informacion de los alumnos!")
    print(Fore.RED +"===" * 20)
    esperar_limpiar()

def ingrese_opciones_correctas():
    print(Fore.RED +"===" * 20)
    print(Fore.BLACK +"\n ⚠️  Por favor ingrese solo las opciones del menu!\n")
    print(Fore.RED + "===" * 20)
    esperar_limpiar()


def leer_archivo(archivo):
    """
    PROPOSITO: Devuelve una lista de dic, con toda la informacion del archivo
    """
    
    with open(archivo,"r", newline="",encoding="utf-8") as e:
            lector = csv.DictReader(e)
            return list(lector)




def animar_texto(texto, color, delay=0.05):
    """Imprime el texto letra por letra con un pequeño delay."""
    for letra in texto:
        print(color + letra, end="", flush=True)
        time.sleep(delay)
    print()  # salto de línea al final


# --- compatibilidad Windows / Linux ---
if os.name == "nt":  # Windows
    import msvcrt
    def esperar_tecla():
        print("\nPresione cualquier tecla para continuar...")
        msvcrt.getch()
else:  # Linux o Mac
    import termios
    import tty
    def esperar_tecla():
        print("\nPresione cualquier tecla para continuar...")
        tty.setcbreak(sys.stdin)
        sys.stdin.read(1)

def limpiar():
    os.system("cls" if os.name == "nt" else "clear")
    
def esperar_limpiar():
    esperar_tecla()
    limpiar()
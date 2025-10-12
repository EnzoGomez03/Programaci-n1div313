import sys, time
import os
from colorama import init, Fore,Style 
#inicializar colorama
init(autoreset=True)

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
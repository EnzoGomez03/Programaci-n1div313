import sys, time
from colorama import init, Fore,Style 
#inicializar colorama
init(autoreset=True)

def animar_texto(texto, color, delay=0.05):
    """Imprime el texto letra por letra con un pequeño delay."""
    for letra in texto:
        print(color + letra, end="", flush=True)
        time.sleep(delay)
    print()  # salto de línea al final
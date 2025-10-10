import os
import sys
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
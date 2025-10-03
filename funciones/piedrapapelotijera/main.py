import app
from colorama import init,Fore, Style
#inicializar colorama
init(autoreset=True)

print (" " *50 +Fore.CYAN +"GANADOR  "+ app.jugar_piedra_papel_tijera())
import os

def print_banner():
    logo = "01001101 01010010 01111110 01010011 01001000 01000001 01000100 01001111 01010111"
    logo = ''.join(chr(int(x, 2)) for x in logo.split())
    print("\033[96m" + logo + "\033[0m")  # Imprime el logo en color cyan

    print("|=======================================================|")
    print(" | Script by              : #MR~SH4DOW                   |")
    print(" | Version                : Version  2.0                |")
    print(" | Contactame en Telegram : @SH4DOWH4CK |")
    print(" | H4CKING & C4RDING  : @SH4DOWH4CK              |")
    print(" ======================================================== ")

def get_command():
    return input("\033[91m$/MR~SH4DOW@root > \033[0m")  # Prompt de entrada en color rojo brillante

def main():
    while True:
        os.system('clear')  # Limpia la terminal
        print_banner()  # Imprime el banner
        command = get_command()  # Obtiene el comando del usuario
        os.system(command)  # Ejecuta el comando

if __name__ == "__main__":
    main()

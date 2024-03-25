import os

def print_banner():
    logo = "01001101 01010010 01111110 01010011 01001000 01000001 01000100 01001111 01010111"
    logo = ''.join(chr(int(x, 2)) for x in logo.split())
    print("\033[96m" + logo + "\033[0m")  # Imprime el logo en color cyan

    print("| Script by: MR~SHADOW                        |")
    print("| En Telegram como: @SH4DOWH4CK |")
    print("| HACKING & CARDING ©                         |")

def get_command():
    return input("$/MR~SH4DOW@root > ")

def main():
    while True:
        os.system('clear')  # Limpia la terminal
        print_banner()  # Imprime el banner
        command = get_command()  # Obtiene el comando del usuario
        os.system(command)  # Ejecuta el comando

if __name__ == "__main__":
    main()

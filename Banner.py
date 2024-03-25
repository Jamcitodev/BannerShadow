class color:
    morado = '\033[95m'
    blanco = '\033[97m'
    cyan = '\033[96m'
    azul  = '\033[94m'
    verde = '\033[92m'
    amarillo = '\033[93m'
    rojo = '\033[91m'
    fin = '\033[0m'

os.system("pkg install openssh")
os.system("pkg install ruby")
os.system("gem install lolcat")
r= requests.get("https://raw.githubusercontent.com/Fenrir-00/baner-termux/main/version.txt")
r=r.text
print(r)
if r != "version=1.3\n":
 os.system("clear")
 print(f"""{color.rojo}HAY UNA NUEVA VERSION ACTUALIZA EL REPOSITORIO
HAY UNA NUEVA VERSION ACTUALIZA EL REPOSITORIO
HAY UNA NUEVA VERSION ACTUALIZA EL REPOSITORIO
HAY UNA NUEVA VERSION ACTUALIZA EL REPOSITORIO
HAY UNA NUEVA VERSION ACTUALIZA EL REPOSITORIO
HAY UNA NUEVA VERSION ACTUALIZA EL REPOSITORIO
HAY UNA NUEVA VERSION ACTUALIZA EL REPOSITORIO
HAY UNA NUEVA VERSION ACTUALIZA EL REPOSITORIO
HAY UNA NUEVA VERSION ACTUALIZA EL REPOSITORIO
HAY UNA NUEVA VERSION ACTUALIZA EL REPOSITORIO
HAY UNA NUEVA VERSION ACTUALIZA EL REPOSITORIO
HAY UNA NUEVA VERSION ACTUALIZA EL REPOSITORIO
HAY UNA NUEVA VERSION ACTUALIZA EL REPOSITORIO
HAY UNA NUEVA VERSION ACTUALIZA EL REPOSITORIO
HAY UNA NUEVA VERSION ACTUALIZA EL REPOSITORIO
HAY UNA NUEVA VERSION ACTUALIZA EL REPOSITORIO
HAY UNA NUEVA VERSION ACTUALIZA EL REPOSITORIO
HAY UNA NUEVA VERSION ACTUALIZA EL REPOSITORIO
HAY UNA NUEVA VERSION ACTUALIZA EL REPOSITORIO
HAY UNA NUEVA VERSION ACTUALIZA EL REPOSITORIO
HAY UNA NUEVA VERSION ACTUALIZA EL REPOSITORIO""")
 time.sleep(5)

def banner():
 os.system("clear")
 print(f"""{color.cyan}
███████╗███████╗███╗  ██╗██████╗ ██╗██████╗
██╔════ ██╔════╝████╗ ██║██╔══██╗██║██╔══██╗
█████╗  █████╗  ██╔██╗██║██████╔╝██║██████╔╝
██╔══   ██╔══╝  ██║╚████║██╔══██╗██║██╔══██╗
██║     ███████╗██║ ╚███║██║  ██║██║██║  ██║
╚═╝     ╚══════╝╚═╝  ╚══╝╚═╝  ╚═╝╚═╝╚═╝  ╚═╝""")
 print(f"{color.fin}")
def version():
 texto ="""
 |=======================================================|
 | Script by              : #FENRIR-00                   |
 | Version                : Version  1.3                 |
 | Follow me on Github    : https://github.com/Fenrir-00 |
 | Contact me on Telegram : @Ritorito1990                |
 ========================================================= """
 lol_py(texto)
def cabecera():
 os.system("clear")
 print (f"""{color.cyan}
██████╗  █████╗ ███╗  ██╗███████╗██████╗ ████████╗██╗  ██╗
██╔══██╗██╔══██╗████╗ ██║██╔════╝██╔══██╗╚══██╔══╝╚██╗██╔╝
██████╦╝███████║██╔██╗██║█████╗  ██████╔╝   ██║    ╚███╔╝
██╔══██╗██╔══██║██║╚████║██╔══╝  ██╔══██╗   ██║    ██╔██╗
██████╦╝██║  ██║██║ ╚███║███████╗██║  ██║   ██║   ██╔╝╚██╗
╚═════╝ ╚═╝  ╚═╝╚═╝  ╚══╝╚══════╝╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝""")

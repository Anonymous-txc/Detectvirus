# Importation de la bibliothèque colorama
from colorama import Fore, Back, Style, init

# Initialisation de colorama pour réinitialiser automatiquement les couleurs
init(autoreset=True)

#!/usr/bin/env python

# Affichage de la bannière
print(f"""{Fore.BLUE}
──•─────•──────
   𝐃𝐄𝐓𝐄𝐂𝐓 𝐕𝐈𝐑𝐔𝐒                 
──•─────•──────
𝐂𝐑𝐄𝐀𝐓𝐄𝐃 𝐁𝐘 𝐀𝐍𝐎𝐍𝐘𝐌𝐎𝐔𝐒 𝐓𝐗𝐂

   𝐅𝐎𝐑 𝐒𝐂𝐀𝐍𝐍𝐄𝐑 𝐅𝐈𝐂𝐇𝐄𝐑

Telegram : shinobi_txc

Github : https//github.com/Anonymous-txc

     Enjoy your SC""")

def scanner_fichier(fichier):
    # Liste de signatures suspectes (exemples signatures)
    signatures = ["malware", "trojan", "virus", "suspicious_code"]
    
    try:
        with open(fichier, "r", encoding="utf-8") as f:
            contenu = f.read()
            
            for signature in signatures:
                if signature in contenu:
                    print(f"{Fore.RED}Alerte : La traces '{signature}' a été trouvée dans {fichier}.")
                    return
            print(f"{Fore.RED}Le fichier {fichier} semble être propre.")
            
    except FileNotFoundError:
        print(f"{Fore.RED}Erreur : Le fichier {fichier} n'a pas été trouvé.")
        
    except Exception as e:
        print(f"{Fore.RED}Une erreur s'est produite : {e}")

# Demande à l'utilisateur de spécifier un fichier à scanner
ficher = input(f"{Fore.CYAN}entre le chemin du ficher a Verifier bruh:\nEx: /storage/emulated/0/download/nom du ficher qui est dans ce dossier que tu veut detecté ")

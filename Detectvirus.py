#Couleurs ANSI pour Termux
GREEN = "\033[92m"
RED = "\033[91m"
CYAN = "\033[96m"

#!/usr/bin/env python

# Affichage de la bannière
print(f"""{GREEN}
──•─────•──────
𝐃𝐄𝐓𝐄𝐂𝐓 𝐕𝐈𝐑𝐔𝐒                 
──•─────•──────
CREATED BY ANONYMOUS TXC

GITHUB : Anonymous-txc

TELEGRAME : shinobi_txc

""")

def scanner_fichier(fichier):
    # Liste de signatures suspectes (exemples signatures)
    signatures = ["malware", "trojan", "virus", "suspicious_code"]
    
    try:
        with open(fichier, "r", encoding="utf-8") as f:
            contenu = f.read()
            
            for signature in signatures:
                if signature in contenu:
                    print(f"{GREEN}Alerte : La traces '{signature}' a été trouvée dans {fichier}.")
                    return
            print(f"{CYAN}Le fichier {fichier} semble être propre.")
            
    except FileNotFoundError:
        print(f"{RED}Erreur : Le fichier {fichier} n'a pas été trouvé.")
        
    except Exception as e:
        print(f"{RED}Une erreur s'est produite : {e}")

# Demande à l'utilisateur de spécifier un fichier à scanner
ficher = input(f"{CYAN}entre le chemin du ficher a Verifier bruh: \nEx : /storage/emulated/0/download/ensuite le nom de ficher dans ce chemin que tu veux verifier..! : ")

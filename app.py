import os
import shutil

class App :

  def getMenu(self) :
    print("╔══════════════════════════════════════════════════════════╗")
    print("║                        📝 TsaraTask                      ║")
    print("╠══════════════════════════════════════════════════════════╣")
    print("║              [1] Ajouter une tâche                 ➕    ║")
    print("║              [2] Marquer terminée                  ✅    ║")
    print("║              [3] Afficher toutes                   📋    ║")
    print("║              [4] Supprimer une tâche               ❌    ║")
    print("║              [5] A propos                          ℹ️    ║")
    print("║              [6] Quitter                           🚪    ║")
    print("╚══════════════════════════════════════════════════════════╝")


  def getPropos(self) :
    print("╔═══════════════════════════════════════════════════╗")
    print("║                                                   ║")
    print("║              TsaraTask v1.0.0                     ║")
    print("║                                                   ║")
    print("║  Organisez vos tâches simplement et efficacement! ║")
    print("║                                                   ║")
    print("║  TsaraTask est une application CLI qui vous       ║")
    print("║  permet de :                                      ║")
    print("║    - Ajouter de nouvelles tâches                  ║")
    print("║    - Marquer les tâches terminées                 ║")
    print("║    - Consulter toutes vos tâches                  ║")
    print("║    - Supprimer des tâches                         ║")
    print("║                                                   ║")
    print("║  Cette application est conçue pour être simple    ║")
    print("║  et rapide à utiliser, directement dans le        ║")
    print("║  terminal.                                        ║")
    print("║                                                   ║")
    print("║  Développé avec ❤️ par Tojosoa Mahefa             ║")
    print("║                                                   ║")
    print("╚═══════════════════════════════════════════════════╝")
    print("")

  def exit(self) :
    while True :
          exit = input("Revenir au menu taper [ok] [> ")
          if exit == "ok" :
            self.clear_screen()
            break
          else :
            print("❌ Veuillez taper 'ok' pour revenir au menu.")


  def getTitle(self, title):
    width, _ = shutil.get_terminal_size()  # largeur actuelle du terminal
    print("\n" + "★" * width)
    print("★" + title.center(width - 2) + "★")
    print("★" * width + "\n")

  def getMessage(self, title) :
    print("")
    print(title)
    print("")

  def clear_screen(self):
    # Windows
    if os.name == "nt":
        os.system("cls")
    # Linux / Mac
    else:
        os.system("clear")

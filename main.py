from app import App
from task import Task
from Manager import TaskManager
import shutil
from datetime import datetime

def saisir_date_friendly():
    while True:
        date_input = input("Entrez la date d'échéance (AAAA-MM-JJ) [> ")
        time_input = input("Entrez l'heure (HH:MM) [> ")

        try:
            # Construire un objet datetime avec secondes à 00
            date_str = f"{date_input} {time_input}:00"
            date_obj = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")

            # Vérification que la date est dans le futur
            if date_obj < datetime.now():
                print("❌ La date et l'heure doivent être supérieures à maintenant !")
                continue

            return date_obj

        except ValueError:
            print("❌ Format invalide ! Date : AAAA-MM-JJ, Heure : HH:MM")


if __name__ == "__main__" :

  run = True
  app = App()
  manager = TaskManager("tasks.json")
  width, _ = shutil.get_terminal_size()
  welcom = "✨ Bienvenue dans TsaraTask - Ny asa voalamina tsara ✨"
  app.clear_screen()
  print("")
  print("")
  print("████████╗ ███████╗  █████╗  ██████╗   █████╗     ████████╗  █████╗  ███████╗ ██╗  ██╗     █████╗  ██████╗  ██████╗ ")
  print("╚══██╔══╝ ██╔════╝ ██╔══██╗ ██╔══██╗ ██╔══██╗    ╚══██╔══╝ ██╔══██╗ ██╔════╝ ██║ ██╔╝    ██╔══██╗ ██╔══██╗ ██╔══██╗")
  print("   ██║    ███████╗ ███████║ ██████╔╝ ███████║       ██║    ███████║ ███████╗ █████╔╝     ███████║ ██████╔╝ ██████╔╝")
  print("   ██║    ╚════██║ ██╔══██║ ██╔══██╗ ██╔══██║       ██║    ██╔══██║ ╚════██║ ██╔═██╗     ██╔══██║ ██╔═══╝  ██╔═══╝ ")
  print("   ██║    ███████║ ██║  ██║ ██║  ██║ ██║  ██║       ██║    ██║  ██║ ███████║ ██║  ██╗    ██║  ██║ ██║      ██║     ")
  print("   ╚═╝    ╚══════╝ ╚═╝  ╚═╝ ╚═╝  ╚═╝ ╚═╝  ╚═╝       ╚═╝    ╚═╝  ╚═╝ ╚══════╝ ╚═╝  ╚═╝    ╚═╝  ╚═╝ ╚═╝      ╚═╝     ")
  print("")
  print(welcom.center(width))
  print("")


  while run :

    app.getMenu()
    print("")
    choice = input("Votre choix [> ")

    match choice :

      # Ajout de tâche

      case "1" :
        app.clear_screen()
        app.getTitle("AJOUTER UNE TACHE")
        title = input("Nom [> ")
        description = input("Description [> ")
        date_echeance = saisir_date_friendly()
        ok = input("[ créer + ] [oui/non] [> ")
        if ok == "oui" :
          task = Task(title, description, date_echeance)
          manager.add_task(task)
          app.clear_screen()
          app.getMessage("✅ Tâche ajouté avec succès 😉")
        else :
          app.clear_screen()
          app.getMessage("❌ Tâche rejeté 🤨")


      # Marquer une tâche comme terminer

      case "2" :
        app.clear_screen()
        app.getTitle("MARQUER TERMINER")
        manager.list_tasks_not_finish()
        task_mark = int(input("Numéro du tâche à marquer comme terminé [> "))
        mark = manager.mark_completed(task_mark)
        app.clear_screen()
        if mark :
          app.getMessage("✅ Tâche mis à jour")
        else :
          app.getMessage("❌ Ce tâche n'existe pas, ou le tâche est déjà terminé !")
      # Afficher tous les taches

      case "3" :
        app.clear_screen()
        app.getTitle("TOUS LES TACHES")
        manager.list_tasks()
        app.exit()


      # Supprimer une tâche

      case "4" :
        app.clear_screen()
        app.getTitle("SUPPRESSION D'UNE TACHE")
        manager.list_tasks()
        task_del = int(input("Numéro du tâche à supprimer [> "))
        res = manager.remove_task(task_del)
        app.clear_screen()
        if res :
          app.getMessage("✅ Tâche supprimé")
        else :
          app.getMessage("❌ Ce tâche n'existe pas !")


      # A propos de l'application

      case "5" :
        app.clear_screen()
        app.getTitle("À PROPOS DE TSARATASK")
        app.getPropos()
        app.exit()


      # Quitter l'application

      case "6" :
        app.clear_screen()
        app.getMessage("Merci d'avoir utiliser notre App :)")
        run = False


      # Commande inconnue

      case _ :
        app.clear_screen()
        app.getMessage("❌❌❌ Choisir les options sur le menu ❌❌❌")

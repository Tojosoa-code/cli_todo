import json
from task import Task

class TaskManager :

  def __init__(self, filename=None):
    self.tasks = []
    self.filename = filename
    self.load_tasks()

  def add_task(self, task) :
    self.tasks.append(task)
    self.save_task()

  def remove_task(self, index) :
    if 0 <= index < len(self.tasks) :
      del self.tasks[index]
      self.save_task()
      return True
    else :
      return False

  def list_tasks(self) :
    if len(self.tasks) <= 0 :
      return False
    else :
      for i,task in enumerate(self.tasks) :
        print(f"{i} | {task.title} | {task.description} | { "✅" if task.completed else "❌" } | echeance : {task.date_echeance} | créer : {task.created_at}")
      print("")
      print("")
      return True

  def list_tasks_not_finish(self) :
    x = 0
    for i,task in enumerate(self.tasks) :
      if task.completed == False :
        print(f"{i} | {task.title} | {task.description} | { "✅" if task.completed else "❌" } | echeance : {task.date_echeance} | créer : {task.created_at}")
        x += 1
    if x <= 0 :
      return False
    else :
      return True

    print("")
    print("")

  def mark_completed(self, index) :
    if 0 <= index < len(self.tasks) :
      self.tasks[index].mark_completed()
      self.save_task()
      return True
    else :
      return False

  def save_task(self) :
    with open(self.filename, "w") as file:
      json.dump([task.to_dictionnaire() for task in self.tasks], file, indent=4)


  def load_tasks(self):
        try:
            with open(self.filename, "r") as f:
                data = json.load(f)
                self.tasks = [Task.from_dict(d) for d in data]
        except FileNotFoundError:
            self.tasks = []

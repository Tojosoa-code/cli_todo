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
      self.tasks.remove(index)
      self.save_task()
      return True
    else :
      return False

  def list_tasks(self) :
    for i,task in enumerate(self.tasks) :
      print(f"{i} | {task.title} | {task.description} | { "✅" if task.completed else "❌" } | echeance : {task.date_echeance} | créer : {task.created_at}")
    print("")
    print("")

  def list_tasks_not_finish(self) :
    for i,task in enumerate(self.tasks) :
      if task.completed == False :
        print(f"{i} | {task.title} | {task.description} | { "✅" if task.completed else "❌" } | echeance : {task.date_echeance} | créer : {task.created_at}")
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

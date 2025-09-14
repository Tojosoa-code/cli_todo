from datetime import datetime

class Task:

    def __init__(self, title, description="", date_echeance=None, created_at=None, completed=False):
        self.title = title
        self.description = description
        self.date_echeance = date_echeance  # datetime ou None
        self.completed = completed
        # Si created_at est fourni, on le prend, sinon on met maintenant
        self.created_at = created_at if created_at else datetime.now()

    def mark_completed(self):
        self.completed = True

    def to_dictionnaire(self):
        return {
            "title": self.title,
            "description": self.description,
            # si date_echeance existe, on formate, sinon None
            "date_echeance": self.date_echeance.strftime("%Y-%m-%d %H:%M:%S") if self.date_echeance else None,
            "created_at": self.created_at.strftime("%Y-%m-%d %H:%M:%S"),
            "completed": self.completed
        }

    @classmethod
    def from_dict(cls, data):
        # Convertir date_echeance et created_at en datetime
        date_echeance = datetime.strptime(data["date_echeance"], "%Y-%m-%d %H:%M:%S") if data["date_echeance"] else None
        created_at = datetime.strptime(data["created_at"], "%Y-%m-%d %H:%M:%S")
        return cls(
            title=data["title"],
            description=data["description"],
            date_echeance=date_echeance,
            created_at=created_at,
            completed=data["completed"]
        )

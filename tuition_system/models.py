# models.py
class Student:
    def __init__(self,name,grade,joining_date,fees_alloted):
        self.name=name
        self.grade=grade
        self.joining_date=joining_date
        self.fees_alloted=fees_alloted

    def __str__(self):
        return f"Name:{self.name} |Grade:{self.grade} |Joining date:{self.joining_date} | Fees alloted:{self.fees_alloted}"
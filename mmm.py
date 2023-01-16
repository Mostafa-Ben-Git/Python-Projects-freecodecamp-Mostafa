from abc import ABC, abstractmethod
from datetime import datetime


class Employee(ABC):
    def __init__(self, Matricule, Nom, Prenom, D_n):
        self.mat = Matricule
        self.Nom = Nom
        self.prenom = Prenom
        self.date = D_n

    def __str__(self):
        return f"dfsffsdfs"

    @abstractmethod
    def GetSalaire(self):
        pass


class Overier(Employee):
    SMIG = 2500
    assert SMIG < SMIG * 2, f"Doit Pas Depasse {SMIG*2} "

    def __init__(self, Matricule, Nom, Prenom, D_n, date_en):
        Employee.__init__(self, Matricule, Nom, Prenom, D_n)
        self.entre = date_en

    def GetSalaire(self):
        return Overier.SMIG + (datetime.now().year - self.entre) * 100


class Cadr(Employee):
    Slaire_base = 11000

    def __init__(self, Matricule, Nom, Prenom, D_n, indice):
        Employee.__init__(self, Matricule, Nom, Prenom, D_n)
        self.indice = indice

    def GetSalaire(self):
        if self.indice == 4:
            return 20000
        else:
            return Cadr.Slaire_base + (self.indice * 2000)


class Patron(Employee):
    def __init__(self, Matricule, Nom, Prenom, D_n, CA, Perc):
        Employee.__init__(self, Matricule, Nom, Prenom, D_n)
        self.CA = CA
        self.Perc = Perc

    def GetSalaire(self):
        return self.CA * (self.Perc / 100)


cc = Cadr("jj", "mm", "kk", 2002, 1)
print(cc.GetSalaire())

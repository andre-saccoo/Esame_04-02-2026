import networkx as nx
from database.dao import DAO

class Model:
    def __init__(self):
        self.G = nx.DiGraph()
        self.artists = []

    @staticmethod
    def dd():
        return DAO.dropdown()


    def build_graph(self, role: str):
        self.dizionario={} #dizionario finale
        self.lista_artisti=[]
        lista_artisti_per_ruolo=DAO.artisti(role)
        self.dizionario_pesi= DAO.pesi()
        for artista in lista_artisti_per_ruolo:
            artista.opere=self.dizionario_pesi[artista.id]
            self.lista_artisti.append(artista)

        for elemento in self.lista_artisti:
            self.dizionario[elemento.id]=elemento

        lista_collegamenti=DAO.collegamenti(role)

        for elemento in lista_collegamenti:
            peso=abs(int(self.dizionario[elemento[0]].opere)-int(self.dizionario[elemento[1]].opere))
            if elemento [0] in self.dizionario.keys() and elemento [1] in self.dizionario.keys() and elemento[0]!=elemento[1]:
                if int(self.dizionario[elemento[0]].opere)<int(self.dizionario[elemento[1]].opere):
                    self.G.add_edge(self.dizionario[elemento[0]],self.dizionario[ elemento[1]], weight=peso)
                elif int(self.dizionario[elemento[1]].opere)<int(self.dizionario[elemento[1]].opere):
                    self.G.add_edge(self.dizionario[elemento[1]], self.dizionario[elemento[0]], weight=peso)

        print(self.G)

        return self.G

    def classifica(self):
        pass

model=Model()
model.build_graph("Designer")
import flet as ft
from model.Model import Model
class Controller:
    def __init__(self, view, model):
        self._view = view
        self._model = model

    def popola_dd(self):
        lista=self._model.dd()
        self._view.popola_dropdown_ruolo(lista)


    def handle_crea_grafo(self, e):
        self._model.create_grafo(e)

    def handle_classifica(self, e):
        pass

import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handle_grafo(self, e):
        borgo=self._view.dd_borgo.value
        if borgo is None:
            self._view.create_alert("Seleziona un borgo")
            return
        grafo = self._model.creaGrafo(borgo)
        self._view.txt_result.controls.append(ft.Text("Grafo correttamente creato."))
        self._view.txt_result.controls.append(ft.Text(f"Il grafo contiene "
                                                      f"{self._model.getNumNodes()} nodi."))
        self._view.txt_result.controls.append(ft.Text(f"Il grafo contiene "
                                                      f"{self._model.getNumEdges()} archi."))

        self._view.update_page()

    def handle_analisi(self, e):
        lista, peso=self._model.analisi()
        self._view.txt_result.controls.append(ft.Text(f"PESO MEDIO: {peso}"))
        self._view.txt_result.controls.append(ft.Text(f"ARCHI CON PESO MAGGIORE DEL PESO MEDIO: {len(lista)}"))
        for (arco1,arco2,peso) in lista:
            self._view.txt_result.controls.append(ft.Text(f"Da {arco1} a {arco2} con peso {peso}"))

        self._view.update_page()

    def fillDD(self):
        borghi=self._model.borghi
        for borgo in borghi:
            self._view.dd_borgo.options.append(ft.dropdown.Option(
                               text=borgo))
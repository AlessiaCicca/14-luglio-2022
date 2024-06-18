import flet as ft


class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff
        self._page = page
        self._page.title = "Template application using MVC and DAO"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.LIGHT
        # controller (it is not initialized. Must be initialized in the main, after the controller is created)
        self._controller = None
        # graphical elements
        self._title = None
        self.txt_name = None
        self.btn_hello = None
        self.txt_result = None
        self.txt_container = None

    def load_interface(self):
        # title
        self._title = ft.Text("Esame 14/07/2022 NYC-HOTSPOTS", color="blue", size=24)
        self._page.controls.append(self._title)

        #ROW with some controls
        # text field for the name
        self.dd_borgo=ft.Dropdown(label="Borgo(b)")
        self.txt_prob = ft.TextField(
            label="Probabilità(p)",
            width=200,
        )
        self.txt_durata = ft.TextField(
            label="Durata(d)",
            width=200,
        )
        self._controller.fillDD()
        # button for the "hello" reply
        self.btn_grafo = ft.ElevatedButton(text="Crea Grafo", on_click=self._controller.handle_grafo)
        self.btn_analisi = ft.ElevatedButton(text="Analisi Archi", on_click=self._controller.handle_analisi)
        row1 = ft.Row([self.dd_borgo, self.btn_grafo],
                      alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row1)
        row2 = ft.Row([self.txt_prob, self.txt_durata, self.btn_analisi],
                      alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row2)


        # List View where the reply is printed
        self.txt_result = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)
        self._page.controls.append(self.txt_result)
        self._page.update()

    @property
    def controller(self):
        return self._controller

    @controller.setter
    def controller(self, controller):
        self._controller = controller

    def set_controller(self, controller):
        self._controller = controller

    def create_alert(self, message):
        dlg = ft.AlertDialog(title=ft.Text(message))
        self._page.dialog = dlg
        dlg.open = True
        self._page.update()

    def update_page(self):
        self._page.update()

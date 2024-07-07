import flet as ft

class Task(ft.Row):
    def __init__(self, text, task_delete):
        super().__init__()
        self.text_view = ft.Text(text, expand=True)
        self.text_edit = ft.TextField(text, visible=False, expand=True)
        self.task_delete = task_delete
        self.edit_button = ft.IconButton(icon=ft.icons.EDIT, on_click=self.edit)
        self.save_button = ft.IconButton(visible=False, icon=ft.icons.SAVE, on_click=self.save)
        self.delete_button = ft.IconButton(icon=ft.icons.DELETE, on_click=self.delete)
        self.container_icon = self.group_icons()
        self.controls = [
            ft.Checkbox(),
            self.text_view,
            self.text_edit,
            self.container_icon
        ]

    def group_icons(self):
        return ft.Container(
            content=ft.Row(
                controls=[
                    self.edit_button,
                    self.delete_button,
                    self.save_button
                ],
                alignment=ft.MainAxisAlignment.END
            ),
            expand=True,
        )

    def edit(self, e):
        self.edit_button.visible = False
        self.save_button.visible = True
        self.text_view.visible = False
        self.text_edit.visible = True
        self.delete_button.visible = False
        self.update()

    def delete(self, e):
        self.delete_button.visible = False
        self.task_delete(self)
    
    def save(self, e):
        self.edit_button.visible = True
        self.delete_button.visible = True
        self.save_button.visible = False
        self.text_view.visible = True
        self.text_edit.visible = False
        self.text_view.value = self.text_edit.value
        self.update()

class ToDoApp(ft.Column):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page
        self.header = self.create_header()
        self.tasks = ft.Column(scroll=ft.ScrollMode.AUTO, expand=True) # TODO expand add
        self.container_task = ft.Container(height=300) # TODO width=500
        self.list_task = self.create_list_task()
        self.icon_button = self.create_icon_button()
        self.alignment = ft.MainAxisAlignment.SPACE_AROUND
        
        self.container_task.content = self.tasks
        self.controls.append(self.header)
        self.controls.append(self.list_task)
        self.controls.append(self.icon_button)

        self.check_width()

    def create_task(self, e): # TODO muda o nome da função, pois ela cria um campo para add um tarefa.
        field_name_task = ft.TextField(on_submit=self.add_task)
        if len(self.tasks.controls) == 0:
            self.tasks.controls.append(field_name_task)
        elif len(self.tasks.controls) == 1:
            if type(self.tasks.controls[-1]) != type(field_name_task):
                self.tasks.controls.append(field_name_task)
        else:
            if type(self.tasks.controls[-1]) != type(field_name_task):
                self.tasks.controls.append(field_name_task)
   
        self.update()

    def create_header(self):
        header = ft.Row(
                controls=[
                    ft.Text('APP Mobile', size=32),
                    ft.CircleAvatar(ft.Text('Dg'))
                ],
                alignment=ft.MainAxisAlignment.SPACE_EVENLY)
        
        return header

    def create_list_task(self):
        return ft.Row(
            [
                self.container_task
            ],
            alignment=ft.MainAxisAlignment.CENTER
        )

    def create_icon_button(self):
        return ft.Row(
            controls=[
                ft.IconButton(
                    icon=ft.icons.ADD, 
                    icon_size=40, 
                    on_click=self.create_task
                ),
            ],
            alignment = ft.MainAxisAlignment.CENTER
        )

    def add_task(self, e):
        task = Task(e.data, self.task_delete)
        if self.check_task(e.data):
            self.tasks.controls.pop()
            self.tasks.controls.append(task)
            
        self.update()

    def task_delete(self, task):
        self.tasks.controls.remove(task)
        self.update()

    def check_task(self, task: str) -> bool:
        if not task:
            return False
        elif task.isspace():
            return False
        
        return True

    def check_width(self):
        if self.page.width > 600:
            self.container_task.width = 500
        else:
            self.container_task.expand = True


class Home(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page

    def build(self):
        return ToDoApp(page=self.page)
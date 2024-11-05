import flet as ft
from database import cars


def main(page: ft.Page):

    # Invocada ao clicar em `mostrar todos`
    def check_item_clicked(e):
        e.control.checked = not e.control.checked
        page.update()

    # Invodaca ao clicar em `Descricao`
    def show_car_description(e):
        car = next((car for car in cars if car['id'] == e.control.parent.key), None)
        dlg = ft.AlertDialog(
            title=ft.Text(car['descricao']),
            actions=[
                ft.TextButton('Fechar', on_click=lambda e: page.close(dlg))
            ]
        )
        page.open(dlg)

    # Invocada ao clicar em `Deletar` no menu de cada carro
    def delete_car(e):
        e.control.parent.parent.visible = False
        page.update()

    # Titulo na barra da janela
    page.title = "Carros"
    # Tamanho da janela
    page.window.height = 800
    page.window.width = 400

    # Barra superior
    app_bar = ft.AppBar(
        # ícone
        leading=ft.Icon(ft.icons.DIRECTIONS_CAR_FILLED),
        # distância da lateral esquerda
        leading_width=40,
        # Título na Barra
        title=ft.Text('Carros'),
        # Centralização do título
        center_title=True,
        bgcolor=ft.colors.SURFACE_VARIANT,
        actions=[
            ft.IconButton(
                ft.icons.NOTIFICATIONS,
            ),
            ft.PopupMenuButton(
                items=[
                    ft.PopupMenuItem(
                        icon=ft.icons.PERSON,
                        text='Perfil',
                    ),
                    ft.PopupMenuItem(
                        icon=ft.icons.SETTINGS,
                        text='Configuração',
                    ),
                    ft.PopupMenuItem(),
                    ft.PopupMenuItem(
                        text='Mostrar Todos',
                        checked=False,
                        on_click=check_item_clicked,
                    )
                ],
            ),
        ],
    )
    # Cria coluna única que expande ocupando todo o espaço disponível
    cars_list = ft.Column(
        scroll=ft.ScrollMode.ALWAYS,
        expand=True,
    )

    # Carrega os carros do database.py
    for car in cars:
        car_component = ft.ListTile(
            leading=ft.Image(
                src=car["foto"],
                fit=ft.ImageFit.COVER,
                repeat=ft.ImageRepeat.NO_REPEAT,
                height=100,
                width=100,
                border_radius=5,
            ),
            title=ft.Text(f'{car["modelo"]} - {car["marca"]}'),
            subtitle=ft.Text(car['ano']),
            trailing=ft.PopupMenuButton(
                key=car['id'],
                icon=ft.icons.MORE_VERT,
                items=[
                    ft.PopupMenuItem(
                        icon=ft.icons.REMOVE_RED_EYE_SHARP,
                        text='Ver descrição',
                        on_click=show_car_description,
                    ),
                    ft.PopupMenuItem(
                        icon=ft.icons.DELETE,
                        text='Deletar',
                        on_click=delete_car,
                    ),
                ],
            ),
        )
        cars_list.controls.append(car_component)

    # Barra de navegação inferior
    nav_bar = ft.NavigationBar(
        destinations=[
            ft.NavigationBarDestination(
                icon=ft.icons.DIRECTIONS_CAR_FILLED_OUTLINED,
                label='Usados',
            ),
            ft.NavigationBarDestination(
                icon=ft.icons.CAR_RENTAL,
                label='Novos'
            ),
            ft.NavigationBarDestination(
                icon=ft.icons.ELECTRIC_CAR_OUTLINED,
                label='Elétricos',
            ),
        ],
    )

    page.add(
        app_bar,
        cars_list,
        nav_bar,
    )


ft.app(main)

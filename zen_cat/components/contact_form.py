"""
Модуль, содержащий компонент формы обратной связи для приложения Zen-кот.

Форма содержит поля для имени, email и сообщения, а также кнопку отправки.
После отправки формы показывается сообщение с благодарностью и меняется изображение кота.
"""

import flet as ft
from utils.localization import Localization


class ContactForm(ft.UserControl):
    """
    Компонент формы обратной связи.
    
    Атрибуты:
        localization (Localization): Объект локализации
        theme (dict): Словарь с настройками темы
    """
    
    def __init__(self, localization: Localization, theme: dict):
        """
        Инициализирует компонент формы обратной связи.
        
        Args:
            localization (Localization): Объект локализации
            theme (dict): Словарь с настройками темы
        """
        super().__init__()
        self.localization = localization
        self.theme = theme
        
        # Элементы формы
        self.title = ft.Text()
        self.name_field = ft.TextField()
        self.email_field = ft.TextField()
        self.message_field = ft.TextField()
        self.submit_button = ft.ElevatedButton()
        
        # Состояние формы
        self.is_submitted = False
        self.success_message = ft.Text()
        
        # Изображение кота (меняется после отправки)
        self.cat_normal = ft.Text("😸", size=60, text_align=ft.TextAlign.CENTER)
        self.cat_happy = ft.Text("😻", size=60, text_align=ft.TextAlign.CENTER)
        self.cat_container = ft.Container()
    
    def build(self):
        """
        Строит компонент формы обратной связи.
        
        Returns:
            ft.Container: Контейнер с формой обратной связи
        """
        # Заголовок блока
        self.title = ft.Text(
            value=self.localization.get("contact_title"),
            size=self.theme["font_sizes"]["lg"],
            weight=ft.FontWeight.BOLD,
            color=self.theme["colors"]["text"],
            text_align=ft.TextAlign.CENTER
        )
        
        # Поле имени
        self.name_field = ft.TextField(
            label=self.localization.get("name_label"),
            hint_text=self.localization.get("name_placeholder"),
            border_color=self.theme["colors"]["text_light"],
            focused_border_color=self.theme["colors"]["primary"],
            text_size=self.theme["font_sizes"]["sm"]
        )
        
        # Поле email
        self.email_field = ft.TextField(
            label=self.localization.get("email_label"),
            hint_text=self.localization.get("email_placeholder"),
            border_color=self.theme["colors"]["text_light"],
            focused_border_color=self.theme["colors"]["primary"],
            text_size=self.theme["font_sizes"]["sm"]
        )
        
        # Поле сообщения
        self.message_field = ft.TextField(
            label=self.localization.get("message_label"),
            hint_text=self.localization.get("message_placeholder"),
            border_color=self.theme["colors"]["text_light"],
            focused_border_color=self.theme["colors"]["primary"],
            multiline=True,
            min_lines=3,
            max_lines=5,
            text_size=self.theme["font_sizes"]["sm"]
        )
        
        # Кнопка отправки
        self.submit_button = ft.ElevatedButton(
            text=self.localization.get("submit_button"),
            on_click=self._submit_form,
            style=ft.ButtonStyle(
                bgcolor={
                    ft.MaterialState.DEFAULT: self.theme["colors"]["primary"],
                    ft.MaterialState.HOVERED: "#26bfad",  # Чуть темнее при наведении
                },
                color={
                    ft.MaterialState.DEFAULT: self.theme["colors"]["white"],
                },
                shape=ft.RoundedRectangleBorder(radius=8),
                animation_duration=300,
            ),
            height=48
        )
        
        # Сообщение об успешной отправке
        self.success_message = ft.Text(
            value=self.localization.get("form_success"),
            size=self.theme["font_sizes"]["md"],
            color=self.theme["colors"]["primary"],
            weight=ft.FontWeight.BOLD,
            text_align=ft.TextAlign.CENTER,
            visible=False
        )
        
        # Контейнер с изображением кота
        self.cat_container = ft.Container(
            content=self.cat_normal,
            alignment=ft.alignment.center,
            margin=ft.margin.only(bottom=self.theme["spacing"]["md"])
        )
        
        # Форма
        form = ft.Column(
            [
                self.cat_container,
                self.name_field,
                ft.Container(height=self.theme["spacing"]["sm"]),  # Отступ
                self.email_field,
                ft.Container(height=self.theme["spacing"]["sm"]),  # Отступ
                self.message_field,
                ft.Container(height=self.theme["spacing"]["md"]),  # Отступ
                ft.Container(
                    content=self.submit_button,
                    alignment=ft.alignment.center
                ),
                ft.Container(height=self.theme["spacing"]["sm"]),  # Отступ
                ft.Container(
                    content=self.success_message,
                    alignment=ft.alignment.center
                )
            ],
            spacing=0,
            width=500  # Ограничиваем ширину формы
        )
        
        # Общий контейнер
        return ft.Container(
            content=ft.Column(
                [
                    self.title,
                    ft.Container(height=self.theme["spacing"]["md"]),  # Отступ
                    form
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=0
            ),
            margin=ft.margin.only(bottom=self.theme["spacing"]["xl"]),
            padding=ft.padding.all(self.theme["spacing"]["md"]),
            alignment=ft.alignment.center
        )
    
    def _submit_form(self, e):
        """
        Обрабатывает отправку формы.
        
        Args:
            e: Событие нажатия кнопки
        """
        # Валидация полей (можно расширить в будущем)
        if not self.name_field.value or not self.email_field.value:
            return
        
        # Выводим данные формы в консоль (имитация отправки)
        print(f"Form submitted:")
        print(f"Name: {self.name_field.value}")
        print(f"Email: {self.email_field.value}")
        print(f"Message: {self.message_field.value}")
        
        # Меняем состояние формы
        self.is_submitted = True
        self.success_message.visible = True
        
        # Меняем изображение кота
        self.cat_container.content = self.cat_happy
        
        # Очищаем поля
        self.name_field.value = ""
        self.email_field.value = ""
        self.message_field.value = ""
        
        # Обновляем компонент
        self.update()
        
        # Через 5 секунд возвращаем кота в нормальное состояние
        self.page.add_delayed_action(5, self._reset_cat)
    
    def _reset_cat(self):
        """
        Возвращает изображение кота в нормальное состояние.
        """
        if not self.is_submitted:
            return
            
        self.cat_container.content = self.cat_normal
        self.success_message.visible = False
        self.is_submitted = False
        self.update()
    
    def update_texts(self):
        """
        Обновляет тексты компонента в соответствии с текущим языком.
        """
        self.title.value = self.localization.get("contact_title")
        self.name_field.label = self.localization.get("name_label")
        self.name_field.hint_text = self.localization.get("name_placeholder")
        self.email_field.label = self.localization.get("email_label")
        self.email_field.hint_text = self.localization.get("email_placeholder")
        self.message_field.label = self.localization.get("message_label")
        self.message_field.hint_text = self.localization.get("message_placeholder")
        self.submit_button.text = self.localization.get("submit_button")
        self.success_message.value = self.localization.get("form_success")
        self.update() 
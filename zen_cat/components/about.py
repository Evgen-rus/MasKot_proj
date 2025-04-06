"""
Модуль, содержащий компонент блока "О нас" для приложения Zen-кот.

Этот компонент отображает информацию о команде и иллюстрацию кота.
"""

import flet as ft
from utils.localization import Localization


class About(ft.UserControl):
    """
    Компонент блока "О нас" с информацией и изображением кота.
    
    Атрибуты:
        localization (Localization): Объект локализации
        theme (dict): Словарь с настройками темы
    """
    
    def __init__(self, localization: Localization, theme: dict):
        """
        Инициализирует компонент блока "О нас".
        
        Args:
            localization (Localization): Объект локализации
            theme (dict): Словарь с настройками темы
        """
        super().__init__()
        self.localization = localization
        self.theme = theme
        
        # Элементы компонента
        self.title = ft.Text()
        self.description = ft.Text()
    
    def build(self):
        """
        Строит компонент блока "О нас".
        
        Returns:
            ft.Container: Контейнер с блоком "О нас"
        """
        # Заголовок блока
        self.title = ft.Text(
            value=self.localization.get("about_title"),
            size=self.theme["font_sizes"]["lg"],
            weight=ft.FontWeight.BOLD,
            color=self.theme["colors"]["text"],
            text_align=ft.TextAlign.LEFT
        )
        
        # Описание
        self.description = ft.Text(
            value=self.localization.get("about_text"),
            size=self.theme["font_sizes"]["sm"],
            color=self.theme["colors"]["text_light"],
            text_align=ft.TextAlign.LEFT
        )
        
        # Изображение кота (временно заменено эмодзи в другой позе)
        cat_image = ft.Text(
            "🧘‍♂️😸",  # Кот в позе медитации
            size=100,
            text_align=ft.TextAlign.CENTER
        )
        
        # Контейнер с текстом слева и изображением справа
        return ft.Container(
            content=ft.Column(
                [
                    # Создаем строку для заголовка
                    ft.Container(
                        content=self.title,
                        alignment=ft.alignment.center_left
                    ),
                    ft.Container(height=self.theme["spacing"]["md"]),  # Отступ
                    
                    # Создаем адаптивный контейнер для основного контента
                    self._create_responsive_content(self.description, cat_image)
                ],
                spacing=0,
            ),
            margin=ft.margin.only(bottom=self.theme["spacing"]["xl"]),
            padding=ft.padding.all(self.theme["spacing"]["md"]),
            width=800
        )
    
    def _create_responsive_content(self, description, cat_image):
        """
        Создает адаптивный контейнер для основного контента.
        На десктопах - описание слева, кот справа.
        На мобильных - описание сверху, кот снизу.
        
        Args:
            description (ft.Text): Текст описания
            cat_image (ft.Text): Изображение кота
            
        Returns:
            ft.Container: Адаптивный контейнер с контентом
        """
        # Создаем контейнер с текстом
        text_container = ft.Container(
            content=description,
            padding=ft.padding.only(right=self.theme["spacing"]["md"]),
            expand=True
        )
        
        # Создаем контейнер с изображением
        image_container = ft.Container(
            content=cat_image,
            alignment=ft.alignment.center,
            width=150,
            height=150,
            bgcolor=self.theme["colors"]["white"],
            border_radius=75,  # Круглый контейнер
            padding=self.theme["spacing"]["md"],
        )
        
        # Создаем адаптивный контейнер
        # Примечание: в мобильной версии контент будет отображаться в колонке,
        # в десктопной - в строке
        return ft.ResponsiveRow(
            [
                ft.Column(
                    [text_container],
                    col={"xs": 12, "sm": 12, "md": 8, "lg": 8, "xl": 8}
                ),
                ft.Column(
                    [image_container],
                    col={"xs": 12, "sm": 12, "md": 4, "lg": 4, "xl": 4},
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER
                )
            ]
        )
    
    def update_texts(self):
        """
        Обновляет тексты компонента в соответствии с текущим языком.
        """
        self.title.value = self.localization.get("about_title")
        self.description.value = self.localization.get("about_text")
        self.update() 
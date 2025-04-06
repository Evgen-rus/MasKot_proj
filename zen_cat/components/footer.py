"""
Модуль, содержащий компонент футера для приложения Zen-кот.

Футер содержит копирайт и является минималистичным, ненавязчивым элементом дизайна.
"""

import flet as ft
from zen_cat.utils.localization import Localization


class Footer:
    """
    Компонент футера с копирайтом.
    
    Атрибуты:
        localization (Localization): Объект локализации
        theme (dict): Словарь с настройками темы
    """
    
    def __init__(self, localization: Localization, theme: dict):
        """
        Инициализирует компонент футера.
        
        Args:
            localization (Localization): Объект локализации
            theme (dict): Словарь с настройками темы
        """
        self.localization = localization
        self.theme = theme
        
        # Копирайт
        self.copyright = ft.Text()
        
        # Создаем контейнер
        self.container = self.build()
    
    def build(self):
        """
        Строит компонент футера.
        
        Returns:
            ft.Container: Контейнер с футером
        """
        # Создаем текст копирайта
        self.copyright = ft.Text(
            value=self.localization.get("copyright"),
            size=self.theme["font_sizes"]["xs"],
            color=self.theme["colors"]["text_light"],
            text_align=ft.TextAlign.CENTER
        )
        
        # Создаем разделительную линию
        divider = ft.Divider(
            color=self.theme["colors"]["text_light"],
            height=1,
            thickness=1
        )
        
        # Создаем контейнер с футером
        return ft.Container(
            content=ft.Column(
                [
                    divider,
                    ft.Container(height=self.theme["spacing"]["md"]),  # Отступ
                    self.copyright,
                    ft.Container(height=self.theme["spacing"]["md"])   # Отступ
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=0
            ),
            padding=ft.padding.only(top=self.theme["spacing"]["md"])
        )
    
    def update_texts(self):
        """
        Обновляет тексты компонента в соответствии с текущим языком.
        """
        self.copyright.value = self.localization.get("copyright") 
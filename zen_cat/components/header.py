"""
Модуль, содержащий компонент шапки (Header) для приложения Zen-кот.

Шапка включает в себя логотип и переключатель языка.
"""

import flet as ft
from zen_cat.utils.localization import Localization


class Header(ft.UserControl):
    """
    Компонент шапки сайта, содержащий логотип и переключатель языка.
    
    Атрибуты:
        localization (Localization): Объект локализации
        on_language_change (callable): Функция обратного вызова при изменении языка
    """
    
    def __init__(self, localization: Localization, on_language_change):
        """
        Инициализирует компонент шапки.
        
        Args:
            localization (Localization): Объект локализации
            on_language_change (callable): Функция обратного вызова при изменении языка
        """
        super().__init__()
        self.localization = localization
        self.on_language_change = on_language_change
        
        # Элементы компонента
        self.logo_text = ft.Text()
        self.language_button = ft.TextButton()
    
    def build(self):
        """
        Строит компонент шапки.
        
        Returns:
            ft.Container: Контейнер с компонентом шапки
        """
        # Обновляем тексты перед построением
        self._update_texts()
        
        # Создаем логотип в виде текста с эмодзи кота
        self.logo_text = ft.Text(
            "😺 Zen-кот",
            size=24,
            weight=ft.FontWeight.BOLD,
            color="#333333"
        )
        
        # Создаем кнопку переключения языка
        self.language_button = ft.TextButton(
            text=self.localization.get("language_switch"),
            on_click=self._toggle_language,
            style=ft.ButtonStyle(
                color={"": "#333333"},
                animation_duration=300,
            )
        )
        
        # Создаем контейнер с шапкой
        return ft.Container(
            content=ft.Row(
                [
                    self.logo_text,
                    ft.Spacer(),  # Пружина для разделения логотипа и кнопки
                    self.language_button
                ],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                vertical_alignment=ft.CrossAxisAlignment.CENTER
            ),
            padding=ft.padding.only(top=24, bottom=24),
            margin=ft.margin.only(bottom=24),
        )
    
    def _toggle_language(self, e):
        """
        Переключает язык и обновляет компонент.
        
        Args:
            e: Событие нажатия кнопки
        """
        # Вызываем функцию обратного вызова для уведомления основного приложения
        self.on_language_change(e)
        # Обновляем тексты в компоненте
        self._update_texts()
        # Перерисовываем компонент
        self.update()
    
    def _update_texts(self):
        """
        Обновляет тексты компонента в соответствии с текущим языком.
        """
        if hasattr(self, 'language_button') and self.language_button:
            self.language_button.text = self.localization.get("language_switch") 
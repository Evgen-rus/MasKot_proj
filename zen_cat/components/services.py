"""
Модуль, содержащий компонент блока услуг для приложения Zen-кот.

Блок услуг содержит 4 карточки с иконками и описанием предоставляемых услуг.
"""

import flet as ft
from utils.localization import Localization


class Services(ft.UserControl):
    """
    Компонент блока услуг, содержащий карточки с описанием услуг.
    
    Атрибуты:
        localization (Localization): Объект локализации
        theme (dict): Словарь с настройками темы
    """
    
    def __init__(self, localization: Localization, theme: dict):
        """
        Инициализирует компонент блока услуг.
        
        Args:
            localization (Localization): Объект локализации
            theme (dict): Словарь с настройками темы
        """
        super().__init__()
        self.localization = localization
        self.theme = theme
        
        # Заголовок блока
        self.title = ft.Text()
        
        # Карточки услуг
        self.service_cards = []
    
    def build(self):
        """
        Строит компонент блока услуг.
        
        Returns:
            ft.Container: Контейнер с блоком услуг
        """
        # Заголовок блока
        self.title = ft.Text(
            value=self.localization.get("services_title"),
            size=self.theme["font_sizes"]["lg"],
            weight=ft.FontWeight.BOLD,
            color=self.theme["colors"]["text"],
            text_align=ft.TextAlign.CENTER
        )
        
        # Создаем карточки услуг
        self.service_cards = [
            self._create_service_card("service_1_title", "service_1_desc", "💻"),
            self._create_service_card("service_2_title", "service_2_desc", "🎨"),
            self._create_service_card("service_3_title", "service_3_desc", "📊"),
            self._create_service_card("service_4_title", "service_4_desc", "🔧")
        ]
        
        # Создаем адаптивное размещение карточек (2x2 на мобильных, 4x1 на десктопе)
        services_grid = self._create_responsive_grid(self.service_cards)
        
        # Создаем контейнер с блоком услуг
        return ft.Container(
            content=ft.Column(
                [
                    self.title,
                    ft.Container(height=self.theme["spacing"]["md"]),  # Отступ
                    services_grid
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=0
            ),
            margin=ft.margin.only(bottom=self.theme["spacing"]["xl"]),
            padding=ft.padding.all(self.theme["spacing"]["md"])
        )
    
    def _create_service_card(self, title_key, desc_key, icon):
        """
        Создает карточку услуги.
        
        Args:
            title_key (str): Ключ для заголовка услуги
            desc_key (str): Ключ для описания услуги
            icon (str): Эмодзи для иконки услуги
            
        Returns:
            ft.Container: Контейнер с карточкой услуги
        """
        card_title = ft.Text(
            value=self.localization.get(title_key),
            size=self.theme["font_sizes"]["md"],
            weight=ft.FontWeight.BOLD,
            color=self.theme["colors"]["text"]
        )
        
        card_description = ft.Text(
            value=self.localization.get(desc_key),
            size=self.theme["font_sizes"]["sm"],
            color=self.theme["colors"]["text_light"]
        )
        
        icon_text = ft.Text(
            value=icon,
            size=32,
            color=self.theme["colors"]["primary"]
        )
        
        return ft.Container(
            content=ft.Column(
                [
                    icon_text,
                    ft.Container(height=self.theme["spacing"]["xs"]),  # Отступ
                    card_title,
                    ft.Container(height=self.theme["spacing"]["xs"]),  # Отступ
                    card_description
                ],
                spacing=0,
                horizontal_alignment=ft.CrossAxisAlignment.START
            ),
            padding=self.theme["spacing"]["md"],
            border_radius=8,
            bgcolor=self.theme["colors"]["white"],
            width=350,  # Максимальная ширина карточки
            height=180,  # Высота карточки
            margin=ft.margin.all(self.theme["spacing"]["xs"])
        )
    
    def _create_responsive_grid(self, cards):
        """
        Создает адаптивную сетку карточек.
        
        Args:
            cards (list): Список карточек
            
        Returns:
            ft.ResponsiveRow: Адаптивная сетка карточек
        """
        # На мобильных устройствах - 2 колонки, на десктопе - 4 колонки
        return ft.Column(
            [
                ft.Row(
                    [cards[0], cards[1]],
                    alignment=ft.MainAxisAlignment.CENTER,
                    wrap=True
                ),
                ft.Row(
                    [cards[2], cards[3]],
                    alignment=ft.MainAxisAlignment.CENTER,
                    wrap=True
                )
            ],
            spacing=self.theme["spacing"]["sm"],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )
    
    def update_texts(self):
        """
        Обновляет тексты компонента в соответствии с текущим языком.
        """
        self.title.value = self.localization.get("services_title")
        
        # Обновляем тексты в карточках
        service_keys = [
            ("service_1_title", "service_1_desc"),
            ("service_2_title", "service_2_desc"),
            ("service_3_title", "service_3_desc"),
            ("service_4_title", "service_4_desc")
        ]
        
        for i, (title_key, desc_key) in enumerate(service_keys):
            if i < len(self.service_cards):
                card_content = self.service_cards[i].content
                # Заголовок находится на позиции 2 (после иконки и отступа)
                card_content.controls[2].value = self.localization.get(title_key)
                # Описание находится на позиции 4 (после заголовка и отступа)
                card_content.controls[4].value = self.localization.get(desc_key) 
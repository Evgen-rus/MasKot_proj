"""
Основной модуль приложения Zen-кот.

Инициализирует Flet-приложение, настраивает тему и управляет основным пользовательским интерфейсом.
"""

import flet as ft
from zen_cat.utils.localization import Localization
from zen_cat.components.header import Header
from zen_cat.components.services import Services
from zen_cat.components.about import About
from zen_cat.components.contact_form import ContactForm
from zen_cat.components.footer import Footer


# Тема приложения с цветами и отступами
THEME = {
    "colors": {
        "primary": "#2dd4bf",      # Бирюзовый акцент
        "background": "#f8f5f0",   # Светлый беж
        "text": "#333333",         # Тёмно-серый
        "text_light": "#666666",   # Серый
        "white": "#ffffff"         # Белый
    },
    "spacing": {
        "xs": 8,    # Очень маленький отступ
        "sm": 16,   # Маленький отступ
        "md": 24,   # Средний отступ
        "lg": 32,   # Большой отступ
        "xl": 48    # Очень большой отступ
    },
    "font_sizes": {
        "xs": 14,   # Очень маленький текст
        "sm": 16,   # Маленький текст
        "md": 18,   # Средний текст
        "lg": 24,   # Большой текст (заголовки)
        "xl": 32    # Очень большой текст (главный заголовок)
    }
}


class ZenCatApp:
    """
    Основной класс приложения Zen-кот.
    
    Управляет состоянием всего приложения, включая выбранный язык,
    и отвечает за построение основного пользовательского интерфейса.
    """
    
    def __init__(self, page: ft.Page):
        """
        Инициализирует экземпляр приложения.
        
        Args:
            page (ft.Page): Объект страницы Flet
        """
        self.page = page
        self.localization = Localization()  # Создаем объект локализации
        
        # Настройка страницы
        self.page.title = "Zen-кот"
        self.page.bgcolor = THEME["colors"]["background"]
        self.page.padding = 0
        self.page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        self.page.scroll = ft.ScrollMode.AUTO
        
        # Создание компонентов
        self.header = Header(self.localization, self.toggle_language)
        self.services = Services(self.localization, THEME)
        self.about = About(self.localization, THEME)
        self.contact_form = ContactForm(self.localization, THEME)
        self.contact_form.page = self.page  # Устанавливаем page для формы
        self.footer = Footer(self.localization, THEME)
        
        # Элементы основного экрана
        self.main_title = ft.Text()
        self.main_subtitle = ft.Text()
        
        # Создание контейнеров для компонентов
        self.header_container = ft.Container(content=self.header.container)
        self.main_container = self._create_main_screen()
        self.services_container = ft.Container(content=self.services.container)
        self.about_container = ft.Container(content=self.about.container)
        self.contact_container = ft.Container(content=self.contact_form.container)
        self.footer_container = ft.Container(content=self.footer.container)
        
        # Добавляем основной контейнер на страницу
        self.build()
    
    def _create_main_screen(self):
        """
        Создает основной экран с заголовком, подзаголовком и изображением кота.
        
        Returns:
            ft.Container: Контейнер с основным экраном
        """
        # Создаем заголовок
        self.main_title = ft.Text(
            value=self.localization.get("main_title"),
            size=THEME["font_sizes"]["xl"],
            weight=ft.FontWeight.BOLD,
            color=THEME["colors"]["text"],
            text_align=ft.TextAlign.CENTER
        )
        
        # Создаем подзаголовок
        self.main_subtitle = ft.Text(
            value=self.localization.get("main_subtitle"),
            size=THEME["font_sizes"]["md"],
            color=THEME["colors"]["text_light"],
            text_align=ft.TextAlign.CENTER
        )
        
        # Временная замена изображения кота эмодзи (в будущем будет заменено на реальное изображение)
        cat_image = ft.Text(
            "😸",
            size=120,
            text_align=ft.TextAlign.CENTER
        )
        
        # Создаем контейнер для основного экрана
        return ft.Container(
            content=ft.Column(
                [
                    self.main_title,
                    ft.Container(height=THEME["spacing"]["md"]),  # Отступ
                    self.main_subtitle,
                    ft.Container(height=THEME["spacing"]["lg"]),  # Отступ
                    cat_image
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=THEME["spacing"]["sm"]
            ),
            margin=ft.margin.only(top=THEME["spacing"]["xl"], bottom=THEME["spacing"]["xl"]),
            padding=ft.padding.all(THEME["spacing"]["md"])
        )
    
    def build(self):
        """
        Строит основной интерфейс приложения и добавляет его на страницу.
        """
        # Основной контейнер с максимальной шириной для контента
        content = ft.Container(
            content=ft.Column(
                [
                    self.header_container,
                    self.main_container,
                    self.services_container,
                    self.about_container,
                    self.contact_container,
                    self.footer_container
                ],
                spacing=0,
            ),
            width=800,  # Максимальная ширина контента
            padding=ft.padding.only(left=THEME["spacing"]["md"], right=THEME["spacing"]["md"]),
        )
        
        # Добавляем контент на страницу
        self.page.add(content)
    
    def toggle_language(self, e):
        """
        Переключает язык приложения и обновляет интерфейс.
        
        Args:
            e: Событие нажатия кнопки
        """
        self.localization.toggle_lang()
        self.update_ui()
    
    def update_ui(self):
        """
        Обновляет все компоненты интерфейса с текущим языком.
        """
        # Обновление компонентов
        self.header._update_texts()
        self.services.update_texts()
        self.about.update_texts()
        self.contact_form.update_texts()
        self.footer.update_texts()
        
        # Обновление текстов основного экрана
        self.main_title.value = self.localization.get("main_title")
        self.main_subtitle.value = self.localization.get("main_subtitle")
        
        # Обновляем страницу
        self.page.update()


def main(page: ft.Page):
    """
    Главная функция, которая инициализирует и запускает приложение.
    
    Args:
        page (ft.Page): Объект страницы Flet
    """
    # Создаем экземпляр приложения
    app = ZenCatApp(page)


# Запуск приложения в веб-браузере
if __name__ == "__main__":
    ft.app(target=main, view=ft.WEB_BROWSER) 
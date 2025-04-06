"""
Модуль локализации для приложения Zen-кот.

Содержит класс Localization, который предоставляет функционал для переключения 
между русским и английским языками и получения текстов на выбранном языке.
"""


class Localization:
    """
    Класс для управления локализацией приложения на разных языках.
    
    Атрибуты:
        lang (str): Текущий выбранный язык (ru или en)
        _texts (dict): Словарь с текстами для всех поддерживаемых языков
    """
    
    def __init__(self, default_lang="ru"):
        """
        Инициализирует объект локализации с языком по умолчанию.
        
        Args:
            default_lang (str): Язык по умолчанию (ru или en)
        """
        self.lang = default_lang
        self._texts = {
            "ru": {
                # Хедер
                "language_switch": "EN",
                
                # Первый экран
                "main_title": "ИТ, КОТОРОЕ НЕ ТРЕВОЖИТ",
                "main_subtitle": "Минимализм. Спокойствие. Надёжность.",
                
                # Блок услуг
                "services_title": "Наши услуги",
                "service_1_title": "Разработка",
                "service_1_desc": "Создаем минималистичные и функциональные приложения, не перегруженные деталями.",
                "service_2_title": "Дизайн",
                "service_2_desc": "Проектируем интерфейсы, которые не отвлекают и помогают сосредоточиться.",
                "service_3_title": "Консалтинг",
                "service_3_desc": "Помогаем упростить процессы и убрать всё лишнее из ваших проектов.",
                "service_4_title": "Поддержка",
                "service_4_desc": "Обеспечиваем стабильную и спокойную работу ваших сервисов 24/7.",
                
                # Блок о нас
                "about_title": "О нас",
                "about_text": "Мы — команда разработчиков и дизайнеров, которые верят, что технологии должны успокаивать, а не тревожить. Наша миссия — создавать цифровые продукты, которые уменьшают информационный шум и помогают сосредоточиться на важном.",
                
                # Форма обратной связи
                "contact_title": "Оставить заявку",
                "name_label": "Имя",
                "email_label": "Email",
                "message_label": "Сообщение",
                "submit_button": "Отправить",
                "form_success": "Спасибо! Мы свяжемся с вами в ближайшее время.",
                "name_placeholder": "Ваше имя",
                "email_placeholder": "Ваш email",
                "message_placeholder": "Ваше сообщение",
                
                # Футер
                "copyright": "© 2025 Zen-кот. Все права защищены."
            },
            "en": {
                # Header
                "language_switch": "RU",
                
                # First screen
                "main_title": "IT THAT DOESN'T DISTURB",
                "main_subtitle": "Minimalism. Calm. Reliability.",
                
                # Services block
                "services_title": "Our Services",
                "service_1_title": "Development",
                "service_1_desc": "We create minimalist and functional applications that aren't overloaded with details.",
                "service_2_title": "Design",
                "service_2_desc": "We design interfaces that don't distract and help you focus.",
                "service_3_title": "Consulting",
                "service_3_desc": "We help simplify processes and remove everything unnecessary from your projects.",
                "service_4_title": "Support",
                "service_4_desc": "We ensure stable and calm operation of your services 24/7.",
                
                # About us block
                "about_title": "About Us",
                "about_text": "We are a team of developers and designers who believe that technology should calm, not disturb. Our mission is to create digital products that reduce information noise and help focus on what's important.",
                
                # Contact form
                "contact_title": "Get in Touch",
                "name_label": "Name",
                "email_label": "Email",
                "message_label": "Message",
                "submit_button": "Submit",
                "form_success": "Thank you! We'll get back to you soon.",
                "name_placeholder": "Your name",
                "email_placeholder": "Your email",
                "message_placeholder": "Your message",
                
                # Footer
                "copyright": "© 2025 Zen-cat. All rights reserved."
            }
        }
    
    def get(self, key):
        """
        Получает текст по ключу для текущего языка.
        
        Args:
            key (str): Ключ для текста
            
        Returns:
            str: Текст на текущем языке или ключ, если текст не найден
        """
        return self._texts[self.lang].get(key, key)
    
    def set_lang(self, lang):
        """
        Устанавливает текущий язык.
        
        Args:
            lang (str): Язык для установки ('ru' или 'en')
            
        Returns:
            bool: True, если язык был изменен, False в противном случае
        """
        if lang in self._texts:
            self.lang = lang
            return True
        return False
    
    def toggle_lang(self):
        """
        Переключает язык между русским и английским.
        
        Returns:
            str: Новый установленный язык
        """
        self.lang = "en" if self.lang == "ru" else "ru"
        return self.lang 
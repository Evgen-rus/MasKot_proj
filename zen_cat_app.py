"""
Точка входа для запуска приложения Zen-кот.

Импортирует и запускает главную функцию из основного модуля приложения.
"""

import os
import sys

# Добавляем путь к проекту в sys.path для корректного импорта
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from zen_cat.main import main
import flet as ft

if __name__ == "__main__":
    # Запускаем приложение в веб-браузере
    ft.app(target=main, view=ft.WEB_BROWSER) 
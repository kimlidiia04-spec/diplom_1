Автотесты для программы заказа бургеров Stellar Burgers

Реализованные сценарии
Созданы юнит-тесты для проверки классов Bun, Burger, Ingredient и Database.
Покрытие кода тестами составляет 100%.
HTML-отчёт о покрытии находится в htmlcov/index.html.

Структура проекта
praktikum/ — пакет с кодом программы.
tests/ — пакет с автотестами, разделёнными по классам (bun_test.py, burger_test.py и другие).

Запуск автотестов
Установка зависимостей:
pip install -r requirements.txt

Запуск тестов и создание HTML-отчёта:
pytest --cov=praktikum --cov-report=html
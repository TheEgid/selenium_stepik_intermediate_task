# selenium_stepik_intermediate_task

Автотест (PYTEST), проверяющий добавление товара в корзину на сайте [selenium1py.pythonanywhere.com](http://selenium1py.pythonanywhere.com).

### Как установить

Скачиваем файлы и переходим в папку.
Устанавливаем chromedriver по [этой инструкции](https://selenium-python.com/install-chromedriver-chrome)
Python 3.7 должен быть уже установлен.
Затем используем pip для установки зависимостей:

```
pip install -r requirements.txt
```

### Опция

```
custom options:
  --language=LANGUAGE   Choose language  #  Выбор языка тестирования страницы
```

### Использование

После настройки скрипт запускаем из корневой папки.
Выполняются автотесты для разных языков пользователей, передаем нужный язык в командной строке.

```
pytest --language=es test_items.py

pytest --language=fr test_items.py
```

### Цель проекта

Код написан в образовательных целях для [stepik.org](https://stepik.org/)

# 🚀 Sprint_5 — UI Automation Testing

Автоматизированные UI-тесты веб-приложения **Stellar Burgers** с использованием **Selenium WebDriver** и **pytest**. Проект покрывает регистрацию, авторизацию, работу личного кабинета и навигацию в разделе «Конструктор».

---

## 🎯 Цели проекта

* Проверка регистрации, авторизации и выхода из аккаунта
* Тестирование переходов между разделами приложения
* Генерация уникальных тестовых данных (email, пароль)
* Организация автотестов по best practices

---

## 🛠 Стек

Python, Selenium, pytest, Google Chrome, Mozilla Firefox, Git

---

## 📌 Структура проекта

```
tests/                  # тесты
conftest.py             # фикстуры
locators.py             # локаторы
data.py                 # тестовые данные и сообщения
curl.py                 # URL страниц
generating_logins.py    # генерация email/пароля
helpers.py              # вспомогательные функции
pytest.ini              # конфиг pytest
```

* Тесты автономны, используют driver.quit()
* Локаторы и генерация данных вынесены в отдельные модули
* Тесты сгруппированы по функциональности

---

## ⚙ Запуск

```bash
git clone https://github.com/ValeevaLudmila/Sprint_5.git
pip install -r requirements.txt
pytest
```

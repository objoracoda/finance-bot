Небольшой Telegram Бот для учета личных расходов

В переменных окружения `.env` надо проставить API токен бота

`MY_TELEGRAM_TOKEN` — API токен бота

В качестве инструмента для создания зависимостей используется `pipenv`

```
$ brew install pipenv
```

Установить библиотеки в переменное окружение

```
pipenv install aiogram
pipenv install sqlite3
pipenv install pandas
```

Чтобы запустить pipenv с зависимостями

```
pipenv run python main.py
```

Пример работы Бота

![hippo](https://github.com/objoracoda/finance-bot/blob/main/readme/finbot.gif)

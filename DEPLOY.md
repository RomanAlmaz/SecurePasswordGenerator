# Развёртывание на Render.com через GitHub

## 1. Репозиторий на GitHub

1. Создайте репозиторий на [github.com](https://github.com) (например, `secure-password-generator`).
2. В корне проекта выполните:

```bash
git init
git add .
git commit -m "Initial commit: Secure Password Generator"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/secure-password-generator.git
git push -u origin main
```

(Замените `YOUR_USERNAME` и имя репозитория на свои.)

## 2. Создание сервиса на Render

1. Зайдите на [render.com](https://render.com) и войдите (можно через GitHub).
2. **Dashboard** → **New** → **Web Service**.
3. Подключите ваш GitHub-аккаунт, если ещё не подключён, и выберите репозиторий `secure-password-generator`.
4. Настройте сервис:

| Поле | Значение |
|------|----------|
| **Name** | `secure-password-generator` (или любое) |
| **Region** | Frankfurt (или ближайший) |
| **Branch** | `main` |
| **Runtime** | Python 3 |
| **Build Command** | `bash build.sh` |
| **Start Command** | `gunicorn secure_password_generator.wsgi:application` |
| **Instance Type** | Free |

5. **Environment** (переменные окружения):

| Key | Value |
|-----|--------|
| `SECRET_KEY` | Случайная строка (например, сгенерируйте на [djecrety.ir](https://djecrety.ir/) или оставьте **Generate** в Render) |
| `DEBUG` | `False` |
| `ALLOWED_HOSTS` | `.onrender.com` (или оставьте пустым — в коде уже есть значение по умолчанию) |

6. Нажмите **Create Web Service**.

## 3. Деплой

- После сохранения настроек Render автоматически запустит сборку и деплой.
- Логи сборки и запуска можно смотреть вкладке **Logs**.
- После успешного деплоя сайт будет доступен по адресу вида:  
  `https://secure-password-generator-XXXX.onrender.com`

## 4. Автодеплой из GitHub

- При каждом `git push` в ветку `main` Render по умолчанию пересобирает и перезапускает сервис.
- Отключить или изменить это можно в **Settings** → **Build & Deploy** → **Auto-Deploy**.

## 5. Важно

- На бесплатном плане сервис «засыпает» после неактивности; первый запрос после сна может идти 30–60 секунд.
- База SQLite на Render **эпимерная**: при перезапуске/пересборке данные сбрасываются. Для этого проекта это допустимо (пароли и слова нигде не хранятся).
- Секрет `SECRET_KEY` храните только в переменных окружения Render, не коммитьте его в репозиторий.

## Альтернатива: Blueprint (render.yaml)

В корне проекта есть файл `render.yaml`. В Render можно развернуть проект по Blueprint:

1. **Dashboard** → **New** → **Blueprint**.
2. Укажите репозиторий; Render подхватит `render.yaml` и создаст Web Service с указанными в нём настройками.
3. Переменную `SECRET_KEY` при необходимости задайте или сгенерируйте вручную в **Environment** после создания сервиса.

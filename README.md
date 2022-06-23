# Тестовое задание по автотестам Яндекс Диска

## Перед началом выполнения задания:
1. Надо завести аккаунт в сервисе Yandex и предоставить логин/пароль для выполнения и проверки ТЗ
2. Загрузить файл с названием “Файл для копирования” в общую папку на диске
3. Создать новую папку, в папке создать файл

## 1 Кейс: Копирование файла в папку
**Предусловие:**
* Открыть браузер

**Шаги:**
* Открыть страницу http://yandex.ru
* Авторизоваться
* Открыть Яндекс.Диск
* Скопировать файл “Файл для копирования” в созданную ранее папку
* Открыть папку
* Удалить файлы кроме скопированного

**Ожидаемый результат:**
* Скопированный файл находится в папке
* Название соответствует оригиналу

**Постусловие:**
* Разлогиниться
* Закрыть браузер

## 2 Кейс: Загрузка файла в Яндекс Диск
**Предусловие:**
* Открыть браузер

**Шаги:**
* Открыть страницу http://yandex.ru
* Авторизоваться
* Открыть Яндекс.Диск
* Создать новую папку и назвать её
* Открыть папку
* Загрузить файл расширения .txt с текстом
* Открыть файл
* Проверить текст в файле

**Ожидаемый результат:**
* Текст соответствует ожиданиям

**Постусловие:**
* Разлогиниться
* Закрыть браузер

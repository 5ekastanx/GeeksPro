# GeeksPro

**GeeksPro** — это проект для управления группой стажеров.  
Проект пока в начальной стадии разработки. Цель — создать удобную и красивую админ-панель для работы со стажерами, используя **Django** и **Jazzmin**.  

> Сейчас проект включает:  
> - Админ-панель на Django с темой Jazzmin  
> - Модель `Trainee` (стажер) и `Role` (роль стажера)  
> - Русский интерфейс админки  
> - Списки, фильтры и поиск по стажерам  


---

## ⚡ Установка и запуск

```bash
git clone https://github.com/<ваше_имя>/GekksPro.git
cd GekksPro
```
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux / macOS
source venv/bin/activate
```
```bash
pip install Django>=4.2 django-jazzmin django-modeltranslation
```
```bash
python manage.py makemigrations
python manage.py migrate
```
```bash
python manage.py createsuperuser
```
```bash
python manage.py runserver
```

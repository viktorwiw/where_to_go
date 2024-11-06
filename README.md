# where_to_go

Интерактивная карта Москвы для просмотра интересных мест и достопримечательностей с подробной информацией и фотографиями.

Демо сайта - [mexan.pythonanywhere.com](https://mexan.pythonanywhere.com) Интерфейс сайта адаптирован для работы как на смартфонах, так и на ПК.


## Добавление новых мест и изменение существующих 

Для добавления новой локации, необходимо:
1. Перейти в админ-панель [127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)
2. Ввести Логин - Пароль
3. Перейти к модели “Places” и нажать “Добавить”
4. Заполнить поля (название, описание и координаты) и добавте фотографии (можно изменить порядок отображения переьаскивая их)
5. Нажать кнопку "Сохранить"

Для изменения существующей локации, необходимо:
1. Перейти в админ-панель [127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)
2. Ввести Логин - Пароль
3. Перейти к модели “Places” и выбрать нужное место. Также есть ужобное поле поиска.
4. Отредактировать информацию или добавить новые фотографии. Возможно изменение порядка отображения фотографий, просто
перетаскивая их и меняя местами или нажимать на кнопки-стрелочки.
5. Нажать кнопку "Сохранить" 


## Запуск

Для изоляции проекта рекомендуется развернуть виртуальное окружение:

для Linux и MacOS
```bash
python3.10 -m venv env
source env/bin/activate
```

для Windows
```bash
python3.10 -m venv env
venv\Scripts\activate.bat
```

Python3.10 должен быть уже установлен. Затем используйте pip (или pip3, есть конфликт с Python2) для установки зависимостей:

Скачайте код с GitHub. Установите зависимости:

```sh
pip install -r requirements.txt
```

Создайте базу данных SQLite

```sh
python3 manage.py migrate
```

Запустите разработческий сервер

```shell
python3 manage.py runserver
```

## Переменные окружения

Часть настроек проекта берётся из переменных окружения. Чтобы их определить, создайте файл `.env` рядом с `manage.py` и запишите туда данные в таком формате: `ПЕРЕМЕННАЯ=значение`.

Доступны 3 переменные:
- `DEBUG` — дебаг-режим. Поставьте `True`, чтобы увидеть отладочную информацию в случае ошибки.
- `SECRET_KEY` — секретный ключ проекта
- `ALLOWED_HOSTS` — Для дебаг-режима не заполнять. [Документация Django](https://docs.djangoproject.com/en/3.1/ref/settings/#allowed-hosts)

## API
Отправте запрос по адресу: 

```
https://127.0.0.1:8000/place/{location_id: int}
```

### Пример:
*Request*
```
https://127.0.0.1:8000/place/3
```

*Response*
```json
{
    "title": "Заброшенный пионерский лагерь «Сказка»",
    "imgs": [
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/0bbdc405dc1df252d80e15bee56021c9.jpg",
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/24cc9bdbdce5240a8a0dc616cc4bd786.jpg",
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/5b4a454c277127aff7e32b004ce3c7b0.jpg",
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/5e7974c7652c32dc2121ed58f3d705a4.jpg"
    ],
    "description_short": "Предупреждаем: это место давным-давно превратилось из дружелюбного пространства для детского отдыха в не самую безопасную точку на карте. Лучше, конечно, сюда не соваться, но если вы всё же решите побывать в «Сказке», стоит быть настороже.",
    "description_long": "<p>Когда-то в этом лагере отдыхали глухонемые дети, но последние три десятка лет сюда приезжают только любители изучать заброшенные места. В лагере несколько корпусов с довольно своеобразным декором — одно здание охватывает щупальцами огромный осьминог, в пролёте лестниц другого затаилась морская раковина причудливой формы. Повсюду можно увидеть гигантских обитателей моря — морских звёзд, кораллы, водоросли.</p><p>Вместе с этими фантастическими тварями «Сказку», к сожалению, облюбовали полукриминальные индивиды, которые легко могут, в лучшем случае, испортить колёса автомобиля искателей острых ощущений.</p><p>Смельчаки, которые не боятся встречи с российской версией мутантов из фильма «У холмов есть глаза», могут не просто погулять по территории (в конце, кстати, находится действующая база отдыха), но и заглянуть внутрь домиков  с разбитыми детскими кроватками со странными рисунками, куклами с оторванными конечностями, ношеными детскими ботиночками и остальными жутковатыми атрибутами.</p><p>Кроме библиотеки, столовой и жилых помещений здесь есть странный бункер, видимо, предназначавшийся для хозяйственных нужд.</p>",
    "coordinates": {
        "lng": "37.39986097091371",
        "lat": "56.23856019594033"
    }
}
```

## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте Devman.

Тестовые данные взяты с сайта [KudaGo](https://kudago.com/msk/).

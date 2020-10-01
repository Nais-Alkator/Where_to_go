# Куда пойти — Where ot go

Сайт об интересных местах Москвы.

<img src="static_src/.gitbook/assets/site.png"/>

[Демка сайта](http://alkator.pythonanywhere.com/).

## Как запустить

- Скачайте код
- Установите зависимости командой `pip install -r requirements.txt`
- Создайте миграции командой `python manage.py makemigrations`
- Создайте БД командой `python manage.py migrate`
- Запустите сервер командой `python manage.py runserver`

## Переменные окружения

Часть настроек проекта берётся из переменных окружения. Чтобы их определить, создайте файл `.env` рядом с `settings.py` и запишите туда данные в таком формате: `ПЕРЕМЕННАЯ=значение`.

- `DEBUG` — дебаг-режим. Поставьте `True`, чтобы увидеть отладочную информацию в случае ошибки.
- `SECRET_KEY` — секретный ключ проекта

## Настройки

Внизу справа на странице можно включить отладочный режим логгирования.

![debug mode]<img src="static_src/.gitbook/assets/debug-option.png"/>

Настройки сохраняются в Local Storage браузера и не пропадают после обновления страницы. Чтобы сбросить настройки удалите ключи из Local Storage с помощью Chrome Dev Tools —&gt; Вкладка Application —&gt; Local Storage.

Если что-то работает не так, как ожидалось, то начните с включения отладочного режима логгирования.


## Источники данных

Фронтенд получает данные из двух источников. Первый источник — это JSON, запечённый внутрь HTML. Он содержит полный список объектов на карте. И он прячется внутри тега `script`:

```javascript
<script id="places-geojson" type="application/json">
  {
    "type": "FeatureCollection",
    "features": [
      {
        "type": "Feature",
        "geometry": {
          "type": "Point",
          "coordinates": [37.62, 55.793676]
        },
        "properties": {
          // Специфичные для этого сайта данные
          "title": "Легенды Москвы",
          "placeId": "moscow_legends",
          "detailsUrl": "./places/moscow_legends.json"
        }
      },
      // ...
    ]
  }
</script>
```

При загрузке страницы JS код ищет тег с id `places-geojson`, считывает содержимое и помещает все объекты на карту.

Данные записаны в [формате GeoJSON](https://ru.wikipedia.org/wiki/GeoJSON). Все поля здесь стандартные, кроме `properties`. Внутри `properties` лежат специфичные для проекта данные:

* `title` — название локации
* `placeId` — уникальный идентификатор локации, строка или число
* `detailsUrl` — адрес для скачивания доп. сведений о локации в JSON формате

Значение поля `placeId` может быть либо строкой, либо числом. Само значение не играет большой роли, важна лишь чтобы оно было уникальным. Фронтенд использует `placeId` чтобы избавиться от дубликатов — если у двух локаций одинаковый `placeId`, то значит это одно и то же место.

Второй источник данных — это те самые адреса в поле `detailsUrl` c подробными сведениями о локации. Каждый раз, когда пользователь выбирает локацию на карте JS код отправляет запрос на сервер и получает картинки, текст и прочую информацию об объекте. Формат ответа сервера такой:

```javascript
{
    "title": "Экскурсионный проект «Крыши24.рф»",
    "imgs": [
        "https://kudago.com/media/images/place/d0/f6/d0f665a80d1d8d110826ba797569df02.jpg",
        "https://kudago.com/media/images/place/66/23/6623e6c8e93727c9b0bb198972d9e9fa.jpg",
        "https://kudago.com/media/images/place/64/82/64827b20010de8430bfc4fb14e786c19.jpg",
    ],
    "description_short": "Хотите увидеть Москву с высоты птичьего полёта?",
    "description_long": "<p>Проект «Крыши24.рф» проводит экскурсии ...</p>",
    "coordinates": {
        "lat": 55.753676,
        "lng": 37.64
    }
}
```

## База данных

Для взаимодействия с БД необходимо:

- Создать суперпользователя командой `python manage.py createsuperuser`
- Придумать ему логин и пароль
- Зайти в админ панель сайта, к примеру `http://127.0.0.1:8000/admin`
- Ввести придуманные логин и пароль

Зайдя в Places можно добавлять/удалять/редактировать локации, добавлять/удалять изображения или менять их местами путем перетаскивания через поле "Сортировать".

## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).

Тестовые данные взяты с сайта [KudaGo](https://kudago.com).

# [Техническое задание](https://drive.google.com/file/d/1qkPSBEPXQV0PK3aBpPj0D9Ou_FgUOGkl/view?usp=sharing)
## Приветствую, меня зовут Кирилл!
Хотел бы пояснить свое решение отойти от условий задания в ТЗ. Да-да, я знаю, что необходимо написать скрипт на Ruby с использованием библиотек **curb** и **nokogiri** + для получения содержимого html использовать **XPATH**. **Однако** есть некоторые моменты:
- *во-первых*: стоит учесть, что на сайте изменен дизайн и поэтому предоставленный пример в ТЗ не актуален. К тому же я имею большой опыт работы с Python, а в Ruby был знаком только с синтаксисом, не более (пока не получил ТЗ от Вашей компании, теперь я *полностью поглощен* этим языком);  
- *во-вторых*: судя по [статье](https://tldrify.com/10jy) с dev.by, в Вашей компании нет ограничений по используемым языкам для решения задачи;  
- *в-третьих*: срок ТЗ заканчивается, а я все еще не выполнит задачу придерживаясь требуемых условий, к моему большому сожалению.  

Резюмируя все вышеперечисленное, я решил использовать... Python для получения необходимого результата (сильно не серчайте, я исправлюсь).  
Уделите еще несколько минут своего времени и посмотрите видео, в котором я поясняю логику работы скрипта и пытаюсь все это сравнить с Ruby (звук плоховат, записывал используя обычные наушники, прошу прощения у Ваших ушей). Нужно нажать на картинку 👆  
####
[![Watch the video](https://github.com/PyWebChannel/Task/blob/master/petsonic_com/preview.png)](https://vimeo.com/461594355)

## ВАЖНО!
Некоторые уточнения по видео:
- забыл сказать, что для краулеров есть [рекомендация](https://www.petsonic.com/robots.txt) (я не учитывал данное время между запросами, т.к. объем получаемых данных невелик):
> Crawl-delay  
> User-agent: *  
> Crawl-delay: 10

- [ссылка](https://github.com/pyweb-kivi/Parsing) на репозиторий небольших проектов с использованием XPATH --> [simple_project_1](https://github.com/pyweb-kivi/Parsing#user-content-leemarpetcom) и [simple_project_2](https://github.com/pyweb-kivi/Parsing#user-content-itkompasscom) 
- в скрипте не используется логирование, т.к. по условиям ТЗ оно не требуется.

## Запуск скрипта
### LINUX / MacOS
В Linux и MacOS Python установлен по умолчанию, поэтому проблем с запуском не должно возникнуть. Команды для запуска:
`python /path/to/script.py `(для версии Python2.x) или `python3 /path/to/script.py`(для версии Python3.x - скрипт написан на версии 3.8)  
### Windows
В Windows сначала необходимо установить [Python](https://www.python.org/downloads/). Запуск скрипта аналогичен запуску на Linux и MacOS.  
**Важное примечание!** Для корректной работы скрипта необходимо установить библиотеки requests и bs4(beautifulsoup) командами `pip install requests` и `pip install bs4` 

# Ответы на вопросы
### Блок Q1
1. *C какими OС Вы работали? Работали ли с консолью? Какие консольные утилиты Linux Вы знаете и использовали?*  
У меня на компьютере установлены две ОС: Win10 & Ubuntu 18.04. С консолью работаю в обеих операционках. Из утилит использую Vim (если он таковой является).
2. *Как Вы повышаете свою профессиональную квалификацию (названия книг, курсов, сайтов, скринкастов и т.д.)?*  
Мой профиль на [Upwork](https://www.upwork.com/freelancers/~0183eedec2580e72aa), правда больше года я работаю с СНГ. На [Linkedin](https://www.linkedin.com/in/kir-minsk/) указаны курсы, которые я проходил. Из сайтов по курсам еще пожалуй ITVDN. Иногда решаю задачки на [Hackerank](https://www.hackerrank.com/kiril9ndi9). Прохожу курсы на [Stepik'е](https://stepik.org/users/31392700). Книги, если не касательно Python, то "Чистый код". Сейчас читаю "Командная строка Linux" Уильям Шоттс. На Youtube кроме питоновской тематики [Senior Software Vlogger](https://www.youtube.com/channel/UCX3w3jB05SHLbGjZPR0PM6g), [АйТиБорода](https://www.youtube.com/channel/UCeObZv89Stb2xLtjLJ0De3Q), [Чёрный Треугольник](https://www.youtube.com/channel/UCZ26MoNJKaGXFQWKuGVzmAg).  
3. *Какие сторонние библиотеки Вы используете чаще всего для разработки? Какие плюсы в них Вы выделяете для себя? (Ruby или тот язык, на котором пишите).*  
Для парсинга я использую requests, beautifulsoup(bs4) + lxml, selenium (это библиотеки Python). Requests шикарная библиотека для работы с сервером. BS4 в связке lxml делают удобной работу с DOM. Selenium помогает при парсинге сайтов, где без эмуляции браузера не обойтись. Про каждую библиотеку можно еще очень много и долго писать/рассказывать.  
### Блок Q2
1. *Какие инструменты для профайлинга и дебага Вы используете? Какие у них минусы?*
PyTest и logging. Про минусы ничего сказать не могу. С моими задачами данные библиотеки вполне справляются.
2. *Объясните почему происходит следующее (в контексте языка Ruby):*  
    a. **1660 / 100 ≠ 16.6**  
    Потому что по умолчанию выполняется целочисленное деление, для получения ожидаемого результата, какое-либо число необходимо привести к типу float.  
    b. **24.0 * 0.1 ≠ 2.4**  
    Все числа под капотом хранятся в двоичном формате, поэтому при хранении чисел типа float и возникает проблема с округлением, т.к. каждое такое число является рациональным числом. Но, более доступно, чем изложено в [статье на хабре](https://habr.com/ru/post/112953/), у меня сказать не получится. Для решения необходимо пользоваться методом round.
3. *С какими СУБД вы работали? Проектировали ли вы свою собственную БД? Сколько было в ней таблиц? С какой самой большой таблицей по количеству записей Вы работали?*  
PostgreSQL. Да. 3 таблицы. >8000 строк / >30 столбцов.
4. *Оптимизировали ли Вы запросы в SQL? Как Вы это делали? Как Вы понимаете что запрос выполняется оптимально?*  
Не было необходимости оптимизировать запросы, т.к. таблицы с небольшим количеством данных.

## PS
Мой последний проект заключался в сборе данных с [сайта](https://artkeramika-opt.ru/). Необходимо было собрать все коллекции из разделов [керамогранит](https://artkeramika-opt.ru/catalog/collections/keramogranit/) и [керамическая плитка](https://artkeramika-opt.ru/catalog/collections/keramicheskaya-plitka/). А также для каждой коллекции необходимо было собрать все элементы коллекции.
**Данные коллекций для сбора:**
| Категория	| Наименование	| Производитель |	Страна |	Изображение |	Цена |	Помещение	| URL |
|:---------:|:-------------:|:-------------:|:------:|:------------:|:----:|:----------:|:---:|
... | ... | ... | ... | ... | ... | ... 

**Данные элементов по каждой коллекции для сбора:**  
| Наименование |	Цена |	Единица измерения |	Изображение |	URL |	Стиль коллекции |	Производитель |	Категория |	Тип плитки |	Страна |	Артикул |	Коллекция |	Тип материала |	Основной цвет |	Рисунок |	Размер |	Поверхность |	Ширина, мм |	Длина, мм |	Толщина (мм) |	Формат (см) |	Форма |	Кол-во шт в коробке |	Кол-во м2 (м.п.) в коробке |	Вес коробки (кг) |	Кол-во коробок на поддоне |	Кол-во м2 (м.п.) на поддоне |	Вес поддона (кг) |	Входит в коллекцию |	Серия |	Производство |	Округление м2 на поддоне (коробок) |	Округление шт на поддоне (коробок) |
|:---------:|:---------:|:---------:|:---------:|:---------:|:---------:|:---------:|:---------:|:---------:|:---------:|:---------:|:---------:|:---------:|:---------:|:---------:|:---------:|:---------:|:---------:|:---------:|:---------:|:---------:|:---------:|:---------:|:---------:|:---------:|:---------:|:---------:|:---------:|:---------:|:---------:|:---------:|:---------:|:---------:|
|...|...|...|...|...|...|...|...|...|...|...|...|...|...|...|...|...|...|...|...|...|...|...|...|...|...|...|...|...|...|...|...|...|

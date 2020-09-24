#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import csv
import json
import re

from bs4 import BeautifulSoup as bs
import requests

HEADERS = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                         "AppleWebKit/537.36 (KHTML, like Gecko) "
                         "Chrome/83.0.4103.116 Safari/537.36"}
HEADERS_CSV = ("Category URL",
               "Category name",
               "Product URL",
               "Product name",
               "Unit",
               "Price",
               "Image",)


def get_page(url):
    """Ф-ция возвращает html страницы, параметр - url целевой страницы"""
    r = requests.get(url, headers=HEADERS)
    # если статус код ответа отличный от 200, тогда выпадает исключение и скрипт завершает свое выполнение
    try:
        r.raise_for_status()
        return r.text
    except requests.exceptions.HTTPError as e:
        print(e)
        quit()


def get_category_urls(html):
    """Ф-ция возвращает словарь/хэш со всеми категориями,
    где ключ - урл категории, значение -> наименование категории"""
    soup = bs(html, "lxml")
    # словарь/хэш типа: {урл категории: наименование категории} | Ruby: {"урл категории" => "наименование категории"}
    cat_urls_names = {}

    try:
        # находим все h5, т.е. список всех категорий --> h5.subcategory-name
        # xpath: //h5[@class='subcategory-name']
        block_h5 = soup.find_all("h5", class_="subcategory-name")

        # с помощью цикла получаем атрибут href и текст тега a --> h5 > a,
        # на каждой итерации добавляем значение href в хэш cat_urls_names
        for h5 in block_h5:
            cat_url = h5.find("a", class_="subcategory-name").get("href")
            cat_name = h5.find("a", class_="subcategory-name").text
            # print(f"Наименование категории: {cat_name}, урл категории: {cat_url}")
            cat_urls_names.update({cat_url: cat_name})

        return cat_urls_names

    # если выпадает исключение AttributeError, скрипт завершает свое выполнение
    except (AttributeError, Exception) as e:
        print(e, "->", "Проверить правильность url, т.к. раздела 'категории' на странице нет!")
        quit()


def get_product_urls(html):
    """Ф-ция возвращает список/массив с урлами продуктов для указанной категории
    или пустой список/массив (если продуктов в данной категории нет)"""
    soup = bs(html, "lxml")
    product_urls = []  # список/массив урлов продуктов для категории
    try:
        # находим все li продуктов, потом с помощью цикла на каждой итерации получаем ссылку на продукт и
        # добавляем эту ссылку в массив product_urls
        block_li = soup.find("ul", id="product_list").find_all("li")
        for li in block_li:
            # урл продукта
            product_url = li.find("div", class_="product-desc").find("a").get("href")
            product_urls.append(product_url)

        return product_urls

    except Exception as e:
        print(e, "->", "проверить категорию, возможно продуктов в данной категории нет!")
        return product_urls


def get_product_data(html):
    """Ф-ция возвращает собранные данные о продукте(Наименование продукта, вид упаковки, изображение, стоимость)"""
    soup = bs(html, "lxml")
    unit_price = {}  # словарь/хэш типа: {вид упаковки: стоимость} | Ruby: {"вид упаковки" => "стоимость"}
    try:
        # Наименование продукта
        prod_name = soup.find("h1", class_="product_main_name").text.strip()
        if len(prod_name) < 1:
            prod_name = "Product name Not Found"

        # Ссылка на изображение продукта
        img = soup.find("img", id="bigpic").get("src")
        if len(img) < 1:
            img = "Img name Not Found"

        # Вид упаковки (единицы, вес, в новой версии сайта все вперемешку, поэтому собирается вместе
        # без разделения на штуки, вес и т.п.) + стоимость
        block_ul = soup.find_all("ul", class_="attribute_radio_list pundaline-variations")
        if len(block_ul) > 0:
            for ul in block_ul:
                block_li = ul.find_all("li")
                for li in block_li:
                    # вид упакови
                    unit = li.find("span", class_="radio_label").text.strip()
                    # стоимость
                    price = re.search(r"\d{1,}\.\d{1,}", li.find("span", class_="price_comb").text.strip()).group(0)
                    # формируем словарь/хэш типа: {вид упакови: стоимость} | {"вид упакови" => "стоимость"}
                    unit_price.update({unit: price})
        else:
            unit = "Unit name Not Found"
            price = re.search(r"\d{1,}\.\d{1,}", soup.find("span", id="our_price_display").text.strip()).group(0)
            if len(price) < 1:
                price = "Price Not Found"
            unit_price.update({unit: price})

        return prod_name, unit_price, img

    except (AttributeError, Exception) as e:
        print(e, "->", "Имя продукта не найдено, проверить урл!")


def write_json(cat_data):
    """Запись json файла типа:
    [{Cat_name: наименование категории,
    Cat_url:  урл категории,
    Product_urls:  урлы продуктов для данной категории}]"""
    try:
        data = json.load(open("cat_url_prod_urls.json"))
    except:
        data = []

    data.append(cat_data)

    with open("cat_url_prod_urls.json", "w", encoding='utf-8') as json_file:
        json.dump(data, json_file, indent=4, ensure_ascii=False)


def sum_line(csv_file):
    """Ф-ция возвращает количество строк в csv файле"""
    with open(csv_file) as f:
        return sum(1 for line in f)


def write_csv(data):
    """Ф-ция записывает в csv файл данные из параметра data"""
    with open("petsonic_com.csv", 'a', encoding="utf-8") as f:
        writer = csv.writer(f)
        if sum_line("petsonic_com.csv") < 1:
            writer.writerow(HEADERS_CSV)

        writer.writerow( (data['Category URL'],
                         data['Category name'],
                         data['Product URL'],
                         data['Product name'],
                         data['Unit'],
                         data['Price'],
                         data['Image'],) )


def main():
    """Алгоритм действия"""
    url = "https://www.petsonic.com/snacks-huesos-para-perros/"

    cat_url_prod_urls = {}  # словарь/хэш типа: {урл категории: [массив урлов продуктов]}
    category_urls = get_category_urls(get_page(url))  # урлы категорий
    print(f"Найдено категорий: {len(category_urls)}")
    print("Сформирован словарь/хэш со всеми категориями, где ключ - урл категории, значение -> наименование категории")
    for num, (key, value) in enumerate(category_urls.items(), start=1):
        print(f"{num}. {value} -> {key}")

    print("=" * 600)

    # Наполняем словарь/хэш, где ключ - урл категории, значение - массив урлов продуктов данной категории
    print("Cловарь/хэш, где ключ - урл категории, значение - список/массив урлов продуктов данной категории")
    for num, (cat_url, cat_name) in enumerate(category_urls.items(), start=1):
        product_urls = get_product_urls(get_page(cat_url))
        cat_url_prod_urls.update({cat_url: product_urls})
        print(f"{num}. {cat_url} -> {product_urls}")

    print("=" * 600)

    # записываем словарь/хэш cat_url_prod_urls в файл json
    for k, v in cat_url_prod_urls.items():
        to_json = {"Cat_url": k, "Product_urls": v}
        write_json(to_json)

    print("Создан файл -> cat_url_prod_urls.json")
    print("=" * 600)

    example_dict = {}  # словарь/хэш для передачи в ф-цию write_csv

    # заполняем словарь/хэш данными:
    # Category URL, Category name, Product URL, Unit, Price, Image
    for cat_url, prod_urls in cat_url_prod_urls.items():
        # ЕСЛИ количество товаров для категории > 0 то собираем данные,
        # ИНАЧЕ в категории нет товаров, следовательно переходим к следующей категории
        if len(prod_urls) > 0:
            for prod_url in prod_urls:
                prod_name, unit_price, image = get_product_data(get_page(prod_url))
                # ЕСЛИ для товара есть несколько видов упаковки, то для каждой упаковки собираем данные:
                # вид упаковки и стоимости ОСТАВЛЯЯ ПРЕЖНИМИ наименование товара + урл, категорию + урл и картинку
                if len(unit_price) > 1:
                    for unit, price in unit_price.items():
                        example_dict.update({"Category URL": cat_url,
                                             "Category name": category_urls[cat_url],
                                             "Product URL": prod_url,
                                             "Product name": prod_name,
                                             "Unit": unit,
                                             "Price": price,
                                             "Image": image})
                        print(example_dict["Category URL"], " | ",
                              example_dict["Category name"], " | ",
                              example_dict["Product URL"], " | ",
                              example_dict["Product name"], " | ",
                              example_dict["Unit"], " | ",
                              example_dict["Price"], " | ",
                              example_dict["Image"])

                        # На каждой итерации собираем данные по товару и дозаписываем в файл csv
                        write_csv(example_dict)
                        print("csv дозаписан!")
                        print("-" * 600)
                else:
                    example_dict.update({"Category URL": cat_url,
                                         "Category name": category_urls[cat_url],
                                         "Product URL": prod_url,
                                         "Product name": prod_name,
                                         "Unit": [unit for unit in unit_price.keys()][0],
                                         "Price": [price for price in unit_price.values()][0],
                                         "Image": image})
                    print(example_dict["Category URL"], " | ",
                          example_dict["Category name"], " | ",
                          example_dict["Product URL"], " | ",
                          example_dict["Product name"], " | ",
                          example_dict["Unit"], " | ",
                          example_dict["Price"], " | ",
                          example_dict["Image"])

                    # На каждой итерации собтраем данные по товару и дозаписываем в файл csv
                    write_csv(example_dict)
                    print("csv дозаписан!")
                    print("-" * 600)
        else:
            print(f"В данной категории {cat_url} товары отсутствуют!")
            continue

    print("#" * 600)
    print("Данные собраны!")
    print("#" * 600)


if __name__ == '__main__':
    main()

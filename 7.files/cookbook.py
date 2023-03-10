from pprint import pprint

def dict_collector(file_path):
    with open(file_path, 'r') as file_work:
        menu = {}
        for line in file_work:
            dish_name = line[:-1]
            counter = file_work.readline().strip()
            list_of_ingridient = []
            for i in range(int(counter)):
                dish_items = dict.fromkeys(['ingredient_name', 'quantity', 'measure']) # - временный словарь с ингридиетом
                ingridient = file_work.readline().strip().split(' | ') # - вот так перемещаемся по файлу
                for item in ingridient:
                    dish_items['ingredient_name'] = ingridient[0]
                    dish_items['quantity'] = ingridient[1]
                    dish_items['measure'] = ingridient[2]
                list_of_ingridient.append(dish_items)
                cook_book = {dish_name: list_of_ingridient}
                menu.update(cook_book)
            file_work.readline()

    return(menu)

dict_collector('reciepts_initial.txt')

def get_shop_list_by_dishes(dishes, persons=int):
    '''Нужно написать функцию, которая на вход принимает список блюд
    из cook_book и количество персон для кого мы будем готовить
    На выходе мы должны получить словарь с названием ингредиентов и его количества для блюда. Например, для такого вызова
    get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)
    {
  'Картофель': {'measure': 'кг', 'quantity': 2},
  'Молоко': {'measure': 'мл', 'quantity': 200},
  'Помидор': {'measure': 'шт', 'quantity': 4},
  'Сыр гауда': {'measure': 'г', 'quantity': 200},
  'Яйцо': {'measure': 'шт', 'quantity': 4},
  'Чеснок': {'measure': 'зубч', 'quantity': 6}
}
    '''
    menu = dict_collector('reciepts_initial.txt')
    print('Наше меню выглядит вот так:')
    pprint(menu)
    print()
    shopping_list = {}
    try:
        for dish in dishes:
            for item in (menu[dish]):
                items_list = dict([(item['ingredient_name'], {'measure': item['measure'], 'quantity': int(item['quantity'])*persons})])
                if shopping_list.get(item['ingredient_name']):
                    # print(f' Такое {items_list} уже есть в списке. Добавил еще')
                    extra_item = (int(shopping_list[item['ingredient_name']]['quantity']) +
                                  int(items_list[item['ingredient_name']]['quantity']))
                    # print(extra_item)
                    shopping_list[item['ingredient_name']]['quantity'] = extra_item

                else:
                    # shopping_list[item['ingredient_name']]['quantity'] *= persons
                    shopping_list.update(items_list)

        print(f"Для приготовления блюд на {persons} человек  нужно:")
        pprint(shopping_list)
    except KeyError:
        print("Такого блюда нет, проверьте ввод")


get_shop_list_by_dishes(['Омлет', 'Фахитос'], 10)
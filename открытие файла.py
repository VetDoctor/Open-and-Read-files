dish_name = 1
ing_count = 2
ingredients = 3

cook_book = {}
dish = dish_name

with open('recipes.txt', encoding='UTF-8') as file:
    for line in file:
        line = line.strip()
        if not line: continue
        if dish == dish_name:
            title = line
            cook_book[title] = []
            dish = ing_count
        elif dish == ing_count:
            count = int(line)
            dish = ingredients
        else:
            if dish == ingredients:
                data = [x.strip() for x in line.split('|')]
                data[1] = int(data[1])
                cook_book[title].append(dict(zip(('ingredient_name', 'quantity', 'measure'), data)))
                count -= 1
                if count == 0:
                    dish = dish_name
# print(cook_book)


def get_shop_list_by_dishes(dishes, person_count):
    for k, v in cook_book.items():
        if dishes.count(k) > 0:
            for i in v:
                x = {}
                x[i['ingredient_name']] = i
                del i['ingredient_name']
                for y in x.values():
                    y['quantity'] = y['quantity'] * person_count
                print(x)


get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)
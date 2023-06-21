def find_possible_combinations(items, max_weight):
    combinations = []

    def find_combinations(item_index, current_combination, current_weight):
        #Вариант с точной массой
        if current_weight == max_weight:
            combinations.append(current_combination)
            return

        if current_weight > max_weight or item_index == len(items):
            return

        item, weight = items[item_index]
        if current_weight + weight <= max_weight:
            find_combinations(item_index + 1, current_combination + [item], current_weight + weight)

        find_combinations(item_index + 1, current_combination, current_weight)

    find_combinations(0, [], 0)
    return combinations

backpack_capacity = 10
items = {
    'Телефон': 1.5,
    'Вода': 3,
    'Тушенка': 4,
    'Макароны': 2,
    'Фонарик': 1,
    'Котелок' : 2.5,
    'Нож' : 1.2,
    'Спички' : 1.3

}

items_list = [(item, weight) for item, weight in items.items()]

combinations = find_possible_combinations(items_list, backpack_capacity)
#print(combinations)
if len(combinations):
    for i,combination in enumerate(combinations, start=1):
        print(f'Вариант {i}')
        print(f'Вещи: {", ".join(item for item in combination)}')
        print(f'Общая масса: {sum(items[item] for item in combination)}')
        print('---')
else:
    print("Нет подходящих комбинаций")

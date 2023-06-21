friends = {
    'Петя': ('спальник', 'палатка', 'фонарик', 'термос'),
    'Иван': ('компас', 'палатка', 'фонарик', 'нож', 'спальник'),
    'Кристина': ('спальник', 'рюкзак', 'кружка', 'палатка','термос'),
}

common_items = set.intersection(*[set(items) for items in friends.values()])
print('Вещи, которые есть у всех:', ', '.join(common_items))

print()

all_items = set.union(*[set(items) for items in friends.values()])
unique_items = {item for item in all_items if sum(item in items for items in friends.values()) == 1}
print('Вещи которые, есть только у одного -', ', '.join(unique_items))

print()

missing_items = {}
for friend, items in friends.items():
    other_friends = {f: set(i) for f, i in friends.items() if f != friend}
    other_items = set.intersection(*other_friends.values())
    missing = other_items - set(items)
    if missing:
        missing_items[friend] = missing

for friend, items in missing_items.items():
    print(', '.join(items), '- есть у всех, кроме', friend)
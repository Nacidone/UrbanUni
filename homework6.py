my_dict = {'Юля': 1991, 'Миша': 1988, 'Николай': 1987}
print('Dict:', my_dict)
print('Existing value:', my_dict.get('Юля'))
print('Not existing value:', my_dict.get('Слава'))
deleted = my_dict.pop('Николай')
print('Deleted value:', deleted)
my_dict.update({'Cлава': 1990, 'Люба': 1993})
print('Modified dictionary:', my_dict)
my_set = {1, 'Беспилотник', 55.45, 1, 55.45, 'Беспилотник'}
print('Set:', my_set)
my_set.add('Бумеранг')
my_set.add((14, 18, 41))
my_set.remove('Беспилотник')
print('Modified set:', my_set)


my_dict = dict()
menu = {
    'Anantha':20,
    'Narayanan':21,
    'Anand':20
}

print(menu['Anand'])
print(menu.get('Anantha'))
print(menu.get('Ananth'))

print(menu.items())
print(menu.keys())
print(menu.values())

menu['Anant'] = 24
print(menu.items())

del menu['Anand']
print(menu.items())

for k,v in menu.items():
    print(f"Key: {k}")
    print(f"value: {v}")

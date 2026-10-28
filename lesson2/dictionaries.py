user = {
    'name' : 'Abdushukur',
    'surname' : 'Kalmatov',
    'city' : 'Bishkek',
    'Age' : 19,

}

print(user['name'])
print(user.get('surname'))

user['city'] = 'Leylek'
print(user['city'])

user['learning python'] = True
print(user['learning python'])

user.pop('city')

for keys, values in user.items():
    print(f"{keys}  :  {values}")
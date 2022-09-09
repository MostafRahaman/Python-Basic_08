
# simple dictionary.
car = {
    'make':'bmw',
      'model':'bw22',
      'model':2022
     }
# nested dictionary
user ={
    'name':'smith',
    'age': 30,
    'location':
        {
            'present_address':
                {
                'road':'002',
                'house':'3'
            },

            'permanent _address':'CTG'
        }
      }
#print(car['model'])

#print(user['location']['present_address']['road'])

person={
        'first_name':'Fiz',
        'last_name': 'Rahman',
        'age':'404',
        'city': 'Not Found City'
}

#print(person['city'])

favorite_color= {
    'smith': 'red',
    'kevin': 'blue',
    'devid' : 'green'
}
for name,color in favorite_color.keys():
    print(name.title())

for color in favorite_color.values():
    print(color.title())

for name,color in favorite_color.items():
    print(f"{name.title()})'s favorite color is {color.title()}.")
phone_book = {'Aleksandr': 89915256565, 'Max': 89205654747}
phone_book['Max'] = 13562456
phone_book['Anton'] = 895622221113
phone_book.update({'Sasha': 89512365656,
                   'Alex': 89041512323})
#print(phone_book.get('Kamila', 'this key not in dict'))
#print(phone_book)
#a = phone_book.pop('Anton')
#list_ = [1, 2, 3]
#list_.pop(0)
#print(list_)
#print(phone_book)
#print(a)

print(phone_book.keys())      #вывод только ключей
print(phone_book.values())      #вывод только значений
print(phone_book.items())       #вывод пар знчение/ключ
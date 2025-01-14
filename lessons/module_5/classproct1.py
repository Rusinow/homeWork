class Database:
    def __init__(self):
        self.data = {}

    def add_user(self, username, password):
        self.data[username] = password

class User:
    """
    Класс пользователя. Содержащий атрибуты: логин, пароль
    """
    def __init__(self, username, password, password_confirm ):
        self.username = username
        if password == password_confirm:
            self.password = password



if __name__ == '__main__':
    database = Database()
    while True:
        choice = int(input('Welcome! Select an action: \n1 - Login\n2 - Registration\n'))
        if choice == 1:
            login = input('Enter login: ')
            password = input('Enter password: ')
            if login in database.data:
                if password == database.data[login]:
                    print(f'login completed, {login}')
                    break
                else:
                    print('Incorrect password')
            else:
                print('User not found')
        if choice == 2:
            user = User(input('Enter login: '), password := input('Enter password: '),
                        password2 := input('Repeat password: '))
            #Здесь необходимо добавить проверку пароля на сложность
            if password != password2:
                print("Passwords don't match, please try again")
                continue
            database.add_user(user.username, user.password)

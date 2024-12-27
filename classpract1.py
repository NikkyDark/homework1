class Database:
    def __init__(self):
        self.data = {}

    def add_user(self, username, password):
        self.data[username] = password


class User:
    """
    Класс пользователя, содержащий атрибуты: логин, пароль
    """

    def __init__(self, username, password, password_confirm):
        self.username = username
        if password == password_confirm:
            self.password = password


if __name__ == '__main__':
    database = Database()
    while True:
        choice = input("Приветствую! Выберите действие: \n1 - Вход\n2 - Регистрация\n")
        if choice == 1:
            login = input("Введите логин ")
            password = input("Введите пароль ")
            if login in database.data:
                print("ok")
            else:
                print("error")
        if choice == 2:
            user = User(input('Введите логин: '), password := input('Введите пароль: '),
                        password2 := input('Повторите пароь: '))
            if password != password2:
                exit()
            database.add_user(user.username, user.password)
        print(database.data)

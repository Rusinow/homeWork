# Задание "Свой YouTube":
#from time import sleep

class User:
    def __init__(self, nickname:str, password:hash, age:int):
        self.nickname = nickname
        self.password = password.__hash__()
        self.age = age

    def __str__(self):
        return f'{self.nickname}'

class Video:
    def __init__(self, title:str, duration:int, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration

class UrTube:
    def __init__(self, users=None, videos=None, current_user=None):
        self.users = []
        self.videos = []

    def log_in(self, nickname, password):
        pass

    def register(self, nickname, password, age):
        if nickname in self.users:
            print(f'Пользователь {nickname} уже существует')
        else:
            self.nickname = User(nickname, password, age)
            self.users.append(nickname)


    def watch_video(self, nickname, password):
        pass

    def log_out(self, current_user):
        current_user = None

# Код для проверки:
ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.register('Den', '1234', 25)




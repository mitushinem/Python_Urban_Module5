from typing import Union
from time import sleep

class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age

    def get_nickname(self):
        return self.nickname

    def get_password_hash(self):
        return self.password

    def get_age(self):
        return self.age


class Video:
    def __init__(self, title: str, duration: int, time_now: int=0, adult_mode: bool=False) -> None:
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode


class UrTube:
    def __init__(self):
        self.videos: list[Video] = []
        self.users: list[User] = []
        self.current_user: Union[User, None] = None


    def log_in(self, login, password):
        """
        Метод log_in, который принимает на вход аргументы: login, password и пытается найти пользователя в users с такмими
        же логином и паролем. Если такой пользователь суещствует, то current_user меняется на найденного.
        Помните, что password передаётся в виде строки, а сравнивается по хэшу.
        """
        for user in self.users:
            if user.get_nickname() == login:
                if user.get_password_hash() == hash(password):
                    self.current_user = user
                    break
                else:
                    print(f'Неверный пароль для {login}!')
                    break
        else:
            print(f'Пользователя {login} нет в базе')

    def register(self, nickname: str, password: str, age: int) -> None:
        """
        Метод register, который принимает три аргумента: nickname, password, age,
        и добавляет пользователя в список, если пользователя не существует (с таким же nickname).
        Если существует, выводит на экран: "Пользователь {nickname} уже существует".
        После регистрации, вход выполняется автоматически.
        """
        if self.users:
            for user in self.users:
                if user.get_nickname() == nickname:
                    print(f'Пользователь {nickname} уже существует')
                    break
            else:
                self.__add_user(nickname, password, age)
        else:
            self.__add_user(nickname, password, age)

    def log_out(self):
        """
        Метод log_out для сброса текущего пользователя на None
        """
        self.current_user = None

    def __is_video_exist(self, title: str) -> bool:
        """
        Поиск по наименованию
        """
        for video in self.videos:
            if title == video.title:
                return True
        return False

    def add(self, *video: Video) -> None:
        """
        Добавление видео
        """
        for elem in video:
            if not self.__is_video_exist(elem.title):
                self.videos.append(elem)

    def get_videos(self, word_search: str) -> list[str]:
        search_list = []
        for video in self.videos:
            if word_search.lower() in video.title.lower():
                search_list.append(video.title)
        return search_list

    def watch_video(self, title: str) -> None:
        if self.current_user is not None:
            video = self.search_video(title)
            if video is not None:
                if self.current_user.get_age() > 18:
                    print('Начало видео')
                    for i in range(video.duration):
                        print(f'Продолдительность {i} из {video.duration} сек.')
                        sleep(1)
                    print('Конец видео')
                else:
                    print('Вам нет 18 лет, пожалуйста покиньте страницу')
            else:
                print('Нет такого кина')
        else:
            print('Войдите в аккаунт чтобы смотреть видео')

    def search_video(self, title: str) -> Union[Video, None]:
        for video in self.videos:
            if title.lower() == video.title.lower():
                return video
        return None

    def __add_user(self, nickname: str, password: str, age: int) -> None:
        """
        Создание нового пользователя
        """
        new_user = User(nickname, password, age)
        self.users.append(new_user)
        self.current_user = new_user


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
# ur.watch_video('Для чего девушкам парень программист?')
# ur.register('vasya_pupkin', 'lolkekcheburek', 13)
# ur.watch_video('Для чего девушкам парень программист?')
# ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
# ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')
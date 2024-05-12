from typing import Union


class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age

    def get_nickname(self):
        return self.nickname

    def get_password_hash(self):
        return self.password


class Video:
    def __init__(self, title, duration, time_now, adult_mode):
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

    def add(self, *video):
        pass

    def get_videos(self, word_search):
        pass

    def watch_video(self):
        pass

    def __add_user(self, nickname: str, password: str, age: int) -> None:
        """
        Создание нового пользователя
        """
        new_user = User(nickname, password, age)
        self.users.append(new_user)
        self.current_user = new_user


ur = UrTube()
ur.register('user1', 'paswd1', 23)
print(ur.users)
ur.register('user2', 'paswd2', 23)

print(ur.users)
print(ur.current_user.nickname)
ur.log_in('user2', '<PASSWORD>')
print(ur.current_user.nickname)
ur.log_in('user1', 'paswd1')
print(ur.current_user.nickname)

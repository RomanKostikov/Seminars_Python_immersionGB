'''
Задание №5
Доработаем задачи 3 и 4. Создайте класс проекта, который
имеет следующие методы:
загрузка данных (функция из задания 4)
вход в систему - требует указать имя и id пользователя. Для
проверки наличия пользователя в множестве используйте
магический метод проверки на равенство пользователей.
Если такого пользователя нет, вызывайте исключение
доступа. А если пользователь есть, получите его уровень из
множества пользователей.
добавление пользователя. Если уровень пользователя
меньше, чем ваш уровень, вызывайте исключение уровня
доступа.
'''
import json

from classwork.task003.task003 import AccesErorr, LevelError
from classwork.task004.task004 import User


# from Seminar_13.Task4 import  User
#
# from Seminar_13.Task3 import AccesErorr, LevelError

class UserWorkshop:
    user_list = set()

    def __init__(self):
        UserWorkshop.load_users()
        pass

    @staticmethod
    def load_users(path: str = 'users2.json'):
        with open(path, 'r', encoding='UTF-8') as f:
            user_dict = json.load(f)
        for level, user_list in user_dict.items():
            for id, name in user_list.items():
                UserWorkshop.user_list.add(
                    User(name, str(id), str(level)))  # создали объекты User и записали во множество

    def login(self, name: str,
              id: str) -> str:  # авторизация пользователя, если есть такой то возвращает уровень пользователя
        login_user = User(name, id)
        for user in UserWorkshop.user_list:
            if login_user == user:  # проверка осуществляется благодаря __eq__ и __hash__ в классе User
                # (равны когда имя и id равны)
                return user.level
        else:
            raise AccesErorr(name)  # возбуждение ошибки прописанной в модуле task3.py

    def create_user(self, name: str, id: str, level: str):  # создает пользоваетля если уровень меньше чем ваш уровень
        cur_name, cur_id = input(
            "Введите имя авторизированного пользователя и его id через пробел").split()  # авторизация пользователя
        # (который есть в базе)
        if current_level := self.login(cur_name, cur_id):  # если есть пользователь и уровень у него не 0
            if int(current_level) > int(level):
                return User(name, id,
                            level)  # создаем новго пользователя, если уровень авторизированного пользователя выше
                # уровня создаваемого пользов
            else:
                raise LevelError(current_level, level)


b = UserWorkshop()
print(b.login('Nesterov', '1'))  # (имя, id)  уровень = 5
print(b.create_user('New_user', '1',
                    '3'))  # создаст нового пользователя (имя, id, уровень) в случае если его уровень меньше,
                                # чем уровень указанного авторизированного пользователя


# код с пары
# import json
# import os
#
# from task_3 import LevelException, AccessException
#
#
# class AccessLevel:
#     @classmethod
#     def check_value(cls, value):
#         if not isinstance(value, (int, float)):
#             raise TypeError('Value must be a number')
#         if not 7 >= value >= 1:
#             raise ValueError('Value must be in range [1, 7]')
#
#     def __set_name__(self, owner, name):
#         self.name = '_' + name
#
#     def __get__(self, instance, owner):
#         return getattr(instance, self.name)
#
#     def __set__(self, instance, value):
#         self.check_value(value)
#         setattr(instance, self.name, value)
#
#
# class User:
#     access_level = AccessLevel()
#
#     def __init__(self, name: str, u_id: int, access_level: int):
#         self.name = name
#         self.access_level = access_level
#         self.u_id = u_id
#
#     def __str__(self) -> str:
#         return f'Пользователь: {self.name}, uid: {self.u_id}, уровень доступа: {self.access_level}'
#
#     def __repr__(self) -> str:
#         return f'User({self.name}, {self.u_id}, {self.access_level})'
#
#
# class UsersGroup:
#     def __init__(self, file_path):
#         self.file_path = file_path
#         self._users_data = self._get_u_data(self.file_path)
#
#     def _check_uid(self, u_id: int):
#         return u_id not in [user.u_id for user in self._users_data]
#
#     def add_user(self, u_name: str, u_id: int, u_access_level: int):
#         if self._check_uid(u_id):
#             self._users_data.append(User(u_name, u_id, u_access_level))
#         else:
#             raise AccessException('Этот uid занят!')
#
#     def save_u_data(self):
#         data = {}
#         for user in self._users_data:
#             if user.access_level not in data:
#                 data[user.access_level] = {}
#             data[user.access_level][user.u_id] = user.name
#
#         with open(self.file_path, 'w') as file:
#             json.dump(data, file, indent=2)
#
#     @staticmethod
#     def _get_u_data(file_path: str) -> dict:
#         u_data = []
#         if not os.path.exists(file_path):
#             users_data = {}
#             with open(file_path, 'w', encoding='UTF-8') as file:
#                 json.dump(users_data, file, indent=4, ensure_ascii=False)
#         else:
#             with open(file_path, 'r', encoding='UTF-8') as file:
#                 users_data = json.load(file)
#         for access_level in users_data:
#             for uid in users_data[access_level]:
#                 u_data.append(User(users_data[access_level][uid], int(uid), int(access_level)))
#
#         return u_data
#
#     def __str__(self) -> str:
#         return str(self._users_data)
#
#
# group_1 = UsersGroup('result.json')
# print(group_1)
# group_1.add_user('Alex', 1, 7)
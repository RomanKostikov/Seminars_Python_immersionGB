# Задание №6
# На семинаре 13 был создан проект по работе с
# пользователями (имя, id, уровень).
# Напишите 3-7 тестов pytest для данного проекта.
# Используйте фикстуры.

import pytest
from task004_sem_13 import User


@pytest.fixture
def user():
    return User("John Doe", "12345")


def test_user_name(user):
    assert user.name == "John Doe"


def test_user_id(user):
    assert user.user_id == "12345"


def test_user_level_default(user):
    assert user.level == "0"


def test_user_level(user):
    user = User("Jane Smith", "67890", "3")
    assert user.level == "3"

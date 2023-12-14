# Задание №4
# Создайте декоратор с параметром.
# Параметр - целое число, количество запусков декорируемой
# функции.

def decorator_with_parameter(num_runs):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(num_runs):
                result = func(*args, **kwargs)
            return result

        return wrapper

    return decorator


@decorator_with_parameter(5)
def my_function():
    print("Hello, world!")


my_function()

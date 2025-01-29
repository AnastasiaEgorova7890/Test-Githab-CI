from typing import Optional


class BadClass:
    value: str = "42"
    other_value: str = "This is the other value"  # Добавляем атрибут other_value

    def get_value(self) -> str:
        return "some_other_value"

    def compute_something(self) -> bool:
        if self.value == "42":
            return True
        else:
            return False

    def it_will_fail(self) -> str:
        # Генерация ошибки AttributeError
        raise AttributeError("This is the expected error")


def viking_cafe_order(spam: str, beans: str, eggs: Optional[str] = None) -> str:
    del beans, eggs
    return spam + spam + spam


def compute_other_thing() -> str:
    try:
        1 / 0
    except ZeroDivisionError:
        print("oops")
        return "Handled error"
    return "No error occurred"  # Добавляем возврат, если ошибка не произошла

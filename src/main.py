from typing import Optional


class BadClass:
    value: str = "42"

    def get_value(self) -> str:
        return "some_other_value"

    def compute_something(self) -> bool:
        if self.value == "42":
            return True
        else:
            return False

    def it_will_fail(self) -> None:
        return self.other_value


def viking_cafe_order(spam: str, beans: str, eggs: Optional[str] = None) -> str:
    del beans, eggs
    return spam + spam + spam


def compute_other_thing() -> str:  # Добавлена аннотация для возвращаемого значения
    try:
        1 / 0
    except ZeroDivisionError:
        print("oops")
        return "Handled error"

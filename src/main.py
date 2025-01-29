import multiprocessing
from typing import Optional

import flask

import tempfile
import sys

from third_party import (
    lib15,
    lib1,
    lib2,
    lib3,
    lib4,
    lib5,
    lib6,
    lib7,
    lib8,
    lib9,
    lib10,
    lib11,
    lib12,
    lib13,
    lib14,
)


class BadClass:
    value: str = "42"

    def get_value(self) -> str:
        return "some_other_value"

    def compute_something(self) -> bool:
        if self.value == "42":
            return True
        else:
            return False

    def it_will_fail(self):
        return self.other_value


def viking_cafe_order(spam: str, beans: str, eggs: Optional[str] = None) -> str:
    del beans, eggs
    return spam + spam + spam


def compute_other_thing():
    try:
        1 / 0
    except ZeroDivisionError:
        print("oops")
        return "Handled error"

import pytest

from src.main import BadClass, compute_other_thing, viking_cafe_order


def test_bad_class_get_value() -> None:  # Добавлена аннотация типа -> None
    bad_class_instance = BadClass()
    result = bad_class_instance.get_value()
    assert (
        result == "some_other_value"
    ), f"Expected 'some_other_value', but got {result}"


def test_bad_class_compute_something() -> None:  # Добавлена аннотация типа -> None
    bad_class_instance = BadClass()
    result = bad_class_instance.compute_something()
    assert result is True, f"Expected True, but got {result}"


def test_bad_class_it_will_fail() -> None:  # Добавлена аннотация типа -> None
    bad_class_instance = BadClass()
    with pytest.raises(AttributeError):
        bad_class_instance.it_will_fail()


def test_viking_cafe_order() -> None:  # Добавлена аннотация типа -> None
    result = viking_cafe_order("spam", "beans", "eggs")
    assert result == "spamspamspam", f"Expected 'spamspamspam', but got {result}"


def test_compute_other_thing() -> None:  # Добавлена аннотация типа -> None
    result = compute_other_thing()
    assert result == "Handled error", f"Expected 'Handled error', but got {result}"

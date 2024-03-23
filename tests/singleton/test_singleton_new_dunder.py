import pytest

from dduda.snippets.singleton.singleton_dunder import SingletonNewDunder


def singleton_factory() -> SingletonNewDunder:
    return SingletonNewDunder()


@pytest.fixture()
def singleton_new_dunder() -> SingletonNewDunder:
    yield singleton_factory()


@pytest.fixture()
def singleton_second_instance() -> SingletonNewDunder:
    yield singleton_factory()


def test_singleton_initialization(singleton_new_dunder: SingletonNewDunder) -> None:
    assert singleton_new_dunder is not None, "Instance should be created"


def test_singleton_created_twice_is_same_object(
    singleton_new_dunder: SingletonNewDunder,
    singleton_second_instance: SingletonNewDunder,
) -> None:
    assert (
        singleton_new_dunder is singleton_second_instance
    ), "Instances should be the same"

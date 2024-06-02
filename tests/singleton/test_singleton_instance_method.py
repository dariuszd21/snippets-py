import pytest
from dduda.snippets.singleton.singleton_method import SingletonInstanceMethod


def singleton_factory() -> SingletonInstanceMethod:
    return SingletonInstanceMethod.instance()


@pytest.fixture()
def singleton_new_dunder() -> SingletonInstanceMethod:
    yield singleton_factory()


@pytest.fixture()
def singleton_second_instance() -> SingletonInstanceMethod:
    yield singleton_factory()


def test_singleton_initialization(
    singleton_new_dunder: SingletonInstanceMethod
) -> None:
    assert singleton_new_dunder is not None, "Instance should be created"


def test_singleton_created_twice_is_same_object(
    singleton_new_dunder: SingletonInstanceMethod,
    singleton_second_instance: SingletonInstanceMethod,
) -> None:
    assert (
        singleton_new_dunder is singleton_second_instance
    ), "Instances should be the same"


def test_singleton_cannot_be_directly_instantiated() -> None:
    with pytest.raises(NotImplementedError):
        SingletonInstanceMethod()

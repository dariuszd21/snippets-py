from typing import Type, Union

import pytest
from dduda.snippets.singleton.singleton_decorator import SingletonDecorator


@SingletonDecorator
class DecoratedTestClassSingleton:
    """Class required for testing."""


@SingletonDecorator()
class DecoratedTestClassSingletonWithoutArgs:
    """Class required for testing."""


@pytest.fixture(
    params=[DecoratedTestClassSingleton, DecoratedTestClassSingletonWithoutArgs]
)
def singleton_factory(
    request
) -> Type[DecoratedTestClassSingleton] | Type[DecoratedTestClassSingletonWithoutArgs]:
    return request.param


@pytest.fixture()
def singleton_new_dunder(
    singleton_factory: Type[DecoratedTestClassSingleton]
    | Type[DecoratedTestClassSingletonWithoutArgs],
) -> Union[DecoratedTestClassSingleton, DecoratedTestClassSingletonWithoutArgs]:
    yield singleton_factory()


@pytest.fixture()
def singleton_second_instance(
    singleton_factory: Type[DecoratedTestClassSingleton]
    | Type[DecoratedTestClassSingletonWithoutArgs],
) -> Union[DecoratedTestClassSingleton, DecoratedTestClassSingletonWithoutArgs]:
    yield singleton_factory()


def test_singleton_initialization(
    singleton_new_dunder: DecoratedTestClassSingleton
) -> None:
    assert singleton_new_dunder is not None, "Instance should be created"


def test_singleton_created_twice_is_same_object(
    singleton_new_dunder: DecoratedTestClassSingleton,
    singleton_second_instance: DecoratedTestClassSingleton,
) -> None:
    assert (
        singleton_new_dunder is singleton_second_instance
    ), "Instances should be the same"

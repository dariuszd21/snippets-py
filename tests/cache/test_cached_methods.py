from dduda.snippets.cache.cached_methods import ClassWithCachedFunctions

import pytest


def instance_factory() -> ClassWithCachedFunctions:
    return ClassWithCachedFunctions()


@pytest.fixture()
def instance_one() -> ClassWithCachedFunctions:
    yield instance_factory()


@pytest.fixture()
def instance_two() -> ClassWithCachedFunctions:
    yield instance_factory()


@pytest.fixture(autouse=True)
def clear_cache(instance_one, instance_two):
    instance_one.class_method_one.cache_clear()
    instance_two.class_method_one.cache_clear()

    instance_one.method_one.cache_clear()
    instance_two.method_one.cache_clear()


def test_cached_classmethod_called_once(instance_one, instance_two) -> None:
    instance_one.class_method_one()
    instance_two.class_method_one()
    ClassWithCachedFunctions.class_method_one()

    cache_info = ClassWithCachedFunctions.class_method_one.cache_info()

    assert cache_info.hits == 2
    assert cache_info.misses == 1


def test_cached_method_called_twice_for_different_instances(
    instance_one, instance_two
) -> None:
    instance_one.method_one()
    instance_two.method_one()

    cache_info = ClassWithCachedFunctions.method_one.cache_info()

    assert cache_info.hits == 0
    assert cache_info.misses == 2


def test_cached_method_called_once_for_same_instance(instance_one) -> None:
    instance_one.method_one()
    instance_one.method_one()

    cache_info = ClassWithCachedFunctions.method_one.cache_info()

    assert cache_info.hits == 1
    assert cache_info.misses == 1

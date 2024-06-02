import pytest
from dduda.snippets.cache.cached_functions import (
    DEFAULT_INT_ARG,
    DEFAULT_STR_ARG,
    cached_function,
    cached_function_with_default_args,
)


@pytest.fixture(autouse=True)
def clear_cache() -> None:
    cached_function.cache_clear()
    cached_function_with_default_args.cache_clear()


def test_function_called_only_once() -> None:
    """Cache result is correctly re-used if function called twice."""
    cached_function()
    cached_function()
    cache_info = cached_function.cache_info()
    assert cache_info.misses == 1
    assert cache_info.hits == 1


def test_function_called_twice_if_default_arguments_in_use() -> None:
    """Default function arguments are not recognized by cache."""
    expected_result = f"{DEFAULT_STR_ARG}: {DEFAULT_INT_ARG}"
    assert cached_function_with_default_args() == expected_result
    assert (
        cached_function_with_default_args(DEFAULT_INT_ARG, DEFAULT_STR_ARG)
        == expected_result
    )
    cache_info = cached_function_with_default_args.cache_info()
    assert cache_info.hits == 0
    assert cache_info.misses == 2

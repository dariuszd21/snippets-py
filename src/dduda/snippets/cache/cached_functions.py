from functools import lru_cache

DEFAULT_INT_ARG = 5
DEFAULT_STR_ARG = "text"


@lru_cache(maxsize=1)
def cached_function() -> None:
    return None


@lru_cache(maxsize=1)
def cached_function_with_default_args(
    int_arg: int = DEFAULT_INT_ARG, str_arg: str = DEFAULT_STR_ARG
) -> str:
    return f"{str_arg}: {int_arg}"

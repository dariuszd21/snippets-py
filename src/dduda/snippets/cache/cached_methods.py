from functools import lru_cache


class ClassWithCachedFunctions:
    @lru_cache(maxsize=1)
    def method_one(self) -> None:
        """Method that does nothing."""

    @classmethod
    @lru_cache(maxsize=1)
    def class_method_one(cls) -> None:
        """Class method that does nothing."""

from functools import lru_cache


class ClassWithCachedFunctions:
    def __init__(self) -> None:
        self.method_two = lru_cache(maxsize=1)(self._method_two)

    @lru_cache(maxsize=1)  # noqa: B019 (cached-instance-method)
    def method_one(self) -> None:
        """Method that does nothing.

        Problem with caching method is that, cache state size is shared
        between all the instances.
        """

    @classmethod
    @lru_cache(maxsize=1)
    def class_method_one(cls) -> None:
        """Class method that does nothing."""

    def _method_two(self) -> None:
        """Method two implementation that will be cached per instances."""

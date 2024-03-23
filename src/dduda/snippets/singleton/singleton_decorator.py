from typing import Any, Optional


class SingletonDecorator:
    """Singleton implementation based on class-decorator.

    It may be used both with and without arguments.
    @SingletonDecorator
    class SomeClass:
        pass

    or

    @SingletonDecorator()
    class SomeClass:
        pass

    """

    def __init__(self, cls: Optional[Any] = None) -> "SingletonDecorator":
        self._cls = cls
        self._instance = None

    def __call__(self, cls: Optional[Any] = None) -> None:
        # Check if called with or without arguments
        if self._cls is not None:
            cls = self._cls

        # Create single instance if not available yet
        if self._instance is None:
            self._instance = cls.__new__(cls)
        cls.__new__ = lambda c: self._instance
        return cls

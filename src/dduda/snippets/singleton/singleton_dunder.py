from typing import Optional


class SingletonNewDunder:
    """Class that represents singleton implementation via __new__ overload."""

    __instance: Optional["SingletonNewDunder"] = None

    def __new__(cls) -> "SingletonNewDunder":
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

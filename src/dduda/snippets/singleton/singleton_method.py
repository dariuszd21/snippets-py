from typing import Optional


class SingletonInstanceMethod:
    """Singleton implementation using instance() method."""

    __instance: Optional["SingletonInstanceMethod"] = None

    def __new__(cls) -> "SingletonInstanceMethod":
        raise NotImplementedError("Cannot instantiate this class.")

    @classmethod
    def instance(cls) -> "SingletonInstanceMethod":
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

from pathlib import Path


class PathConfigMeta(type):
    def __init__(cls, *args, **kwargs):
        cls.__base = Path(__file__).resolve().parent

    @property
    def root(cls) -> Path:
        return cls.__base

    @property
    def log(cls) -> Path:
        return cls.root / "logs"


class PathConfig(metaclass=PathConfigMeta):
    pass

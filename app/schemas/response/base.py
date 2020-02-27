from abc import ABC, abstractmethod
from typing import Union


class Base(ABC):
    @abstractmethod
    def serialize(self) -> Union[dict, list]:
        pass

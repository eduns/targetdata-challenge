from abc import ABC, abstractmethod
from typing import TypeVar

T = TypeVar('T')

class BaseController(ABC):
    @abstractmethod
    def handle(input: object) -> T:
        pass
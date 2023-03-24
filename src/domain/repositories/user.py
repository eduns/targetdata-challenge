from abc import ABC, abstractmethod
class UserRepository(ABC):
    @abstractmethod
    def get(criteria: dict) -> dict:
        pass

    @abstractmethod
    def add(user_data: dict) -> None:
        pass
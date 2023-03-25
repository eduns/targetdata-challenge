from abc import ABC, abstractmethod

from ..entities.LocaleForecast import LocaleForecast

class ForecastRepository(ABC):
    @abstractmethod
    def get_forecast(locale_cep: str) -> LocaleForecast:
        pass
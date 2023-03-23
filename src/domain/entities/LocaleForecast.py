class LocaleForecast():
    def __init__(self, locale_data: dict, forecast_data: dict) -> None:
        self.locale = locale_data
        self.forecast = forecast_data
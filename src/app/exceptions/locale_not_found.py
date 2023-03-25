class LocaleNotFound(Exception):
    def __init__(self, locale_cep: str) -> None:
        self.message = f'locale with cep {locale_cep} not found'
        super().__init__(self.message)
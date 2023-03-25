class MissingParams(Exception):
    def __init__(self, missing_params: list[str]) -> None:
        self.message = f'missing params: {", ".join(missing_params)}'
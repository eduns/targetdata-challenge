class UserNotFound(Exception):
    def __init__(self, username: str) -> None:
        self.message = f'user {username} not found'
        super().__init__(self.message)
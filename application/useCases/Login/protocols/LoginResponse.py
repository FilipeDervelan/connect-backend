class LoginResponse:
    def __init__(self, success: bool, user: str = None):
        self.success = success
        self.user = user

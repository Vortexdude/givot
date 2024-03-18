
class GitInit:

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.base_url = 'https://api.github.com'
        self.headers = {}
        self._init_headers()

    def _init_headers(self):
        self.api_version = '2022-11-28'
        self.authorization = f'Bearer {self.password}'
        self.headers.update(
            {
                "Authorization": self.authorization,
                "X-GitHub-Api-Version": self.api_version
            }
        )

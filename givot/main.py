import os
import requests
from core.branch_ops import BranchOperation

GIT_TOKEN = os.getenv('GIT_TOKEN', 'Nothing')
USER_NAME = os.getenv('GIT_USERNAME', 'vortexdude')


class GitHub:

    def __init__(self, username, password):
        self.branch_ops = BranchOperation(username=username, password=password)

    def branches(self, owner: str = None, repo: str = None) -> list:
        """Some documentation"""

        return self.branch_ops.get_branches(owner=owner, repo=repo)

from givot.core import GitInit
import requests


class BranchOperation(GitInit):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def get_branches(self, owner: str = None, repo: str = None) -> list:
        if repo is None:
            raise Exception("Please provide the Repo first")

        if owner is None:
            owner = self.username

        _url = self.base_url + f'/repos/{owner}/{repo}/branches'
        res = requests.get(_url, self.headers).json()
        return [i['name'] for i in res if i['name']]

    def rename_branch(
            self,
            owner: str = None,
            repo: str = None,
            old_branch: str = None,
            new_branch: str = None
    ):
        self.headers.update({'Content-Type': 'application/x-www-form-urlencoded'})
        url = self.base_url + f'/repos/{owner}/{repo}/branches/{old_branch}/rename'
        data = {"new_name": new_branch}
        response = requests.post(url=url, headers=self.headers, data=data)
        if response.status_code == 201:
            return response.json()
        elif response.status_code == 404:
            return {"Error": "You Entered something wrong"}
        else:
            return {"Error": "Connectivity problem, contact to Admin"}

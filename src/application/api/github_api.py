import requests

class GithubAPI:
  def __init__(self) -> None:
    pass
    
  def search_repository(self, repository : str):
    response = requests.get(url=f'https://api.github.com/search/repositories?q={repository}')
    data = response.json()

    return data['total_count'], response


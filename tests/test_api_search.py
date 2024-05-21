def test_check_number_of_repos(github_api):
  """
      Summary: check API to search number of reposositories with certain name
      steps:
          1. Send API request to find the repository
          2. Analyse the response

      Expected result:
          number of found repos == SOMENUMBER
  """
  
  # 1. Send API request to find the repository
  repo_numbers, response = github_api.search_repository("AQA Academy")

  # 2. Analyse the response
  response.raise_for_status()

  assert repo_numbers == 27
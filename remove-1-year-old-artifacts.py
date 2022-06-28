def remove_artifacts():

    import requests

    base_url = ''

    headers = {
        'content-type': 'text/plain',
        'X-JFrog-Art-Api': ''
    }

    data = 'items.find({"repo":"repoName", "name":{"$match":"repoNameToMatch"}, "created":{"$before": "1y"}})'

    response = requests.post(base_url+'api/search/aql', headers=headers, data=data)

    for result in eval(response.text)["results"]:
        artifact_url = base_url + result['repo'] + '/' + result['name']
        # requests.delete(artifact_url, headers=headers)
        print("removed ->" + artifact_url)

        # removing from trash can
        trash_artifact_url = base_url + result['repo'] + '/api/trash/clean/' + result['name']
        # requests.delete(trash_artifact_url, headers=headers)
        print("=>" + trash_artifact_url)


if __name__ == '__main__':
    remove_artifacts()


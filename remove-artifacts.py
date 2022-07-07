import sys

repo_name = sys.argv[1]
item_name = sys.argv[2]
ARTIFACTORY_API_KEY = sys.argv[3]

def getVersion(artifact_name):
    item_name_stripped = item_name.strip('-')
    return artifact_name.replace(item_name_stripped, '').split('-')[1]

def getYear(artifact_created):
    return int(artifact_created.split("-")[0])

def remove_artifacts():

    import requests

    base_url = 'https://artifactory.coxautoinc.com/artifactory/'

    headers = {
        'content-type': 'text/plain',
        'X-JFrog-Art-Api': ARTIFACTORY_API_KEY
    }

    data = 'items.find({"repo":"%s", "name":{"$match":"%s-*"}}).sort({"$desc" : ["name"]})' % (repo_name, item_name)

    response = requests.post(base_url+'api/search/aql', headers=headers, data=data)

    RELEASES_NUMBER_TO_KEEP = 10
    YEAR_TO_REMOVE = 2020

    artifacts = set()
    artifact_removed_list = [] # at least 10 releases

    # CONDITION: keep last 10 release helm artifacts and then only delete 2020 and older helm artifacts
    for result in eval(response.text)["results"]:
        artifact_name = result['name']
        artifact_created = result['created']
        artifact_version = getVersion(artifact_name)

        if (artifact_version in artifacts):
            artifacts.add(artifact_version)
        elif (len(artifacts) < RELEASES_NUMBER_TO_KEEP):
            artifacts.add(artifact_version)
        elif (getYear(artifact_created) <= YEAR_TO_REMOVE):
            artifact_removed_list.append(result)
        else:
            artifacts.add(artifact_version)

    for artifact in artifact_removed_list:
        artifact_url = base_url + artifact['repo'] + '/' + artifact['name']
        # requests.delete(artifact_url, headers=headers)
        print(artifact_url)

        # removing artifacts from trash can
        trash_artifact_url = base_url + artifact['repo'] + '/api/trash/clean/' + artifact['name']
        # requests.delete(trash_artifact_url, headers=headers)


if __name__ == '__main__':
    remove_artifacts()

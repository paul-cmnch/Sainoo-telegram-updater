import requests
import json
import sainoo_telegram


# Opens saved postings and put their ids in the ids_json list
with open('/home/paul/Python_projects/sainoo_postings.json', 'r') as json_file:
    posting_list = json.load(json_file)
ids_json = []
for i in posting_list:
    ids_json.append(i['id'])

response = requests.get('https://www.sainoo.com/api/v1/board/jobs')

postings = json.loads(response.text)['data']['entities']
for posting in postings:
    CurrentPostingDict = {
        'id': posting['id'],
        'companyname': posting['company']['name'],
        'positiontitle': posting['position_title'],
        'postcode': posting['office']['postcode'],
        'city': posting['office']['city'],
        'country': posting['office']['country'],
        'postingtype': posting['experiences'],
        'deadline': posting['deadline'],
        'jobfunctions': f"posting['job_functions']",
        'industry': posting['company']['industry'],
        'logolink': posting['company']['logo'],
        'joblink': f"https://www.sainoo.com/jobs/{posting['id']}"
    }
    if CurrentPostingDict['id'] not in ids_json:
        posting_list.append(CurrentPostingDict)
        print(f"{CurrentPostingDict['id']} was added in the json")
        sainoo_telegram.send(CurrentPostingDict)
    else:
        print(f"{CurrentPostingDict['id']} was already present in the json")


with open('/home/paul/Python_projects/sainoo_postings.json', 'w') as json_file:
    json.dump(posting_list, json_file, indent=4)

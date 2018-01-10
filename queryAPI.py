import requests

def req(command, qry='', )

#auth = ',\'ajoiner\', \'Lis@1676\''
#url = 'http://camgian.atlassian.net/rest/api/latest/'
#qry = 'http://camgian.atlassian.net/rest/api/latest/search?jql=labels+%3D+RIF+AND+resolution+%3D+Unresolved', auth=('ajoiner', 'Lis@1676')
resp = requests.get('http://camgian.atlassian.net/rest/api/latest/search?jql=labels+%3D+RIF+AND+resolution+%3D+Unresolved', auth=('ajoiner', 'Lis@1676'))
print(resp.url)
print(resp.status_code)
ans = resp.json()
print(ans['total'])
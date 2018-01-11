import requests
import time

def yearly_total_req(issueType, year):
    yrDiff = time.localtime(time.time()).tm_year
    if (year < yrDiff):
        yrDiff = str(year - yrDiff)
    query = 'Type%20%3D%20' + issueType + '%20And%20Status%20in%20(Resolved%2C%20Completed)%20AND%20resolutiondate%20%3E%3D%20startOfYear(' + yrDiff + ')%20AND%20resolutiondate%20%3C%3DendOfYear(' + yrDiff + ')'
    r = 'http://camgian.atlassian.net/rest/api/latest/search?jql=' + query
    return r

#auth = ',\'ajoiner\', \'Lis@1676\''
resp = requests.get(yearly_total_req('Bug', 2017), auth=('ajoiner', 'Lis@1676'))
print(resp.url)
print(resp.status_code)
ans = resp.json()
print(ans['total'])
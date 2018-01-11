import sys
import time
import requests

def yearly_total_req(issueType, wantedYr):
    #Get current year
    wantedYr = int(wantedYr)
    yrDiff = time.localtime(time.time()).tm_year
    if (wantedYr < yrDiff):
        #Calculate year offset for query
        yrDiff = str(wantedYr - yrDiff)
    #Compile to query to return
    query = 'Type%20%3D%20' + issueType + '%20And%20Status%20in%20(Resolved%2C%20Completed)%20AND%20resolutiondate%20%3E%3D%20startOfYear(' + yrDiff + ')%20AND%20resolutiondate%20%3C%3DendOfYear(' + yrDiff + ')'
    r = 'http://camgian.atlassian.net/rest/api/latest/search?jql=' + query
    return r

def main():
    #Get username, password, and year from cmd line
    usrName = sys.argv[1]
    passWrd = sys.argv[2]
    year = sys.argv[3]

    issues = ['Story', '"New Feature"', 'Task', 'Improvement', 'Bug']

    for x in issues:
        #Submit request to Jira API store in resp
        resp = requests.get(yearly_total_req(x, year), auth=(usrName, passWrd))
        #print(resp.status_code)
        #store response json in and to access json structure
        ans = resp.json()
        print('Number of {} issues for {}: {}'.format(x, year, ans['total']))
    return 0

if __name__=='__main__':
    sys.exit(main())
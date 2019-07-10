from django.shortcuts import render, HttpResponse
import requests
import json
import time


"""Hello Analytics Reporting API V4."""



''' comment out unti i figure this shit out !!!!!



from apiclient.discovery import build
from oauth2client.service_account import ServiceAccountCredentials


SCOPES = ['https://www.googleapis.com/auth/analytics.readonly']
KEY_FILE_LOCATION = 'vaulted-cove-243420-c134c79707df.json'
VIEW_ID = '106424670'



def initialize_analyticsreporting():
  """Initializes an Analytics Reporting API V4 service object.

  Returns:
    An authorized Analytics Reporting API V4 service object.
  """
  credentials = ServiceAccountCredentials.from_json_keyfile_name(KEY_FILE_LOCATION, SCOPES)

  # Build the service object.
  analytics = build('analyticsreporting', 'v4', credentials=credentials)

  return analytics



def get_report(analytics):
  """Queries the Analytics Reporting API V4.

  Args:
    analytics: An authorized Analytics Reporting API V4 service object.
  Returns:
    The Analytics Reporting API V4 response.
  """
  return analytics.reports().batchGet(
      body={
        'reportRequests': [
        {
          'viewId': VIEW_ID,
          'dateRanges': [{'startDate': '7daysAgo', 'endDate': 'today'}],
          'metrics': [{'expression': 'ga:sessions'}],
          'dimensions': [{'name': 'ga:country'}]
        }]
      }
  ).execute()



def print_response(response):
  """Parses and prints the Analytics Reporting API V4 response.

  Args:
    response: An Analytics Reporting API V4 response.
  """
  
  for report in response.get('reports', []):
    columnHeader = report.get('columnHeader', {})
    dimensionHeaders = columnHeader.get('dimensions', [])
    metricHeaders = columnHeader.get('metricHeader', {}).get('metricHeaderEntries', [])

    for row in report.get('data', {}).get('rows', []):
      dimensions = row.get('dimensions', [])
      dateRangeValues = row.get('metrics', [])

      for header, dimension in zip(dimensionHeaders, dimensions):
        print(header + ': ' + dimension)

      for i, values in enumerate(dateRangeValues):
        print('Date range: ' + str(i))
        for metricHeader, value in zip(metricHeaders, values.get('values')):
          print(metricHeader.get('name') + ': ' + value)


def main():
  analytics = initialize_analyticsreporting()
  response = get_report(analytics)
  print_response(response)


if __name__ == '__main__':
  main()


comment out unti i figure this shit out !!!!! ''' 


from oauth2client.service_account import ServiceAccountCredentials

# The scope for the OAuth2 request.
SCOPE = 'https://www.googleapis.com/auth/analytics.readonly'

# The location of the key file with the key data.
KEY_FILEPATH = 'app/vaulted-cove-243420-c134c79707df.json'

# Defines a method to get an access token from the ServiceAccount object.
t = ServiceAccountCredentials.from_json_keyfile_name(KEY_FILEPATH, SCOPE).get_access_token().access_token

access_token = # token here


print('*******************************')
print(t)
print('*******************************')

def avg_session_dur():
    jsonList = []
    x = 'https://www.googleapis.com/analytics/v3/data/ga?ids=ga%3A160650493&start-date=30daysAgo&end-date=yesterday&metrics=ga%3AavgSessionDuration&access_token=' + access_token
    print('*******************************')
    print(x)
    print('*******************************')
    y = requests.get(x)

    jsonList.append(json.loads(y.content))
    
    for data in jsonList:
        z = data['rows']

    z_form = float(z[0][0])
    z_form = round(z_form)

    return 'Average session duration:  ' + time.strftime('%H:%M:%S', time.gmtime(z_form))


def amount_of_sessions():
    jsonList2 = []
    x2 = 'https://www.googleapis.com/analytics/v3/data/ga?ids=ga%3A160650493&start-date=30daysAgo&end-date=yesterday&metrics=ga%3Asessions&access_token=' + access_token
    print('*******************************')
    print(x2)
    print('*******************************')   
    y2 = requests.get(x2)

    jsonList2.append(json.loads(y2.content))
    
    for data in jsonList2:
        z2 = data['rows']
    
    z2_form = z2[0][0]

    return 'Amount of sessions:  ' + z2_form


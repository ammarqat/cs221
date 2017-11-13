import requests
import json
# import urllib.request

# urllib.request.urlopen("http://example.com/foo/bar").read()
outfile = open('data.txt', 'w')

result = requests.get("https://api.propublica.org/congress/v1/both/votes/1991/01.json", 
			headers={"X-API-Key":"6hihyZvzLmrhy2ArFVvKc3BLTO6srDuHE2SdLh6d"})
try:
	print result.json()['results']['votes']
except(ValueError):
	print ValueError
	print("Oops!  That was no valid number.  Try again...")


# for year in range(1990, 2018):
# 	for month in range(1, 13):
# 		monthString = '%02d' % month
# 		result = requests.get("https://api.propublica.org/congress/v1/both/votes/"+str(year)+"/"+monthString+".json", 
# 			headers={"X-API-Key":"6hihyZvzLmrhy2ArFVvKc3BLTO6srDuHE2SdLh6d"})
# 		try:
# 			json.dump(result.json()['results']['votes'], outfile)
# 		except:
# 			print("Oops! Couldn't print " + str(year) + ", " + monthString)

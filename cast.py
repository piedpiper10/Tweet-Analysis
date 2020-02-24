import csv
ret="RT"
#l=['reptherealm']
#l=['cast','interaction','fan','photos','hosts','competitions']
l=['celebrity','publicity','show','actor','actress','hollywood']
#l=['promo','visual','trailer','music','teaser','theme','soundtrack','audio']
with open('GameofThrones1.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        	tweet=row[2]
		tweet=tweet.lower()
		if any(search in tweet for search in l):
				print row[2],"\t",row[4]

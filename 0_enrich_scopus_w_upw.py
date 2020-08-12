import pandas as pd
import requests, json

def get_upw_info(doi):
	#print(f"https://api.oadoi.org/v2/{doi}?email=m@larri.eu")
	r = requests.get(f"https://api.oadoi.org/v2/{doi}?email=m@larri.eu")
	pb = ""

	try : 
		res = r.json()
	except : 
		pb = "pb in upw answer"

	if res.get("message") and "isn't in Unpaywall" in res.get("message") :
		pb = "not in upw"

	isOa = 1 if res.get('is_oa') else 0
	repo = publisher = 0
	if res.get('oa_locations') : 
		for loc in res.get('oa_locations') :
			if loc['host_type'] == 'repository' : repo = 1
			if loc['host_type'] == 'publisher' : publisher = 1

	return {
	'is_oa': isOa,
	'repo' : repo,
	'publisher' : publisher,
	'pb' : pb
	}



separate_df = (pd.read_csv(str(y)+"_scopus.csv") for y in range(2014,2018))
df = pd.concat(separate_df, ignore_index=True)
print(f"nb of publications\t{len(df)}\n")

#convert DOI column to string
df['DOI'] = df['DOI'].astype(str) 

for nb, row in enumerate(df.itertuples()):
		
	if not row.DOI.startswith('10.') : continue
	
	#test DOI non présent dans upw
	#upw_info = get_upw_info("10.4324/9781315079042-8")
	#upw_info = get_upw_info("10.13154/tosc.v2020.iS1.262-294")
			
	print(row.DOI)
	upw_info = get_upw_info(row.DOI)

	for field in upw_info:
		df.at[row.Index, field] = upw_info[field]

	if nb > 5600 : break
	if nb % 50 == 0 : 
		print(f">> {round(nb/len(df)*100,2)} % treated")


# by default pandas write in float, next line convert float to int
cols = ['is_oa', 'repo', 'publisher']
df[cols] = df[cols].astype('Int64') 

df.to_csv("00_scopus_upw.csv",index=False)



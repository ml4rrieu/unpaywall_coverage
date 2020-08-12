import pandas as pd
import requests, json


## first step add hal value
df = pd.read_csv("scopus_upw.csv")
print(f"{len(df)} publications")
df_not_oa = df.loc[df['is_oa'] == 0]
print(f"{len(df_not_oa)} publis not oa")
print(f"{round(len(df_not_oa)/len(df)*100)} % publis not oa") 


halDoiError = []
for i, row in enumerate(df_not_oa.itertuples()):
	
	r = requests.get(f"https://api.archives-ouvertes.fr/search/?q=doiId_s:{row.DOI}&fl=submitType_s")
	try :
		res = r.json()
	except : 
		print(f"\n\nerror while formating hal answer to json{r}\n\n")
		halDoiError.append(row.DOI)
		continue

	res = res['response'].get('docs', [])
	halfile = False
	for item in res : 
		if item['submitType_s'] == 'file' : 
			halfile = True
			break

	if halfile : 
		df.at[row.Index, 'notoa_in_upw_but_in_hal'] = 1

	if i % 50 == 0  : 
		print(f"{round(i/len(df_not_oa)*100)} % treated")
	#if i > 100 : break


df.to_csv("scopus_upw_hal.csv",index=False)

if halDoiError : 
	print('\n--halDoiError')
	[print(doi) for doi in halDoiError]
	print('\n\n')

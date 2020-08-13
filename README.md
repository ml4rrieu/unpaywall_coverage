## Context
This is a pursuit of a work made by Aaron Tay [_Open Access Indicators and the importance of optimising your Institutional repository for discovery in Unpaywal_](https://musingsaboutlibrarianship.blogspot.com/2020/08/open-access-indicators-and-importance.html) <br/>
In 2020 Open Access indicators at institution level are growing  ([see for example CWTS Leiden Ranking 2020](https://www.leidenranking.com/ranking/2020/list) ). Most of them are using [unpaywall](unpaywall.org) to know if a publication is open access or not. <br/>
The goal here is to represent the limits of unpaywall. 


Steps : 
1. get bibliographic data from Scopus (or something else)
2. run and adapt _0_enrich_scopus_w_upw.py_ to get open access status for each publications
3. run and adapt _1_compare_w_hal.py_ to compare with HAL repository
4. run and adapt _2_draw_graphics.py_ to represent what cannot be treated with unpaywall 


## Results
#### 1. Reproducing Aaron works : Where unpaywall say "this publications are closed" can I find an open access version in my Institutionnal Repository ? 
At first, 16 publications were concerned<br/>
![](https://pbs.twimg.com/media/Ee52FmGWAAAApzF?format=png&name=small)

However, after a manal verification only 2 publications were really in that case <br/><br/>
DOI | Problem
------------ | -------------
10.1016/j.respe.2017.03.133	| embargo forever
10.1016/j.jtemb.2016.11.006	| embargo forever
10.1007/s10552-016-0832-4	| embargo forever
10.1016/j.spinee.2013.08.017	| embargo forever
10.1136/jnnp-2013-306799	| embargo forever
10.1016/j.vaccine.2014.11.045	| embargo forever
10.1016/j.bulcan.2016.06.005 |	embargo forever
10.4230/LIPIcs.STACS.2016.52	| isn't in Unpaywall
10.1002/pssc.201700181	| isn't in Unpaywall
10.4074/S0761898017002072	| isn't in Unpaywall
10.1002/2015GL066170	| loaded 3 August
10.1002/2016GL070620	| loaded 3 August
10.1002/2017GL074353	| loaded 3 August
10.1088/2041-8205/807/2/L29	| loaded 5 August
10.1016/j.ijepes.2014.07.064	| upw missed it
10.1038/nature23266	| upw missed it

#### 2. How much pubications cannot be treated by unpaywall ? 
(upw can treat 'only' publication with a Crossref DOI)<br/>
From the 5597 publications finded in Scopus 4% cannot be treated with Unpaywall<br/>

![](https://pbs.twimg.com/media/EfNzPuXWoAIO6OE?format=jpg&name=medium)

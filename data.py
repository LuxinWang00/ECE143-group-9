
import pandas as pd
import geopandas as gpd
import numpy as np
import matplotlib.pyplot as plt
#%%
bib = pd.read_csv('Bible.csv')
his = pd.read_csv('History.csv')
law = pd.read_csv('law.csv')
tra = pd.read_csv('Travel.csv')
sci = pd.read_csv('Science.csv')
tec = pd.read_csv('Technology_Engineering.csv')
#%%
label=[bib,sci,his,law,tec,tra]
categories = ['Bible','Science','History','Law','Technology Engineering','Travel']
color_set = ['salmon','orange','gold','palegreen','turquoise','deepskyblue']

#%%
name = []
for i in range(len(tec)):
    name.append('Technology Engineering')
tec['Category'] = pd.Series(name)
#%%
total = [bib[:189],sci[:190],his[:190],law[:190],tec[:190],tra[:190]]
total = pd.concat(total)
total.index = np.arange(0,len(total))
#%%
ran = []
for i in range(len(total['price'])):
    if total['price'][i] < 50:
        ran.append(total['Category'][i])
df = pd.Series(k for k in ran)
df = df.groupby(df).size()

fig, ax = plt.subplots()
def func(pct, allvals):
    absolute = int(pct/100.*np.sum(allvals))
    return "{:.1f}%".format(pct, absolute)

wedges, texts, autotexts = ax.pie(df, autopct=lambda pct: func(pct, df.values),textprops=dict(color="black"),
                                   colors=color_set,startangle=160,pctdistance=1.1,labeldistance=1.5)

#ax.legend(wedges, categories,loc=("center left"), bbox_to_anchor=(1, 0, 0.5, 1))
ax.set_title('Price(<50)')
ax.axis('equal')
plt.show()
#%%
ran = []
for i in range(len(total['price'])):
    if 50 < total['price'][i] < 100:
        ran.append(total['Category'][i])
df2 = pd.Series(k for k in ran)
df2 = df2.groupby(df2).size()
fig2, ax2 = plt.subplots()
def func(pct, allvals):
    absolute = int(pct/100.*np.sum(allvals))
    return "{:.1f}%".format(pct, absolute)

wedges, texts, autotexts = ax2.pie(df2, autopct=lambda pct: func(pct, df2.values),textprops=dict(color="black"),
                                   colors=color_set,startangle=160,pctdistance=1.1,labeldistance=1.5)

#ax2.legend(wedges, categories,loc=("center left"), bbox_to_anchor=(1, 0, 0.5, 1))
ax2.set_title('Price(50~100)')
ax2.axis('equal')
plt.show()
#%%
ran = []
for i in range(len(total['price'])):
    if 100 < total['price'][i]:
        ran.append(total['Category'][i])
df3 = pd.Series(k for k in ran)
df3 = df3.groupby(df3).size()
fig3, ax3 = plt.subplots()
def func(pct, allvals):
    absolute = int(pct/100.*np.sum(allvals))
    return "{:.1f}%".format(pct, absolute)

wedges, texts, autotexts = ax3.pie(df3, autopct=lambda pct: func(pct, df3.values),textprops=dict(color="black"),
                                   colors=color_set,startangle=160,pctdistance=1.1,labeldistance=1.5)

ax3.legend(wedges, categories,loc=("center left"), bbox_to_anchor=(1, 0, 0.5, 1))
ax3.set_title('Price(>100)')
ax3.axis('equal')
plt.show()

#%%
world = geopandas.read_file(geopandas.datasets.get_path('naturalearth_lowres'))
cities = geopandas.read_file(geopandas.datasets.get_path('naturalearth_cities'))

#%%
bib['publish date'] =pd.to_datetime(bib['publish date'])
new_year = []
for i in bib['publish date']:
    i.to_pydatetime()
    i = i.year
    new_year.append(i)
bib['year'] = pd.Series(np.array(new_year))
bib = bib.sort_values(by='year', ascending=True)
kk = pd.value_counts(bib['year'].values, sort=False)
bibb = bib.groupby('year').size()
#%%
his['publish date'] =pd.to_datetime(his['publish date'])
new_year = []
for i in his['publish date']:
    i.to_pydatetime()
    i = i.year
    new_year.append(i)
his['year'] = pd.Series(np.array(new_year))
his = his.sort_values(by='year', ascending=True)
kk = pd.value_counts(bib['year'].values, sort=False)
hiss = his.groupby('year').size()
#%%
sci['publish date'] =pd.to_datetime(sci['publish date'])
new_year = []
for i in his['publish date']:
    i.to_pydatetime()
    i = i.year
    new_year.append(i)
sci['year'] = pd.Series(np.array(new_year))
sci = his.sort_values(by='year', ascending=True)
kk = pd.value_counts(sci['year'].values, sort=False)
scii = his.groupby('year').size()
#%%
law['publish date'] =pd.to_datetime(law['publish date'])
new_year = []
for i in law['publish date']:
    i.to_pydatetime()
    i = i.year
    new_year.append(i)
law['year'] = pd.Series(np.array(new_year))
law = his.sort_values(by='year', ascending=True)
kk = pd.value_counts(law['year'].values, sort=False)
laww = his.groupby('year').size()
#%%
tec['publish date'] =pd.to_datetime(tec['publish date'])
new_year = []
for i in tec['publish date']:
    i.to_pydatetime()
    i = i.year
    new_year.append(i)
tec['year'] = pd.Series(np.array(new_year))
tec = his.sort_values(by='year', ascending=True)
kk = pd.value_counts(bib['year'].values, sort=False)
hiss = his.groupby('year').size()
import requests
from pprint import pprint
import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter

r = requests.get('http://api.worldbank.org/countries/swe/indicators/SP.POP.TOTL?format=json&per_page=100')
data = r.json()
#pprint(data)

pop = data[1]

pop_per_country = {}
for entry in pop:
    country_id = entry['country']['id']
    if country_id in pop_per_country:
        pop_per_country[country_id][entry['date']] = entry['value']
    else:
        pop_per_country[country_id] = {}

#pprint(pop_per_country)

x=[]
y=[]
for year, value in pop_per_country['SE'].items():
    x.append(int(year))
    y.append(int(value))

pprint(x)
pprint(y)

fig, ax = plt.subplots()

ax.fill_between(x, 7484656, y)
ax.grid(True, zorder=5)
ax.set_ylabel('Total population SE')
ax.set_xlabel('Year')
ax.set_title('')
plt.show()

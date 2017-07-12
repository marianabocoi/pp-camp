import requests
from pprint import pprint
import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter

r = requests.get('http://api.worldbank.org/countries/swe;esp/indicators/SP.POP.TOTL?format=json&per_page=1000')
data = r.json()
# pprint(data)

pop = data[1]

pop_per_country = {}
for entry in pop:
    country_id = entry['country']['id']
    if country_id in pop_per_country:
        pop_per_country[country_id][entry['date']] = entry['value']
    else:
        pop_per_country[country_id] = {}

# pprint(pop_per_country)

x_se = []
y_se = []
for year, value in pop_per_country['SE'].items():
    x_se.append(int(year))
    y_se.append(int(value))

x_es = []
y_es = []
for year, value in pop_per_country['ES'].items():
    x_es.append(int(year))
    y_es.append(int(value))
pprint(x_es)
pprint(x_se)
fig, ax = plt.subplots()

# line-plot

fig, ax = plt.subplots()
line1, = ax.plot(x_se, y_se, '--', color='teal', linewidth=2,
                 label='Sweden Popiulation yearly growth')

line2, = ax.plot(x_es, y_es, ',:', color='orange', linewidth=2,
                 label='Spain Popiulation yearly growth')

ax.legend(loc='best')
ax.set_xlabel('Year')
ax.set_ylabel('Total population')
ax.set_title('Comparison')

plt.show()



# fill-plot
# ax.fill_between(x, 7484656, y)
# ax.grid(True, zorder=5)
# ax.set_ylabel('Total population SE')
# ax.set_xlabel('Year')
# ax.set_title('')
# plt.show()

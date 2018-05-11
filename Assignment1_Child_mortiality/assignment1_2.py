#2. graph the under-five mortality rates as above, but for 2015.
import csv
import plotly as py 
import plotly.graph_objs as go
survey = open('WHOSIS_MDG_000003.csv')
read_survey = csv.reader(survey)

date = []
country = []
mortaliy_rate = []
filter_mortality_rate = []

for row in read_survey:
    if row[1] == '2015':
        date.append(row[1])
        country.append(row[0])
        mortaliy_rate.append(row[4])

for m_r in mortaliy_rate:
    i = m_r.split()
    # print i[0] 
    filter_mortality_rate.append(i[0])

filter_mortality_rate.sort(key=lambda x: (float(x), len(x)))
print filter_mortality_rate
trace1 = go.Scatter(
     x = country,y = filter_mortality_rate, name='For 2015'
)

layout = dict(title = 'Under five mortality rate for 2015',
                xaxis = dict(title = 'Country'),
                yaxis= dict(title = 'UnderFive Mortality rate'),
)

data = [trace1]
fig = dict(data = data, layout = layout)
# print fig
py.offline.plot(fig, filename='mortaility rate for 2015')
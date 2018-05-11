#3. choose three representative countries in different areas of the world,
# then create a line graph showing the trends in under-five mortality in
# those countries over the years from 1990 to 2015.
import csv
import plotly as py 
import plotly.graph_objs as go
survey = open('WHOSIS_MDG_000003.csv')
read_survey = csv.reader(survey)


for row in read_survey:
    print row[1]
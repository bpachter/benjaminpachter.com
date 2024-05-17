import plotly.express as px
import pandas as pd
from fredapi import Fred

# Replace with your FRED API key
fred = Fred(api_key='b6846d3d5b062fb26dc43c8f344db268')
plotlyapi = '1XJ9nfpq7C7mkXaI46Jg'

# Fetch data
data = fred.get_series('UNRATE')
df = pd.DataFrame(data, columns=['Unemployment Rate'])
df.reset_index(inplace=True)
df.columns = ['Date', 'Unemployment Rate']

# Create a Plotly chart
fig = px.line(df, x='Date', y='Unemployment Rate', title='US Unemployment Rate')

# Save to your Plotly account
import chart_studio
chart_studio.tools.set_credentials_file(username='bpachter', api_key= plotlyapi)
import chart_studio.plotly as py
py.plot(fig, filename='us-unemployment-rate', auto_open=True)


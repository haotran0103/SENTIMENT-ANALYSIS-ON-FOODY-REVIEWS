import dash
from dash import dcc, html
import pandas as pd
import plotly.express as px

df = pd.read_csv('dataset.csv')

app = dash.Dash(__name__)

sentiment_counts = df['category'].value_counts()

fig = px.pie(values=sentiment_counts, names=['Positive', 'Negative'], title="Sentiment Distribution")

app.layout = html.Div([
    html.H1("Sentiment Analysis Dashboard"),
    
    dcc.Graph(figure=fig),
    
    html.H3("Sample Data"),
    dash.dash_table.DataTable(
        data=df.sample(10).to_dict('records'), 
        columns=[{'name': i, 'id': i} for i in df.columns]
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)

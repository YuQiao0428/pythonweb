
import dash
import dash_html_components as html

app = dash.Dash(__name__)

app.layout = html.Div(
    html.H1('Hello python page...')
)

if __name__ == '__main__':
    #app.run_server(debug=False)
    app.run_server(debug=True, port=80) 
    # or whatever you choose
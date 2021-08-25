import pandas as pd

CSV = pd.read_csv('/Users/dansp/Desktop/Book1.csv')
CSV.to_html('/Users/dansp/Desktop/test_html.html')
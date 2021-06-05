import os

data_url = "https://www.fca.org.uk/publication/data/short-positions-daily-update.xlsx"

root_dir = os.path.dirname(os.path.abspath(__file__))
data_dir = os.path.join(root_dir, 'data_store')

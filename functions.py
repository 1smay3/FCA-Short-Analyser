import datetime
import pandas as pd

from config import data_dir


def _validate(date_string):
    try:
        datetime.datetime.strptime(date_string, '%d.%m.%Y')
    except ValueError:
        raise ValueError("Incorrect data format, should be DD.MM.YYYY")


def read_pickle(date):
    _validate(date)
    return pd.read_pickle(data_dir + '/disclosures ' + date + '.pickle')

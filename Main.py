import pandas as pd
import numpy as np
import openpyxl
import requests

try :
    bajajFinanceDF = pd.read_html ()

except Exception as e :

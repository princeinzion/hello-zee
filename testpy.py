import numpy as np
import jinja2
import matplotlib as plt

import csv
data_file = "C:/Users/MTzion/Documents/PyLearn/worldincome.csv"
with open(data_file, 'r') as csvfile:
	reader = csv.DictReader(csvfile)
	data = list(reader)

	len(data)

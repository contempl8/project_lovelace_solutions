import os
here=os.path.abspath(os.path.dirname(__file__))
data_dir=os.path.dirname(here)+'/data/'
os.chdir(data_dir)

import csv

with open('mei.ext_index.txt') as csvfile:
    reader = csv.reader(csvfile, delimiter='	')
    next(reader, None)  # skip the header line
    data={}
    for line in reader:
        floats=[]
        for num in line[1:]:
            floats.append(float(num))
        data[line[0]]=floats


def enso_classification(year):
    classification = ''
    intensity = ''
    year_data=data[str(year)]
    mei=(0,0)
    for idx, d_pnt in enumerate(year_data):
        if abs(d_pnt) > mei[1]:
            mei=(idx,abs(d_pnt))
    mei=year_data[mei[0]]
    if mei >= 0.5: classification='El Nino'
    elif mei <= -0.5: classification='La Nina'
    else: classification = 'Neither'
    if abs(mei) >= 0.5 and abs(mei) < 1.0: intensity = 'weak'
    elif abs(mei) >= 1.0 and abs(mei) < 1.5: intensity = 'moderate'
    elif abs(mei) >= 1.5 and abs(mei) < 2.0: intensity = 'strong'
    elif abs(mei) >= 2.0: intensity = 'very strong'
    else: intensity = 'none'

    return classification, intensity

print(enso_classification(2016))
print(enso_classification(1996))
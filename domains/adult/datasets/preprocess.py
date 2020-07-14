import os
import csv

labels_0 = ['<=50k', '>50k']
labels_workclass = ['private', 'self-employed', 'government', 'without-pay']
labels_4 = ['married-civ-spouse', 'divorced', 'never-married', 'separated', 'widowed', 'married-spouse-absent', 'married-af-spouse']
labels_5 = ['tech-support', 'craft-repair', 'other-service', 'sales', 'exec-managerial', 'prof-specialty', 'handlers-cleaners', 'machine-op-inspct', 'adm-clerical', 'farming-fishing', 'transport-moving', 'priv-house-serv', 'protective-serv', 'armed-forces']
labels_6 = ['wife', 'own-child', 'husband', 'not-in-family', 'other-relative', 'unmarried']
labels_7 = ['white', 'asian-pac-islander', 'amer-indian-eskimo', 'other', 'black']
labels_8 = ['female', 'male']

def remove_attributes(row, indices):
    for i in indices:
        del row[i]
    return row

def has_missing(row):
    return '?' in row

def merge_similar(row):
    if row[2] == 'Self-emp-inc' or row[2] == 'Self-emp-not-inc':
        row[2] = 'self-employed'
    elif row[2] == 'Federal-gov' or row[2] == 'Local-gov' or row[2] == 'State-gov':
        row[2] = 'government'
    elif row[2] == 'Never-worked':
        row[2] = 'without-pay'
    return row

def normalize_names(row):
    return [x.lower() for x in row]

def label_encoder(row):
    row[0] = str(labels_0.index(row[0]))
    row[2] = str(labels_workclass.index(row[2]))
    row[4] = str(labels_4.index(row[4]))
    row[5] = str(labels_5.index(row[5]))
    row[6] = str(labels_6.index(row[6]))
    row[7] = str(labels_7.index(row[7]))
    row[8] = str(labels_8.index(row[8]))
    return row

def preprocess(filename, dest):
    data = []
    with open(filename) as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        row_number = 0
        for row in reader:
            row_number = row_number + 1
            if row_number == 1:
                continue
            row = remove_attributes(row, [14, 4, 3])
            if has_missing(row):
                continue
            row = merge_similar(row)
            row = normalize_names(row)
            row = label_encoder(row)
            data.append(row)

    with open(dest, 'w', newline=None) as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        writer.writerow(['# {} {}'.format(len(data), len(data[0]) - 1)])
        for row in data:
            writer.writerow(row)
        os.system('dos2unix {}'.format(dest))



preprocess('training-set.csv', 'training-set-preprocessed.csv')
preprocess('test-set.csv', 'test-set-preprocessed.csv')

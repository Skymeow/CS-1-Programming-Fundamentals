import csv

virus_list = {}

with open('data.csv', 'r') as csvfile:
    i = 0
    csv_reader = csv.reader(csvfile)
    for disease in csv_reader:
        if i > 1:
            fatality = disease[1]
            for index, character in enumerate(fatality):
                if character == "%":
                    fatality = float(fatality[:index])
            repr_rate = float(disease[2])
            virus_list[disease[0]] = [fatality, repr_rate]
        i += 1
    return(virus_list)

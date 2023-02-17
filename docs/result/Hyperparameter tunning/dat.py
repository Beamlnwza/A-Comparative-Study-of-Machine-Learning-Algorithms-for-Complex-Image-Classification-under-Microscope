import csv
import os
# specify the input and output file names

PATH = os.path.join(os.getcwd(), 'docs/result/Hyperparameter tunning/')


input_file = PATH + 'Hyperparameter.csv'
output_file = PATH + 'Hyperparameter_l.csv'

with open(input_file, 'r') as input_csv:
    # read the CSV file
    reader = csv.reader(input_csv)

    with open(output_file, 'w', newline='') as output_csv:
        # create a CSV writer
        writer = csv.writer(output_csv)

        for row in reader:
            # replace empty cells with "-"
            row = [cell if cell != "" else "-" for cell in row]
            # write the modified row to the output file
            writer.writerow(row)
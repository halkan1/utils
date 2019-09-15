import csv
import json

# Use Argparse to accept file from command line

def csvTojson(csv_file):
    with open(csv_file,'r') as input_file:
        reader = csv.DictReader(input_file)
        result = json.dumps([row for row in reader], indent=4)
    return result

print(csvTojson('test.csv'))

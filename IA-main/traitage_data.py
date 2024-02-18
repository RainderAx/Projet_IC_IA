import json
import csv

with open('data_dist.json', 'r') as f:
    data_dist = json.load(f)

sensor_data = data_dist['sensor']

with open('donee.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Distance', 'Value'])

    for key, value in sensor_data['us'].items():
        distance = value.get('Distance')
        sensor_value = value.get('value')
        writer.writerow([distance, sensor_value])



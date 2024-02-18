import json
import csv

with open('data_dist.json', 'r') as f:
    data_dist = json.load(f)


sensor_data = data_dist['sensor']

with open('output.csv', 'w', newline='') as f:

     writer = csv.writer(f)

     writer.writerow(['Distance', 'Value'])

     for key, value in sensor_data['us'].items():
        # key est l'identifiant unique, value est un dictionnaire contenant les données de chaque capteur
        distance = value.get('Distance')
        time = value.get('Time')
        sensor_value = value.get('value')
        
        writer.writerow([distance, value])


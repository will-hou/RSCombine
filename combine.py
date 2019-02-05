import argparse
import os

import json

parser = argparse.ArgumentParser()
parser.add_argument('-a', '--a',
                    help="the path to the first JSON file. The new JSON data will be made in the same directory",
                    type=str)
parser.add_argument('-b', '--b', help="the path to the second JSON file", type=str)

args = parser.parse_args()

try:
    with open(args.a, 'r') as file_path_1, open(args.b, 'r') as file_path_2:
        data_1 = json.load(file_path_1)
        data_2 = json.load(file_path_2)
        print(file_path_1, '\n', file_path_2)
except json.decoder.JSONDecodeError:
    print("Invalid JSON file! Make sure your file is a true JSON file")
    exit()

new_data = data_1

for (team_key, team) in data_2['teams'].items():
    for scout in team:
        if team_key not in new_data['teams']:
            new_data['teams'][team_key] = [scout]
        elif scout not in new_data['teams'][team_key]:
            new_data['teams'][team_key].append(scout)

newpath = "{}/{}_{}_combined.json".format(os.path.dirname(args.a), os.path.basename(args.a).split('.')[0],
                                          os.path.basename(args.b).split('.')[0])

print(newpath)

with open(newpath, 'w') as outfile:
    json.dump(new_data, outfile)
    print("Successfully created {}".format(newpath))

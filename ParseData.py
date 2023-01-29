"""
How to get CSV file:
Go to https://www.google.com/maps/d/u/0/viewer?mid=1cEAhNHqp82AXABF8qU7k6sRFI4392V0e&ll=39.86977160553247%2C-104.379495&z=10, click on 3 vertical dots then click "copy map", click 3 dots for "layer options" then click "export data" then select "CSV"

Important links:
- http://www.coemergency.com/p/fire-bans-danger.html
- maps: https://www.google.com/maps/d/u/0/viewer?mid=1cEAhNHqp82AXABF8qU7k6sRFI4392V0e&ll=39.86977160553247%2C-104.379495&z=10
https://www.crummy.com/software/BeautifulSoup/bs4/doc/
"""

import csv

def parse_data():
  restrictions = []
  
  county_data = [
    # {"name": "adams", "restriction": False},
    # {"name": "park", "restriction": True},
    # {"name": "teller county", "restriction": False}
  ]
  
  with open("restrictions.csv") as f:
    reader = csv.reader(f, delimiter = ",")
    for line in reader:
      if len(line) == 3:
        restrictions.append(line[1:3])
  
  temp_list = []
  
  counter = 0
  for restriction in restrictions:
    # print(restriction)
    # if counter % 2 == 0:
    #   temp_list.append(restriction)
    # counter += 1
    if "Colorado" not in restriction[1]:
      temp_list.append(restriction)
  restrictions = [x for x in temp_list]
  
  for restriction in restrictions:
    if restriction[1][0:2].lower() == "no":
      dictionary = {"name": restriction[0], "restriction": False}
      county_data.append(dictionary)
    else:
      remove = {"name": restriction[0],                "restriction": True}
      county_data.append(remove)
  
  return county_data


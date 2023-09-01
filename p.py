# lst =[[2,3,4],3,4,[9,10,[9]],8]
# new = " "
# for i in lst:
#     if type(i) == list:
#         ele=str(i)
#         new+=ele.replace('[',' ')
#     elif type(i)== int:
#         new+=str(i)

# x = new.replace(']',' ')
# print(x)


# lst =[[2,3,4],3,4,[9,10,[9]],8]     
# new_list=[]
# for item in lst :
#     if isinstance (item ,int):
#         new_list.append(item)
#     else:
#         for j in item:
#             new_list.append(j)
# print(new_list)
     
 
# [2, 3, 4, 3, 4, 9, 10, 9, 8]

# data = {
#     "ID State": "04000US01",
#     "State": "Alabama",
#     "ID Year": 2019,
#     "Year": "2019",
#     "Population": 4876250,
#     "Slug State": "alabama",
    
# }

# print(data)

import datetime

def generate_unique_id():
    current_datetime = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    order_number = current_datetime 
    return order_number


def generate_key(data_entry):
    for key, val in data_entry.items():
        if not key:
            return generate_unique_id()
    return None

csv_path = "C:\\Users\\narsimhac\\Downloads\\convertcsv (1).csv"

with open(csv_path, "r") as file:
    lines = file.readlines()

header = lines[0].strip().split(",")

for line in lines[1:]:
    values = line.strip().split(",")
    data_entry = {}

    for i, column_name in enumerate(header):
        data_entry[column_name] = values[i]
    
    # data_entry[''] = ''

    key = generate_key(data_entry)
    if key:
        data_entry[key] = data_entry.pop('')
    data_entry[''] = ''

    print(data_entry)
            

 
 


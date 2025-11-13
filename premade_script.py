premade_list = []

raw_data = open("premade_safe.txt", "r")
read_data = raw_data.read()
entities = read_data.split("/x1E")
for entity in entities:
    if len(entity) >= 3:
        print(entity.split("/x1F"))
        premade_list.append(entity.split("/x1F"))
raw_data.close()

print(premade_list)

def save_data():
    raw_data = open("premade_safe", "w")
    raw_data.write
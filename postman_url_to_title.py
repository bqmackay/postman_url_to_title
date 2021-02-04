import json

filename = input("Postman filename path (relative to this program's location): ")

try:
    with open(filename) as file:
         data = json.load(file)
except:
    print(f"the file {filename} could not be opened")

def updateItemTitles(items):
    for item in items:
        if "item" in item:
            updateItemTitles(item["item"])
        elif "name" in item and "request" in item:
            item["name"] = item["request"]["url"]["raw"]

updateItemTitles(data["item"])

with open(filename, "w") as file:
    json.dump(data, file)

print(f"Conversion of \"{filename}\" is complete. You can now import the file into Postman.")

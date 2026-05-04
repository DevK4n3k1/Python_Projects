##############################################
# Read the whole JSON
##############################################
import json
with open("app_config.json", "r", encoding="utf-8") as f:
    data = json.load(f)

print(data)    
print(data["features"])     # specific data


##############################################
# Create/overwrite a JSON file
##############################################
payload = {
    "store": {"products": []},
    "last_update": "2025-10-06"
}
with open("data.json", "w", encoding="utf-8") as f:
    json.dump(payload, f, indent=4, ensure_ascii=False)


##############################################
# Update (read → update → write)
##############################################
with open("data.json", "r", encoding="utf-8") as f:
    data = json.load(f)
    data["features"][2] = "export"

with open("data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)



##############################################
# Append (read → append → write)
##############################################
with open("data.json", "r", encoding="utf-8") as f:
    data = json.load(f)
    data["features"].append("export") 

with open("data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)



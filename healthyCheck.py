mport json
#json formatted string
new_data = """
{
  "Status": "Healthy",
  "Checks": [
    {
      "Name": "Connections",
      "Status": "Healthy"
    },
    {
      "Name": "ConnectionRead",
      "Status": "unHealthy"
    },
    {
      "Name": "redis",
      "Status": "Healthy"
    },
    {
      "Name": "ProcessCheck",
      "Status": "Healthy"
    },
    {
      "Name": "UserProfile",
      "Status": "unHealthy"
    },
    {
      "Name": "features",
      "Status": "unHealthy",
      "Description": "sample sample sample"
    },
    {
      "Name": "shutdown",
      "Status": "Healthy"
    },
    {
      "Name": "lifespan",
      "Status": "unHealthy"
    }
  ]
}

"""

#currently a multiline string in json format
print(type(new_data))

#loads is a function that deserializes the json string to a dictionary
#different from loads as loads uses a file like object
dictionaryData = json.loads(new_data)
#print type to double check
print(type(dictionaryData))


def statusCheck(data): 
  total, total1, total2 = 0 
  for mainKey, value in data.items():
      if value == "Healthy" or "unHealthy":
        total1+=1
  for check in data["Checks"]:
        print(f"check : {check}")
  total = total1 + total2
  return total



print("*******Break****")


print(statusCheck(dictionaryData))
print("New line")


"""Practice with dictionaries"""

ice_cream: dict[str, int] = {"chocolate": 12, "vanilla": 8, "strawberry": 5}

#Adding
ice_cream["mint"] = 3     
print("after adding mint:")
print(ice_cream)

#removing
ice_cream.pop("mint")
print("After removing mint:")
print(ice_cream)

#Accessing
print(f"Number of vanilla orders {ice_cream['vanilla']}.")

#Updating a value
ice_cream["mint"] += 1
print("Adding one to vanilla.")
print(ice_cream)

#Checking if in dictionary
print("mint" in ice_cream)
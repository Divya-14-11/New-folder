dictionary1={"name":"Divya","age":15,"school":"kv"}
print(dictionary1["school"])
dictionary1["city"]="miao"
print(dictionary1)
dictionary1.pop("age")
print(dictionary1)
print(f"city:{dictionary1.get("city")}")
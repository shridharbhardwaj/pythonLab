# a= {}
# b= set()
# print(a,type(a))
# print(b,type(b))


dict1 = {"good": "Something pleasant", "fetch": "to bring", "1": "The number 1"}
marks = {"Harsh": 34, "Shree": 98, "Shivam": 93, "Smriti": 45, "Naina": 23, "Sankalp": 55}

print(dict1["good"])
print(marks["Shree"])

marks["Priyanka"] = 34
print(marks)

print(marks.get("Priyanka Chopra"))
print(marks.get("Priyanka"))
# print(marks.get("Priyanka Chopra")) #This will save you from getting error and give "None"
print(marks["Priyanka"])
print(marks.keys())
print(marks.values())
print(marks.items())
print(marks.pop("Shree"))
print(marks)
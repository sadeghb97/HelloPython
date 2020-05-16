#tarif ba acolad
#key value structure

dict1 = {"name": "Sadegh", "last_name": "Bagherzadeh"}
print(dict1)

#yek key mitavanad do bar tekrar shavad vali dovomi lahaz khahad shod
dict2 = {"name": "Mehdi", "last_name": "Javedani", "name": "Reza"}
print(dict2)

#size an moteghayyer ast va be sadegi maitavan be an item ezafe kard
dict2['age'] = 40;
print(dict2)

#joda kardane key az value ha
print(dict2.keys())
print((list) (dict2.keys()))
print(dict2.values())

del dict2['name']
print(dict2)
import json

person = '{"name":"Rafi", "language":["English","Python"]}'

person_dic=json.loads(person)
print(person_dic)

print(person_dic['language'])
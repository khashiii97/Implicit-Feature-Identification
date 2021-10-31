import json
dictionary = {}
postings = []
with open('auxiliary-files/postings.txt','r',encoding='utf-8') as f:
    for line in f.read().split('\n')[:-1]:
        postings.append(json.loads(line))
print(postings)
with open('auxiliary-files/dictionary.txt','r',encoding='utf-8') as f:
    dictionary = json.loads(f.read())
print(dictionary)
opinions = []
aspects = []
with open('auxiliary-files/ops.txt', 'r',encoding='utf-8') as f:
    for opinion in f.read().split('\n')[:-1]:
        opinions.append(opinion)


with open('auxiliary-files/aspects.txt', 'r',encoding='utf-8') as f:
    for aspect in f.read().split('\n')[:-1]:
        aspects.append(aspect)
print(aspects)
R = 8411 #number of reviews
rules = {} #opinion to list of aspects
Oi = {} #opinion to number of times it occurred in reviews
for opinion in dictionary.keys():
    Oi[opinion] = 0
    for aspect in postings[dictionary[opinion]].keys():
        Oi[opinion] += postings[dictionary[opinion]][aspect]
for opinion in dictionary.keys():
    opinion_rules = []

    for aspect in postings[dictionary[opinion]].keys():
        support_score = postings[dictionary[opinion]][aspect]/R
        if support_score > 0.0005:
            confidence = postings[dictionary[opinion]][aspect]/Oi[opinion]
            if confidence > 0.005:
                opinion_rules.append(aspects[int(aspect)])
    if opinion_rules:
        rules[opinion] = opinion_rules
text = ''
for opinion in rules.keys():
    text += opinion + " : " + str(rules[opinion]) +'\n'
with open('../Results/Rules.txt','w',encoding='utf-8') as wr:
    wr.write(text)







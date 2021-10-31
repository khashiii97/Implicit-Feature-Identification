import os
import xml.etree.ElementTree as ET
import re
from src.Utils import *
import json
""""
this file extracts the co-occurrence matrix mentioned in the paper. although we will not construct the matrix since it will be
quite sparse. dus, we'll create an inverted index with the dictionary the opinion words and the index comprising lists of features.
"""
test = []
opinion_words = set()
aspect_words = []
dictionary = {}# a dictionary with key being opinion words and value the index of that word in the posting list
postings = []
adverbs = []
R = 0 #number of reviews
with open('auxiliary-files/adverbs.txt', 'r', encoding='utf-8') as in_file:
    adverbs = in_file.read().split("\n")
aspect_words_index = {}#key : feature word value: index
main_path = "data/main/"
bad_tars = ['بهتر','برتر','بيشتر','دسترس','شاتر','باتری']
for path in os.listdir(main_path):
    full_path = os.path.join(main_path, path)
    if os.path.isfile(full_path) and full_path.endswith(".xml"):
        # print(full_path)
        with open(full_path,encoding="utf8") as file:
            sentences = {}  # (sentence_id, sentence text)
            sentences = {}  # (sentence_id, sentence text)
            root_aspects = {} # (element_id, aspect)
            tag_to_aspect ={} # {(target(i).tag,element_id)
            root = ET.parse(full_path).getroot()
                #getting all sentences and putting them in the sentence dictionary
            for sentence in root.iter('Sentence'):
                sentences[sentence.attrib['ID']] = sentence.text
                R += 1
            target_Ms =[]
            target_Is = []
            opinions = []
            for tag in root.iter('Tag'):
                if tag.attrib['Type'] == 'Target(M)': #aspects
                    target_Ms.append(tag)
                if tag.attrib['Type'] == 'Target(I)': #aspects
                    target_Is.append(tag)
                if tag.attrib['Type'] == 'Opinion':  # opinions:
                    opinions.append(tag)

            for tag in target_Ms:
                if tag.attrib['Type'] == 'Target(M)':  # aspects
                    feature = extract_aspect_root(tag.attrib['Root'])
                    if feature not in aspect_words_index.keys():
                        aspect_words_index[feature] = len(aspect_words)
                        aspect_words.append(feature)
                    root_aspects[tag.attrib['ID']] = feature
            for tag in target_Is:
                tag_to_aspect[tag.attrib['ID']] = tag.attrib['Relation']
            for tag in opinions:
                coordinate = re.split('[ \[,\]]+', tag.attrib['Coordinate'])
                target_id = tag.attrib['Relation']
                # if full_path == 'data/main/Acer Aspire E1-531-B9602G50Maks.xml' and tag.attrib['ID'] == 'tagID10090':
                #     print("hoooo")
                #     print(coordinate[2])
                #     print(coordinate[3])
                #     print(coordinate[1])
                #     print(sentences[coordinate[1]])
                #     print(sentences[coordinate[1]][int(coordinate[2]):int(coordinate[3])])

                opinion = sentences[coordinate[1]][int(coordinate[2]):int(coordinate[3])]
                # before = opinion
                opinion = opinion_root_extractor(opinion)

                # if len(opinion) < 2:
                #     print(opinion)
                #     print(before)
                #     print(tag.attrib['ID'])
                #     print(full_path)
                #     print("heyyy")

                # if 'ترین' in opinion:
                #     flag = False
                #     for tar in bad_tars:
                #         if tar in opinion:
                #             flag = True
                #             break
                #     if flag!= True:
                #         opinion = opinion[:opinion.index('ترین')]
                # if 'ترين' in opinion:
                #     flag = False
                #     for tar in bad_tars:
                #         if tar in opinion:
                #             flag = True
                #             break
                #     if flag != True:
                #         opinion = opinion[:opinion.index('ترين')]
                # if opinion.enswith('تر'):
                #     opinion = opinion[0:-2]
                if opinion != '':
                    opinion_words.add(opinion)
                    aspect_tag_id = tag_to_aspect[target_id]
                    aspect = root_aspects[aspect_tag_id]
                    if opinion in dictionary.keys():
                        if aspect_words_index[aspect] in postings[dictionary[opinion]].keys():
                            postings[dictionary[opinion]][aspect_words_index[aspect]] += 1
                        else:
                            postings[dictionary[opinion]][aspect_words_index[aspect]] = 1

                    else:
                        postings.append({aspect_words_index[aspect] : 1})
                        dictionary[opinion] = len(postings) - 1
import random
def show():
    opwords = list(opinion_words)
    for i in range(5):
        index = random.randint(0,len(opinion_words))
        print(opwords[index])
        index = dictionary[opwords[index]]
        output = []
        for p in postings[index]:
            output.append(aspect_words[int(p)])
        print(output)
        print("****")

# print(opinion_words)
# print(aspect_words)
opinion_words = list(opinion_words)
with open('auxiliary-files/ops.txt', 'w',encoding='utf-8') as f:
    for opinion in sorted(list(opinion_words)):
        f.write(str(opinion))
        f.write("\n")


with open('auxiliary-files/aspects.txt', 'w',encoding='utf-8') as f:
    for aspect in sorted(list(aspect_words))[:-1]:
        f.write(str(aspect))
        f.write("\n")
with open('auxiliary-files/dictionary.txt','w',encoding = 'utf-8') as f:
    f.write(json.dumps(dictionary))
with open('auxiliary-files/postings.txt', 'w',encoding='utf-8') as f:
    for posting in postings:
        f.write(json.dumps(posting))
        f.write("\n")
# print(len(opinion_words))
show()
#print(R) 8411
# for word in opinion_words:
#     if  'درست' in word:
#         print(word)


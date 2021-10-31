lexicon = set() # a lexicon consisting of all terms in the reviews except stopwords
from src.Utils import *
stop_words_list = []
import os
for path in os.listdir('../StopWords/'):
    full_path = os.path.join('../StopWords/', path)
    if os.path.isfile(full_path) and full_path.endswith(".txt"):
        with open(full_path, 'r', encoding='utf-8') as in_file:
            words = in_file.read().split('\n')
            for word in words:
                stop_words_list.append(word)
with open('auxiliary-files/slang_verbs.txt','r', encoding='utf-8') as in_file:
    words = in_file.read().split('\n')
    for word in words:
        stop_words_list.append(word)
split_token = '@@@'
POS_tags = [] #POS tags of each token in a sentence
with open('auxiliary-files/POS-tags.txt', 'r', encoding='utf-8') as in_file:
    strings = in_file.read().split(split_token)
    for i in range(len(strings) - 1):
        POS_tags.append(eval(strings[i]))


aspect_Bs = []
aspect_Is = []
with open('auxiliary-files/aspect-Bs.txt', encoding='utf-8') as in_file:
    strings = in_file.read().split(split_token)
    for i in range(len(strings) - 1):
        aspect_Bs.append(eval(strings[i]))
with open('auxiliary-files/aspect-Is.txt', encoding='utf-8') as in_file:
    strings = in_file.read().split(split_token)
    for i in range(len(strings) - 1):
        aspect_Is.append(eval(strings[i]))
features = set()
for i,POS_tag in enumerate(POS_tags):
    #finding aspects
    #aspects will be added to the lexicon as a complete word
    for begining in aspect_Bs[i]:
        word_to_be_added = POS_tag[begining][0]
        #finding the continious parts of that aspect
        j = 0
        for j in range(len(aspect_Is[i])):
            if aspect_Is[i][j] == begining + 1:
                break
        if j < len(aspect_Is[i]):
            while True:
                word_to_be_added += ' ' + POS_tag[aspect_Is[i][j]][0]
                j += 1
                if j == len(aspect_Is[i]):
                    break
                elif aspect_Is[i][j] != aspect_Is[i][j-1] + 1 :# the parts don't belong to one aspect:
                    break
        if word_to_be_added !='':
            lexicon.add(extract_aspect_root(word_to_be_added))
            features.add(word_to_be_added)
    for k,word in enumerate(POS_tag):
        if k in aspect_Bs[i] or k in aspect_Is[i] or word[0] in stop_words_list:
            continue
        lexicon.add(opinion_root_extractor(word[0],False))
with open('auxiliary-files/lexicon.txt','w',encoding='utf-8') as f:
    for word in lexicon:
        f.write(word)
        f.write('\n')
# lexicon = []
# with open('lexicon.txt','r',encoding='utf-8') as f:
#     lexicon = f.read().split('\n')[:-1]
# print(lexicon)
lexicon_dictionary = {}#word to index
for i,word in enumerate(list(lexicon)):
    lexicon_dictionary[word] = i
# print(lexicon_dictionary)
#generating context vector for each feature. for avoiding a sparse matrix we will create each vector as a posting list

def add_to_posting_list(number,posting_list):
    index = len(posting_list)
    for i,element in enumerate(posting_list):
        if number < element:
            index = i
            break
        elif number == element:
            return posting_list
    posting_list.insert(index,number)
    return posting_list



context_vectors = {}#word to posting list
for i,POS_tag in enumerate(POS_tags):
    print(aspect_Bs[i])
    #finding aspects
    #aspects will be added to the lexicon as a complete word
    features_in_this_reveiw = set()
    for begining in aspect_Bs[i]:
        word_to_be_added = POS_tag[begining][0]
        #finding the continious parts of that aspect
        j = 0
        for j in range(len(aspect_Is[i])):
            if aspect_Is[i][j] == begining + 1:
                break
        if j < len(aspect_Is[i]):
            while True:
                word_to_be_added += ' ' + POS_tag[aspect_Is[i][j]][0]
                j += 1
                if j == len(aspect_Is[i]):
                    break
                elif aspect_Is[i][j] != aspect_Is[i][j-1] + 1 :# the parts don't belong to one aspect:
                    break
        if word_to_be_added !='':
            features_in_this_reveiw.add(extract_aspect_root(word_to_be_added))
    for z,feature in enumerate(list(features_in_this_reveiw)):
        if feature not in context_vectors.keys():
            context_vectors[feature] = []
        for j,other_feature in enumerate(list(features_in_this_reveiw)):
            if z != j:
                context_vectors[feature] = add_to_posting_list(number=lexicon_dictionary[other_feature],posting_list=context_vectors[feature])


    for k,word in enumerate(POS_tag):

        if k in aspect_Bs[i] or k in aspect_Is[i] :
            # print("yesss")
            continue
        if word[0] in stop_words_list:
            continue
        for x, feature in enumerate(list(features_in_this_reveiw)):
            # print(feature)
            # print(opinion_root_extractor(word[0],False))
            # print("********")
            context_vectors[feature] = add_to_posting_list(number=lexicon_dictionary[opinion_root_extractor(word[0],False)],
                                                          posting_list=context_vectors[feature])
import json
with open('Results/context_vectors.txt', 'w',encoding='utf-8') as f:
    f.write(json.dumps(context_vectors))



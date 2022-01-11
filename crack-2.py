import Vegenere as V

alphabet="abcdefghijklmnopqrstuvwxyz"
user_input = 'mi huzl wvts dtlw irvl kijrvnvi se mhxw gekkrykeq tyir mfb dyyolkglji gtugtqlx mex fzglw bej xwysej xw nt vrbv vtskxu e aa dtlwdn dtlw rejm fppii idvrehnh xduk eh qdnux hwi cffpi ra'
# user_input="escmsju gdpqtqx poptc zdxw yh wjlw bhhtfmc escvsxu tgrkgdqbh rdxztdy shfjw hteei segiexw"
user_input="escmsjuntvyxvgwdvtiisgmchftqcppmcdgwlehhwidfahsggmcdxtxvxqxtuvdjeilscweqoipxfdqwdlvroekligxrxyigvmihpnqe"
user_input="ij vbxbxln pzrsfwq jbq zw bcnjuub uxrw cbxcbw ub srsjjr inp jcrirxscp"
user_input="kjh hukfy visgovf nkjh julf urxclokvgk us poxshkis ubvq otv qfk us wxpdngxs jkkwnk"
text = user_input.split()
text = ''.join(text)

initials=[]
repetetions=[]
key_length=4
sorted_list=[]
frequency = {"e":15.10,
             "a":8.13,
             's':7.91, 
             't':7.11,
             'i':6.94, 
             'r':6.43,
             "n":6.42,
             "u":6.05,
             "l":5.68,
             "o":5.27,
             "d":3.55,
             "m":3.23,
             "c":3.15,
             "p":3.03,
             "v":1.83, 
             "h":1.08,
             "g":0.97, 
             "f":0.96, 
             "b":0.93, 
             "q":0.89, 
             "j":0.71, 
             "x":0.42, 
             "z":0.21, 
             "y":0.19, 
             "k":0.16, 
             "w":0.04}
words=["informatique",
        "bonjour",
        "madame",
        "bioinfo",
        "texte",
        "valeur",
        "ordinateur",
        "chiffrement",
        "malade",
        "covid",
        "telephone",
        "table",
        "chaise",
        "imprimante",
        "teste",
        "souris",
        "chat",
        "lion",
        "puce",
        "clavier",
        "sachet"]
cypher_text=text

#text partitions depending on key length
parts = [text[i:i+key_length] for i in range(0, len(text), key_length)]

#delete last element if (text % key != 0)
sup=""
if(len(text)%key_length!=0):
    sup=parts.pop()

# print(parts)
# print(sup)
#create empty lists depending on key length
initials=[[] for x in range(key_length)]

#fill in the letters list
for i in range(key_length):
    initials[i]= [x[i] for x in parts]

#calculate repetitions of each letter
for j in initials:
    repetetion=dict()
    for i in j:
        repetetion[i]= j.count(i)
    repetetions.append(repetetion)

#sort the list 
for liste in repetetions:
    sort_dictionary= dict(sorted(liste.items(), key=lambda item: item[1],reverse=True))
    sorted_list.append(sort_dictionary)

#add letters that dont appear in the cipher text
for i in sorted_list:
    for c in alphabet:
        if (c not in i):
            i[c]=0
            
#frequencies to list
frequency_list=list(frequency.keys())
frequency_list_sorted=sorted(frequency_list)

# print(sorted(frequency))

#sort frequencies int the dictionary
sortedDict = dict( sorted(frequency.items(), key=lambda x: x[0].lower()) )
# for k,v in sortedDict.items():
#     print('{}:{}'.format(k,v))

#from string to list
text_list=[]
text_list[:0]=text

# print("sorted",sorted_list)
#replace each letter by its frequency letter
count=0
char=""
for i in sorted_list:
    x=list(i.keys())
    for j in range(count,len(text),3):
        char = x.index(text[j])
        text_list[j]=frequency_list[char]
    count+=1

#list to text  
text=""
for ele in text_list:
    text+=ele
    
#wihwhtsvdjvppqpwmdqhtflxijghqtqxqlsxqjdescmsjuxpeptveaoixqjduqpwmfxixptglqpqxtflplwtpmgrmghpdqkjhygoegjijufdxxtlpahwdxvxveyryihvghgwhvrkigfppymtufxhr


count=0
for i in sorted_list:
    sorted_list[count] = dict( sorted(i.items(), key=lambda x: x[0].lower()) )
    count+=1

# print(sorted_list[0])
# print(sortedDict)

#sorted_list dictionary to list
list_sorted_list=[[] for x in range(key_length)]

count=0
for i in sorted_list:
    list_sorted_list[count]=list(i.values())
    count+=1

#get the frequencies values
frequency_list_values=list(sortedDict.values())

#calculate rates
# for i in list_sorted_list[0]:
#     for j in range(26):
#         list_sorted_list[0]*frequency_list_values

#function that shift to the right by 1
def right(listL):
    k=len(listL)-1
    right = listL[k::]
    left = listL[:k:]
    return(right+left)

#create the rate of each letter
frequency_rate=[[] for x in range(key_length)]
intermidiate=[]
for j in range(key_length):
    for i in range(26):
        for n1,n2 in zip(list_sorted_list[j],frequency_list_values):
            intermidiate.append(n1*n2)
        frequency_rate[j].append(sum(intermidiate))
        intermidiate=[]
        frequency_list_values = right(frequency_list_values)

key_rates=[]
for i in range(key_length):
    key_rates.append(frequency_rate[i].index(max(frequency_rate[i])))

key=""
for i in range(key_length):
    key+=frequency_list_sorted[key_rates[i]]

print("list_sorted_list",list_sorted_list)
print("frequency_list_values",frequency_list_values)
print("frequency_list",frequency_rate)

print(key_rates)
print("key :",key)

decrypted=V.decrypt_veg(user_input,key)
print("cypher_text : ",cypher_text)
print("decrypted : ",decrypted)



keys_rates=[[] for x in range(key_length)]
frequency_rate_copy=frequency_rate.copy()
for i in range(key_length):
    for j in range(4):
        keys_rates[i].append(frequency_rate_copy[i].index(max(frequency_rate_copy[i])))
        frequency_rate_copy[i][frequency_rate_copy[i].index(max(frequency_rate_copy[i]))] = -1

key_letters=[[] for x in range(key_length)]
print(keys_rates)
print(key_letters)


letter=""
for i in range(key_length):
    for j in range(4):
        letter=frequency_list_sorted[keys_rates[i][j]]
        key_letters[i].append(letter)

print(key_letters)

from itertools import product
possibilities = []
iteration = product(*tuple(key_letters))
for thing in iteration:
  possibilities.append(thing)

print(possibilities)
print(len(possibilities))

keys=[]
key_2=""
for i in range(len(possibilities)):
    for j in range(key_length):
        key_2+=possibilities[i][j]
    keys.append(key_2)
    key_2=""
print(keys)

decrypteds=[]
for key in range(len(possibilities)):
    plain_text=V.decrypt_veg(user_input,keys[key])
    decrypteds.append([plain_text,keys[key]])
print("decrepteds",decrypteds)

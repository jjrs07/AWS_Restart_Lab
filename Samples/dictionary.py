myDictionary= {}
myDictionary["one"] = 1
myDictionary["two"] = 2
myDictionary[3] = "three"
myDictionary["four"] = 4.4
myDictionary["five"] = "hello"


print(myDictionary[3])
for key, value in myDictionary.items():
    print(key, value)


#print(myDictionary["one"])
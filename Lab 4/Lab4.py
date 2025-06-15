"""
Lab 4 Working with Lists, Tuples, and Dictionaries
"""


myFruitList = ["apple", "banana", "cherry", "mango"]
print(myFruitList)
print(type(myFruitList))

print(myFruitList[0])
print(myFruitList[1])
print(myFruitList[2])
print(myFruitList[3])

myFruitList[2] = "Orange"

print(myFruitList)


myFinalAnswerTuple = ("apple", "banana", "pineapple","cherry")
print(myFinalAnswerTuple)
print(type(myFinalAnswerTuple))

print(myFinalAnswerTuple[0])
print(myFinalAnswerTuple[1])
print(myFinalAnswerTuple[2])
print(myFinalAnswerTuple[3])

#myFinalAnswerTuple[2] = "cherry"

myFavoriteFruitDictionary = {
  "Akua" : "apple",
  "Saanvi" : "banana",
  "Paulo" : "pineapple"
}

print(myFavoriteFruitDictionary)
print(type(myFavoriteFruitDictionary))

print(myFavoriteFruitDictionary["Akua"])
print(myFavoriteFruitDictionary["Saanvi"])
print(myFavoriteFruitDictionary["Paulo"])
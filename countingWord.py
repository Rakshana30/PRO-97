intro = input("enter your intro")
characterCount = 0
wordCount = 1
for i in intro:
    characterCount = characterCount+1
    if(i==' '):
        wordCount = wordCount+1
print("number of characters in the intro")
print(characterCount)
print("number of word in the intro")
print(wordCount)

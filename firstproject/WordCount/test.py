sentence = "안녕 나는 은주 안녕"
    
wordList=sentence.split()

wordDict={}

for word in wordList:        
    if word in wordDict:
        wordDict[word]+=1
    else:
        wordDict[word]=1

print(wordDict)
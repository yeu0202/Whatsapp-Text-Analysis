f = open("Rachel_chat.txt", "r")

text = f.read()
rawTexts = text.split('M] ')
# texts = f.readlines()
# print(texts)
texts = []
timeStamps = []
for word in rawTexts:
    index = word.rfind('\n')
    texts.append(word[:index])
    timeStamps.append(word[index:])

people = ['Kelvin', 'Rachel']
person1Count = 0
person2Count = 0
person1Words = {}
person2Words = {}

errorTexts = []

for textLine in texts[:]:  # you can change the [:] in texts to change the range
    print(textLine)
    personNumber = 1

    # split to find person message count
    t = textLine.split(':')
    if people[0] in t[0]:
        person1Count += 1
    elif people[1] in t[0]:
        person2Count += 1
        personNumber = 2
    else:
        errorTexts.append(textLine)

    # find words by each person
    messageContent = ""
    for i in range(len(t)):
        if i != 0:
            messageContent += t[i]
    # print(messageContent)
    messageByWord = messageContent.split()
    for word in messageByWord:
        if not word.isupper() or len(word) == 1:
            word = word.lower()
        if personNumber == 1:
            if word in person1Words:
                person1Words[word] += 1
            else:
                person1Words[word] = 1
        elif personNumber == 2:
            if word in person2Words:
                person2Words[word] += 1
            else:
                person2Words[word] = 1

print("\n\n\n")

# word analysis
person1Sorted = dict(sorted(person1Words.items(), key = lambda item: item[1], reverse = True))
person2Sorted = dict(sorted(person2Words.items(), key = lambda item: item[1], reverse = True))

print(people[0] + "'s words:")
wordAnalysisMaxWordsDisplay = 30
wordAnalysisMinWordsCount = 100
wordMaxCount = 0
for word in person1Sorted:
    if person1Sorted[word] > wordAnalysisMinWordsCount:
        print(word, person1Sorted[word], "times")
    wordMaxCount += 1
    if wordMaxCount > wordAnalysisMaxWordsDisplay:
        break
print("\n\n\n" + people[1] + "'s words:")
wordMaxCount = 0
for word in person2Sorted:
    if person2Sorted[word] > wordAnalysisMinWordsCount:
        print(word, person2Sorted[word], "times")
    wordMaxCount += 1
    if wordMaxCount > wordAnalysisMaxWordsDisplay:
        break


# people message count
print("\n\nnumber of messages: ", len(texts))
print("messages by", people[0], ":", person1Count)
print("messages by", people[1], ":", person2Count, "\n")


# errors
print("errors in text: ", errorTexts)


# f = open("Rachel_chat.txt", "r")
#
# text = f.read()
# texts2 = text.split('?')
# print(texts2[:1000])

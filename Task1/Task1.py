# Write a program which will delete from text all the words, containing "абв"

inputString = input('Please enter some text: ')
wrongText = "абв"
#result = [word for word in inputString.split() if wrongText not in word]
resultString = " ".join([word for word in inputString.split() if wrongText not in word])
print(f'resultString is: {resultString}')
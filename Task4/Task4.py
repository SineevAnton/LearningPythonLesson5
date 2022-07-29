# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

def coding(txt):
    count = 1
    result = ''
    for i in range(len(txt)-1):
        if txt[i] == txt[i+1]:
            count += 1
        else:
            result = result + str(count) + txt[i]
            count = 1
    if count > 1 or (txt[len(txt)-2] != txt[-1]):
        result = result + str(count) + txt[-1]
    return result

def decoding(txt):
    number = ''
    result = ''
    for i in range(len(txt)):
        if not txt[i].isalpha():
            number += txt[i]
        else:
            result = result + txt[i] * int(number)
            number = ''
    return result

with open('TextToEncode.txt', 'r') as decodedFile:
    data = decodedFile.readline()
    encodedData = coding(data)
    print(f"Текст после кодировки: {encodedData}")
    with open('TextToDecode.txt', 'a') as encodedFile:
        encodedFile.write(encodedData + '\n')

with open('TextToDecode.txt', 'r') as encodedFile:
    data = encodedFile.readline()
    encodedData = decoding(data)
    print(f"Текст после дешифровки: {encodedData}")
    with open('TextToEncode.txt', 'a') as decodedFile:
        decodedFile.write(encodedData + '\n')

data = input()
parsed_data = data.split()
sentence = []
sentences = []
for word in parsed_data:
    if '.' not in word:
        sentence.append(word)
    else:
        if '?' in word:
            test = word.split('?')
            sentence.append(test[0]+'?')
            if test[1] == '"':
                sentence.append(test[1])
            sentences.append(sentence)
            sentence = []
            if test[1] != '' and test[1] != '"':
                if '!' in test[1]:
                    sentence.append(test[1])
                    sentences.append(sentence)
                    sentence = []
                else:
                    sentence.append(test[1])
        if '!' in word:
            test = word.split('!')
            sentence.append(test[0]+'!')
            if test[1] == '"':
                sentence.append(test[1])
            sentences.append(sentence)
            sentence = []
            if test[1] != '' and test[1] != '"':
                sentence.append(test[1])
        if '.' in word:
            test = word.split('.')
            sentence.append(test[0]+'.')
            if test[1] == '"':
                sentence.append(test[1])
            sentences.append(sentence)
            sentence = []
            if test[1] != '' and test[1] != '"':
                sentence.append(test[1])

for s in sentences:
    sent = ' '.join(s)
    print(sent)

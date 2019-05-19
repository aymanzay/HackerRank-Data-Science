data = input()

parsed_data = data.split()
sentence = []
sentences = []
delimiters = ['.', '?', '!']
for word in parsed_data:
    if '?' in word:
        temp = word.split('?')
        if '"' in temp[1]:
            x = temp[0] + temp[1] + ' '
            sentence.append(x)
            del temp[0]
            del temp[0]
        for w in temp:
            if '!' in w:
                sentences.append(w)
            else:
                sentence.append(w)

        sentences.append(sentence)
        sentence = []
    elif '.' in word:
        temp = word.split('.')
        sentence.append(temp[0] + '.')
        del temp[0]
        if '"' in temp[0]:
            sentence.append(temp[0])
            del temp[0]
        sentences.append(sentence)
        sentence = []
    else:
        sentence.append(word)

ready_sent = []
ready_sent.append(' '.join(sentences[0]))
combined = False
for i, j in zip(range(len(sentences) - 1), range(1, len(sentences))):
    first = sentences[i]
    second = sentences[j]

    sent1 = ' '.join(first)
    sent2 = ' '.join(second)

    if sent2[0].islower():
        ready_sent[len(ready_sent) - 1] += sent2
        combined = True

    if not combined:
        ready_sent.append(sent2)
    else:
        # skip
        combined = False

for s in ready_sent:
    print(s)

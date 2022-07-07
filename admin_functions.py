# add a word and convert it to a vocabulary word with gap
def setWords():
    print("Input your word:")
    a = input()
    b = a.lower()
    a, b = list(a), list(b)
    temp_list = []
    voc_word = ''
    for i in range(len(a)):
        if a[i] != b[i]:
            temp_list.append(i)

    for k in range(len(a)):
        for l in range(len(temp_list)):
            if k == temp_list[l]:
                voc_word += '_'
            else:
                voc_word += a[k]

    return voc_word

def count_letters(sentence, average = False):
    count_all = 0
    if average == False:
        for i in sentence:
            if i!= ' ': count_all+=1
        return count_all
    else:
        count_words = [len(word) for word in sentence.split()]
        return(sum(count_words)/len(count_words))

print(count_letters("Beep boop"))
sentence=input('write your sentence : ')
word_count=1
letter_count=0
for i in sentence:
    letter_count+=1
    if i == ' ':
        word_count+=1
print('word count : ',word_count)
print('letter count : ',letter_count)
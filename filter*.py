with open('filtered_words.txt','r') as f:
    text=f.read()
word=text.split('\n')
judge=True
while(1):
    k=input('enter to test:')
    for i in word:
        if i in k:
            k=k.replace(i,'*'*len(i))
    print(k)


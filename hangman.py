def isanswer(secret, letters):
    word = []
    for i in secret:
        word.append(i)
    word = list(set(word))
    for i in letters:
        if i in word:
            word.remove(i)
        else: 
            return False
    return False if word != [] else True

def status(answer, letters):
    result1 = []
    result2 = []
    for cnt in answer:
        result1.append(cnt)
    for i in answer:
        result2.append('_')
    for ii in letters: 
        if ii in answer: 
            for iii in range(len(result1)): 
                if ii == result1[iii]:
                    result2[iii] = ii
    return (' '.join(result2)).replace(' ','')

def hangman(answer):
    letters = []
    attempt = 6
    input_answer = []
    while True:
        print(f'남은 시도 : {attempt}')
        print(f'{status(answer, letters):^20}')
        char = input('알파벳을 입력하세요 :')
        input_answer.append(char)
        print(input_answer.count(char))
        if input_answer.count(char) > 1:
            print('ㄹㄹ')
            continue
        if not char.isalpha() or len(char) != 1:
            print('알파벳을 입력하세요.')
            continue
            
        letters.append(char)
        if char in answer:
            print(f'{answer.count(char)}개 있어요.')
        else :
            print('틀렸어요.')
            attempt -= 1
            
        if isanswer(answer, letters):
            print('정답', answer)
            return None
        
        if attempt == 0:
            return 'ㅈㅈ'
        print('========================')
if __name__ == '__main__':
        hangman('pneumonoultramicroscopicsilicovolcanoconiosis')
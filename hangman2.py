def isanswer(secret, letters):
    return not (set(secret) - set(letters))

def status(answer, letters):
    for char in answer:
        if char not in letters:
            answer = answer.replace(char, '_')
    return answer

def hangman(answer):
    letters = []
    attempt = 8
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
            
        if isanswer(answer, letters):
            print('정답', answer)
            return None
                  
        attempt -= 1
        
        if attempt == 0:
            return 'ㅈㅈ'
        print('========================')

if __name__ == '__main__':
        hangman('pneumonoultramicroscopicsilicovolcanoconiosis')
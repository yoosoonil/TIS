# 문제풀이 참고 : https://ywtechit.tistory.com/153

a = input()
b = input()
c = input()

resist = {
    'black': 0,
    'brown': 1,
    'red': 2,
    'orange': 3,
    'yellow': 4,
    'green': 5,
    'blue':6,
    'violet': 7,
    'grey': 8,
    'white': 9    
}
# 값들을 딕셔너리로 만든다.

print((resist[a]*10 + resist[b]) * (10 ** resist[c]))
# 앞자리+뒷자리 * 10^c 이기에 (a*10+b)*10**c 이다.
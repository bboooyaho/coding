# 정수 1개 입력받아 2배 곱해 출력하기
try:
    n1, n2, n3 = map(int, input().split(" "))
    sum = n1 + n2 + n3
    print(sum, format(sum / 3, ".2f"))
except ZeroDivisionError as e:
    print("n2 는 양수여야 합니다.")

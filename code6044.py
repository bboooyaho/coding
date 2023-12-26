# 정수 2개 입력받아 자동 계산하기


# 예외처리
try:
    n1, n2 = map(int, input().split(" "))
    # 합
    print(n1 + n2)
    # 차
    print(n1 - n2)
    # 곱
    print(n1 * n2)
    # 몫
    print(format(n1 // n2))
    # 나머지
    print(format(n1 % n2))
    # 나눈 값
    print(format(n1 / n2, ".2f"))
except ZeroDivisionError as e:
    print("n2 는 양수여야 합니다.")

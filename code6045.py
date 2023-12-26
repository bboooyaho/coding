# 정수 3개 입력받아 합과 평균 출력하기
# 예외처리
try:
    n1, n2, n3 = map(int, input().split(" "))
    sum = n1 + n2 + n3
    print(sum, format(sum / 3, ".2f"))
except ZeroDivisionError as e:
    print("n2 는 양수여야 합니다.")

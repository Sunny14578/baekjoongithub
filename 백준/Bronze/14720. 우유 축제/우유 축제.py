# 우유 가게 수 입력 받기
n = int(input())

# 우유 가게 정보 입력받기 (리스트)
milk_list = list(map(int, input().split()))

# 마신 우유 수를 저장할 변수 count
count = 0

# for문으로 우유 가게를 차례로 방문하면서
for i in range(n):
   # 우유 가게에서 파는 우유 종류가 내가 이번에 마실 우유 종류와 같다면, count 1 증가
   if milk_list[i] == count % 3:
        count += 1

print(count)
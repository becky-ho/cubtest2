# 程式邏輯題目
# QA部門今天舉辦團康活動，有n個人圍成一圈，順序排號。從第一個人開始報數（從1到3報數），凡報到3的人退出圈子。
# 請利用一段程式計算出，最後留下的那位同事，是所有同事裡面的第幾順位?

def find_last_person(n):
    if n == 0:
        return 0

    index = 0
    for i in range(1, n + 1):
        index = (index + 3) % i

    return index + 1

# 測試程式
n = int(input("請輸入同事的總人數："))
last_person = find_last_person(n)
print("最後留下的同事是第", last_person, "順位。")

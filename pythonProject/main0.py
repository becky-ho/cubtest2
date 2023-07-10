# 程式邏輯題目
# 國泰補習班中，有五位學生期中考的成績分別為[53, 64, 75, 19, 92]，但是老師在輸入成績的時候看反了，
# 把五位學生的成績改成了[35, 46, 57, 91, 29]，請用一個函數來將學生的成績修正。

def revise_score(old_score):
    new_score = []
    for i in range(len(old_score)):
        a = old_score[i] % 10
        b = old_score[i] - a
        new_score.append(int(a * 10 + b / 10))
    return new_score

# 測試程式
old_score = [35, 46, 57, 91, 29]
new_score = revise_score(old_score)
print(new_score)



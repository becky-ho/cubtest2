# 程式邏輯題目
# 國泰銀行要慶祝六十周年，需要買字母貼紙來布置活動空間，文字為"Hello welcome to Cathay 60th year anniversary"，
# 請寫一個程式計算每個字母(大小寫視為同個字母)出現次

def count_letters(text):
    letter_count = {}
    for char in text:
        if char.isalnum():
            char = char.lower()
            if char in letter_count:
                letter_count[char] += 1
            else:
                letter_count[char] = 1

    sorted_count = sorted(letter_count.items())
    return sorted_count

# 測試程式
text = "Hello welcome to Cathay 60th year anniversary"
result = count_letters(text)
for letter, count in result:
    print(f"{letter}: {count}")
# 程式邏輯題目
# 國泰銀行要慶祝六十周年，需要買字母貼紙來布置活動空間，文字為"Hello welcome to Cathay 60th year anniversary"，
# 請寫一個程式計算每個字母(大小寫視為同個字母)出現次



from collections import Counter

def count_letters(text):
    text = text.lower()  # 將文字轉換為小寫
    letter_count = Counter(c for c in text if c.isalpha())
    return letter_count

# 測試程式
text = "Hello welcome to Cathay 60th year anniversary"
result = count_letters(text)
for letter, count in result.items():
    print(letter, ":", count)

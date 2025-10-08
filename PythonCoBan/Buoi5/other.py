sentence = "Hello Hoàng đẹp trai"
print(sentence)

key = "Hel"
if sentence.startswith(key):
    print(f"sentence có chứa {key}")

map_st = ' & '.join(["Hoàng", "Đẹp", "trai"])
print(map_st, len(map_st))

# a, b, c = map(int, input("Nhập a, c, b:").split())
# print(a, b, c)

print("|", "Cindy".center(25), "|")
print("|", "Cindy".rjust(25, '_'), "|")

spam = 'SpamSpamBaconSpamEggsSpamSpam'

print(spam.strip('ampS'))

print(''.rjust(30, '-'))


## String formatting
st = "Hello %d %d người đẹp" % (5, 6)
print(st)


'''
    :-^20
    Đây là cú pháp định dạng:
    :  bắt đầu phần định dạng
    -  ký tự lấp đầy (fill character)
    ^  căn giữa (alignment)
    20  tổng độ dài cần định dạng
'''
name = "cindy"
print(f"Dep trai {name=:-^20}")
print(f"Dep trai {name= :-^20}")

a = 123456789
print(f"{a:,}")





# bytes与str互转

# str->bytes encoding
# bytes->str decoding

s1 = 'hello，世界！'
print(s1)
b = s1.encode(encoding='utf-8')
print(b)
s2 = b.decode(encoding='utf-8')
print(s2)

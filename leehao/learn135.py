# re模块 正则表达式
import re

s = 'My email is 568233708@qq.com,pilihaotian@163.com'
print(re.findall('\w+@\w+\.com', s))

print(re.findall('abc', 'abcdefghij'))

print(re.findall('ab|cd', 'abcdefghij'))

print(re.findall('ab|bc', 'abcdefghij'))

print(re.findall('.oo.', 'it looks like a good book.'))

print(re.findall('^hello', 'hello world'))

print(re.findall('^world', 'hello world'))

print(re.findall('hello$', 'hello world'))

print(re.findall('world$', 'hello world'))

print(re.findall('fo*', 'foa fooa foooa fooooa'))

print(re.findall('fo+', 'foa fooa foooa fooooa'))

print(re.findall('l*', 'hello world'))
print(re.findall('l+', 'hello world'))

print(re.findall('f?', 'abc f fo'))

print(re.findall('fo{3}', 'foa fooa foooa fooooa'))

print(re.findall('fo{3,4}', 'foa fooa foooa fooooa'))

print(re.findall('[ab12AB*]', 'abcd1234ABCD.*()&^&'))
print(re.findall('[a-bA-B0-2*-^]', 'abcd1234ABCD.*()&^&'))

print(re.findall('[^ab12AB*]', 'abcd1234ABCD.*()&^&'))
print(re.findall('[^a-bA-B0-2*-^]', 'abcd1234ABCD.*()&^&'))

print(re.findall('\d', 'abcd1234'))
print(re.findall('\D', 'abcd1234'))

# 匹配11位电话号码
print(re.findall('1\d{10}', '18095555555000000abc18296365985$%#'))

print(re.findall('\w+', 'abcd_1234&*)(%$'))
print(re.findall('\W+', 'abcd_1234&*)(%$'))

print(re.findall('\s+', 'hello world \t my \r name \n is leehao'))
print(re.findall('\S+', 'hello world \t my \r name \n is \0 leehao'))

# 训练，匹配出大写字母开头的单词
print(re.findall("[A-Z]\S+", 'hello World , I am from China'))

# 精准匹配hello该单词，该单词就是hello
print(re.findall("\Ahello\Z", 'hello'))
print(re.findall("\A/\w+/\w+/\w+\Z", '/D/User/leehao'))
print(re.findall("\A/\w+/\w+/\w+\Z", '/D/User/leehao/docs/ppt'))

print(re.findall(r"is", 'this is a world,aaisbb'))
# 匹配第二个is
print(re.findall(r"\bis\b", 'this is a world,aaisbb'))
# 匹配第一个this中的is
print(re.findall(r"\Bis\b", 'this is a world,aaisbb'))
# 匹配第三个aaisbb中的is
print(re.findall(r"\Bis\B", 'this is a world,aaisbb'))

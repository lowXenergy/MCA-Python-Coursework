# # import re
# # string = """Hello my Number is 123456789 and
# #             my friend's number is 9999"""
            
# # #regex = '\d+'
# # #match = re.findall('\d+', string)
# # print(re.findall('\\d+', string))
# # p=re.compile('[a-e]')
# # print(p.findall(string))
# # # import re
# # # p = re.compile('[a-e]')
# # # print(p.findall("Aye, said Mr. Gibenson Stark"))

# import re
# p = re.compile(r'\d')
# print(p.findall("I went to him at 11 A.M. on 4th July 1886"))

# p = re.compile(r'\d+')
# print(p.findall("I went to him at 11 A.M. on 4th July 1886"))

import re

p = re.compile(r'\w')
print(p.findall("He&\llo+"))

p = re.compile(r'\w+')
print(p.findall("i am 999 %$ pyhto()n"))

p = re.compile(r'\W')
print(p.findall("he said *** in."))


#~ Example of match()
#* Ex.1:
import re
s='hai python'
mo=re.match('h',s)
print(mo) ## return ---> <re.Match object; span=(0, 1), match='h'>




#* Ex.2:
import re
s='hai python'
mo=re.match('y',s)
print(mo) ## return ---> None




#* Ex.3:
import re
s='hai python'
mo=re.match('\w{3}',s)
print(mo) ## return ---> None



##------------------------------------------------------------------------------------------------





#~ Example of search()
#* Ex.1:
import re
s='hai python'
mo=re.search('t',s)
print(mo) ## return ---> <re.Match object; span=(6, 7), match='t'>




#* Ex.2:
import re
s='hai python'
mo=re.search('h',s)
print(mo) ## return ---> <re.Match object; span=(0, 1), match='t'>




#* Ex.3:
import re
s='hai python'
mo=re.search('y',s)
print(mo) ## return ---> <re.Match object; span=(5, 6), match='y'>




#* Ex.4:
import re
s='hai python'
mo=re.search('z',s)
print(mo) ## return ---> None



##------------------------------------------------------------------------------------------




#~ Example of findall()
#* Ex.1:
import re
s='hai python'
mo=re.findall('t',s)
print(mo) ## return ---> ['t']




#* Ex.2:
import re
s='hai python'
mo=re.findall('h',s)
print(mo) ## return ---> ['h', 'h']




#* Ex.3:
import re
s='hai python'
mo=re.findall('y',s)
print(mo) ## return ---> ['y']




#* Ex.4:
import re
s='hai python'
mo=re.findall('z',s)
print(mo) ## return ---> []



##-----------------------------------------------------------------------------------




#~ Example of meta charecter:-
#* any charecter ('.')
import re
s='hAi pyt2@oN'
print(re.findall('.',s))    ## return --->['h', 'A', 'i', ' ', 'p', 'y', 't', '2', '@', 'o', 'N']





#* starts with charecter ('^')
import re
s='hAi pyt2@oN'
print(re.findall('^h',s))  ## return ---> ['h']
print(re.findall('^p',s))  ## return ---> []





#* ends with charecter ('$')
import re
s='hAi pyt2@oN'
print(re.findall('N$',s))  ## return ---> ['N']
print(re.findall('s$',s))  ## return ---> []





#* 0 to n occurance charecter ('*')
import re
s='hello help hp heep heeep heeeeep'
print(re.findall('he*p',s)) ## return ---> ['hp', 'heep', 'heeep', 'heeeeep']





#* 1 to n occurance charecter ('+')
import re
s='hello help hp heep heeep heeeeep'
print(re.findall('he+p',s)) ## return ---> ['heep', 'heeep', 'heeeeep']





#* 0 to 1 occurance charecter ('?')
import re
s='hello help hp heep heeep heeeeep'
print(re.findall('he?p',s)) ## return ---> ['hp']





#* specified occurance charecter ('{}')
import re
s='hello help hp heep heeep heeeeep'
print(re.findall('he{2}p',s)) ## return ---> ['heep']
print(re.findall('he{3}p',s)) ## return ---> ['heeep']
print(re.findall('he{4}p',s)) ## return ---> []
print(re.findall('he{2,7}p',s)) ## return ---> ['heep', 'heeep', 'heeeeep']


#* or(|)
import re
s1='hai hello help hp hep heep heeeep'
print(re.findall('he*p|hai',s1)) ## return ---> ['hai', 'hp', 'hep', 'heep', 'heeeep']




##-----------------------------------------------------------------------------------



#~ special sequence Example
#* \w <--- small w
import re
s1='hai 12_@bye'
print(re.findall('\w',s1)) ## return ---> ['h', 'a', 'i', '1', '2', '_', 'b', 'y', 'e']
print(re.findall('\w{2}',s1)) ## return ---> ['ha', '12', 'by']
print(re.findall('\w{3}',s1)) ## return ---> ['hai', '12_', 'bye']




#* \W <--- capital W
import re
s1='hai 12_@bye'
print(re.findall('\W',s1)) ## return ---> [' ', '@']




#* \d
import re
s1='hai 12_@bye'
print(re.findall('\d',s1)) ## return ---> ['1', '2']




#* \D
import re
s1='hai 12_@bye'
print(re.findall('\D',s1)) ## return ---> ['h', 'a', 'i', ' ', '_', '@', 'b', 'y', 'e']




#* \s
import re
s1='hai 12_@bye'
print(re.findall('\s',s1)) ## return ---> [' ']




#* \S
import re
s1='hai 12_@bye'
print(re.findall('\S',s1)) ## return ---> ['h', 'a', 'i', '1', '2', '_', '@', 'b', 'y', 'e']




#~ ------------------------------------------------------------------------------------------




#* []
import re
s='abcdef'
print(re.findall('abc',s)) ## return ---> ['abc']
print(re.findall('[abc]',s)) ## return ---> ['a', 'b', 'c']

s1='abfuqAg838929@@#45$op'
print(re.findall('[e-p]',s1)) ## return ---> ['f', 'g', 'o', 'p']
print(re.findall('[a-k]',s1)) ## return ---> ['a', 'b', 'f', 'g']
print(re.findall('[a-z]',s1)) ## return ---> ['a', 'b', 'f', 'u', 'q', 'g', 'o', 'p']
print(re.findall('[a-zA-Z]',s1)) ## return ---> ['a', 'b', 'f', 'u', 'q', 'A', 'g', 'o', 'p']
print(re.findall('[a-zA-Z0-9]',s1)) ## return ---> ['a', 'b', 'f', 'u', 'q', 'A', 'g', '8', '3', '8', '9', '2', '9', '4', '5', 'o', 'p']
print(re.findall('[a-zA-Z0-9][a-zA-Z0-9]',s1)) ## return ---> ['ab', 'fu', 'qA', 'g8', '38', '92', '45', 'op']
print(re.findall('[a-zA-Z0-9]{2}',s1)) ## return ---> ['ab', 'fu', 'qA', 'g8', '38', '92', '45', 'op']
print(re.findall('[a-zA-Z0-9][a-zA-Z]',s1)) ## return ---> ['ab', 'fu', 'qA', 'op']
print(re.findall('[a-zA-Z0-9]{3}',s1)) ## return ---> ['abf', 'uqA', 'g83', '892']
print(re.findall('[4-9][0-9]',s1)) ## return ---> ['83', '89', '45']
print(re.findall('[4-9][5-9]',s1)) ## return ---> ['89', '45']





#* [^ character]
import re
s='Aj784gjk@fT891764'
print(re.findall('[Ajk]',s)) ## return ---> ['A', 'j', 'j', 'k']
print(re.findall('[^Ajk]',s)) ## return ---> ['7', '8', '4', 'g', '@', 'f', 'T', '8', '9', '1', '7', '6', '4']





#* Match()  special charecter
import re
s='A*j784abc+@'
print(re.findall('@',s)) ## return ---> ['@']
print(re.findall('[+]',s)) ## return ---> ['+']
print(re.findall('\+',s)) ## return ---> ['+']
print(re.findall('[*]',s)) ## return ---> ['*']
print(re.findall('\*',s)) ## return ---> ['*']
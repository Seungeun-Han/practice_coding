from collections import Counter
import re

def solution(str1, str2):
    answer = 0
    
    str1, str2 = str1.lower(), str2.lower()
    if str1 == str2: return 65536

    rule = re.compile(r'[a-z]{2}')
    str1_multilist = [str1[i:i+2] for i in range(len(str1)-1) if rule.findall(str1[i:i+2])]
    str2_multilist = [str2[i:i+2] for i in range(len(str2)-1) if rule.findall(str2[i:i+2])]
    
    str1_multiset = Counter(str1_multilist)
    str2_multiset = Counter(str2_multilist)
    
    inter = len(list((str1_multiset & str2_multiset).elements()))
    uni = len(list((str1_multiset | str2_multiset).elements()))
        
    if uni == 0:
        answer = 0
    else:
        answer = inter/uni
        
    return int(answer*65536)
import re
strs =["图5 全国降水量预报图（4月18日08时-19日08时）","别的内容（见图1）。"]
img_anotation_rz = r'（见图[1-9]）'
for i,str in enumerate(strs):
    if(str[0]=='图'):
        strs.remove(str)
    strs[i] = re.sub(img_anotation_rz,"",strs[i])
print(strs)
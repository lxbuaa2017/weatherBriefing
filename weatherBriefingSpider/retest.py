# import re
# strs =["二、重点天气预报图5 全国降水量预报图（4月18日08时-19日08时）","别的内容（见图1）。"]
# # img_anotation_rz = r'（见图[1-9]）'
# # for i,str in enumerate(strs):
# #     if(str[0]=='图'):
# #         strs.remove(str)
# #     strs[i] = re.sub(img_anotation_rz,"",strs[i])
# str = strs[0]
# strs.remove(strs[0])
# if(str[0:2]=="二、"):
#  print(str)
strs = [1, 3, 5, 7, 12, 'a', 'v', 'b']
print(strs[1:])
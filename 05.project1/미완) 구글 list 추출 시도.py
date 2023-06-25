import requests

response = requests.get("https://www.google.com/complete/search?q=%EC%A3%BC%EC%8B%9D%20%E3%84%B1&cp=4&client=gws-wiz&xssi=t&hl=ko&authuser=0&psi=mYmQY_r3GIWF-AacrZnQAw.1670416793876&dpr=1.25")
origin_data = response.text


print(type(origin_data))
print(origin_data)
# string_data = "".join(map(str, origin_data))
# # print(string_data)

# split_data = string_data.split(")]}'")
# replace_data= list()

# for i in split_data:
#     new_i = i.replace('\\u003cb\\u003e',"").replace("\\u003c\\/b\\u003e", "")
#     replace_data.append(new_i)
# print(replace_data)
# print(type(replace_data))

# print(type(replace_data))
# for i in replace_data:
#     replace_data2 = i.replace('\\u003c\\/b\\u003e"',"")
# print(replace_data2)


# print(replace_data)


# print(origin_data.split(')]}')[1].replace('\\u003cb\\u003e', ''))
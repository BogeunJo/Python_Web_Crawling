person_info_list=[
    ["유재석", 51, "남"],
    ["노홍철,", 44, "남"],
    ["하하", 44, "남"]
]

#바깥 리스트에 접근
print(person_info_list[0])

#바깥 리스트에 할당
person_info_list[1]=["박명수", 51, "남"]
print(person_info_list)

# 바깥 리스트 길이
print(len(person_info_list))

# 안쪽 리스트에 접근
print(person_info_list[0][0])

# 안쪽 리스트에 할당
person_info_list[1][2]= "여"

print(person_info_list)


good_number = [2,45,66,2,44,1]
choice = []
lucky = []
for i in range(6):
    choice.append(int(raw_input("Please put 6 numbers:")))
    



for num in choice:
    for good in good_number:
        if num == good:
            lucky.append(num)

print(len(lucky))

def input_list():
    inputlist = input("Fill number in the list (seperated by spacebar): ")
    result = [int(x) for x in inputlist.split()]
    return result


num_list = input_list()
k = int(input("k = "))
result = []
sub_list = []

for element in num_list:
    sub_list.append(element)

    if len(sub_list) == k:
        result.append(max(sub_list))
        del sub_list[0]

print(result)

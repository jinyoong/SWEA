cell_dict = {"TV": 2000000,
            "냉장고": 1500000,
            "책상": 350000,
            "노트북": 1200000,
            "가스레인지": 200000,
            "세탁기": 1000000}
'''cell_list = list(cell_dict.items())
cell_list.sort(key= lambda x: x[1], reverse=True)
print(cell_list)'''

cell_dict2 = sorted(cell_dict, key= lambda x: cell_dict[x], reverse=True)

for i in cell_dict2:
    print("{}: {}".format(i, cell_dict[i]))

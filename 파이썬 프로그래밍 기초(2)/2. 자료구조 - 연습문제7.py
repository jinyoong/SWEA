num_input = int(input())

yaksu_list = [i for i in range(1, num_input + 1) if num_input % i == 0]
print(yaksu_list)
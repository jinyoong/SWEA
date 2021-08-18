def juice(people):
    number = ['1/' + str(people)]
    return (number * people)


T = int(input())

for test_case in range(1, T + 1):
    people = int(input())
    print("#{}".format(test_case), *juice(people))

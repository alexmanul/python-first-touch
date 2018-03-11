def count_over_30(list_ages):
    count_worker = 0
    for age in list_ages:
        if age > 30:
            count_worker = count_worker + 1
    print("Количество работников старше 30 лет: ")
    print(count_worker)


def count_over_30_two(list_ages):
    i = 0
    count_worker = 0
    while i < len(list_ages):
        if list_ages[i] > 30:
            count_worker = count_worker + 1
        i = i + 1
    print("Количество работников старше 30 лет: ")
    print(count_worker)


list_ages_of_workers = [25, 36, 35, 34, 38, 22, 21, 25]

count_over_30(list_ages_of_workers)
count_over_30_two(list_ages_of_workers)

def count_over_30(dict_workers):
    count_worker = 0
    for key in dict_workers.keys():
        if dict_workers[key] > 30:
            count_worker = count_worker + 1
    print("Количество работников старше 30 лет: ")
    print(count_worker)


dict_our_workers = {"Andrew": 34, "Michael": 35, "Alex": 33, "Max": 32, "Elena": 24, "Sergey": 26}

count_over_30(dict_our_workers)

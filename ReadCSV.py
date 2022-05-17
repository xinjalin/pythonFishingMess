from csv import DictReader


def main():
    __csv_read__()


def __csv_read__():
    # open file in read mode
    with open('Fish.csv', 'r') as csv_file_in_memory:
        dict_reader = DictReader(csv_file_in_memory)
        list_of_dict = list(dict_reader)
        print(list_of_dict)


if __name__ == '__main__':
    main()

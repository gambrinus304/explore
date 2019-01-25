import csv



def write_csv(data):
    with open('names.csv', 'a') as file:
        writer = csv.writer(file)
        writer.writerow((data['name'], data['surname'], data['age']))


def write_csv2(data):
    with open('names.csv', 'a') as file:
        order = ['name', 'surname', 'age']
        writer = csv.DictWriter(file, fieldnames=order)

        writer.writerow(data)


def main():
    d1 = {'name': 'Ivan', 'surname': 'Hzkov', 'age': '15'} 
    d2 = {'name': 'Fedor', 'surname': 'Ivanov', 'age': '30'}
    d3 = {'name': 'Igor', 'surname': 'Petrov', 'age': '45'}

    l = [d1, d2, d3]

    # for i in l:
    #     write_csv2(i)



with open('cmc_pagination.csv') as file:
    fieldnames = ['name',  'link', 'price']
    reader = csv.DictReader(file, fieldnames=fieldnames)

    for row in reader:
        print(row)


if __name__ == "__main__":
    main()
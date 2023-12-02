import csv


def read_csv_file(csv_file):
    data = []
    with open(csv_file) as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            data.append(row[0])

    return data


def read_txt_file(text_file):
    with open(text_file) as f:
        data = f.readlines()

    return data


def conver_value_to_number(value) -> str:
    try:
        v = int(value)
    except ValueError:
        v = int(mapping.get(value))
    return str(v)

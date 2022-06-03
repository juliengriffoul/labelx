import json
from csv import reader, writer


def parse_config_file(path):
    with open(path, "r", encoding="utf-8") as file:
        return json.load(file)


def get_length_of_csv_file(path):
    with open(path, "r", encoding="utf-8") as file:
        csv_reader = reader(file)
        return len(list(csv_reader))


def append_row_to_csv_file(path, delimiter, length, fields, row):
    with open(path, "a", encoding="utf-8") as file:
        csv_writer = writer(file, delimiter=delimiter)

        if length == 0:
            csv_writer.writerow(fields)

        csv_writer.writerow(row)


def get_rows_of_csv_file(path, delimiter):
    rows = []

    with open(path, "r", encoding="utf-8") as file:
        csv_reader = reader(file, delimiter=delimiter)

        for row in csv_reader:
            rows.append(row[:-1])

    return rows


def get_first_non_labelled_row(path, delimiter, labelled_rows):
    index = -1

    with open(path, encoding="utf-8") as file:
        csv_reader = reader(file, delimiter=delimiter)

        for row in csv_reader:
            if len(labelled_rows) == 0 and index == -1:  # Skip fields row
                index = 0
                continue

            if row not in labelled_rows:
                current_row = row
                break

            index += 1

    return index, current_row


def get_fields_indexes_of_csv_file(path, delimiter, selected_fields, last_labelled_row_index):
    index = 0
    selected_fields_indexes = []
    fields = None
    last_row = None

    with open(path, encoding="utf-8") as file:
        csv_reader = reader(file, delimiter=delimiter)

        for row in csv_reader:
            if not fields:
                fields = row
                for field in selected_fields:
                    selected_fields_indexes.append(fields.index(field))
                continue

            if last_labelled_row_index and index == int(last_labelled_row_index):
                last_row = row
                break

            index += 1

    return fields, selected_fields_indexes, index, last_row

import sys
import os
from csv import reader, writer, field_size_limit
from flask import Flask, render_template, request
from file import *

field_size_limit(sys.maxsize)
CONFIG_PATH = "config.json"


config = parse_config_file(CONFIG_PATH)
app = Flask(__name__)


@app.route("/", methods=["GET"])
def hello_world():
    current_row = None
    delimiter = config["data"]["delimiter"] or ","
    selected_fields = config["interface"]["fields"]
    last_labelled_row_index = request.args.get('index')
    last_label_value = request.args.get('label')
    output_len = 0
    labelled_rows = []

    if os.path.exists(config["data"]["output"]):
        output_len = get_length_of_csv_file(config["data"]["output"])

    fields, selected_fields_indexes, index, last_row = get_fields_indexes_of_csv_file(
        config["data"]["input"], delimiter, selected_fields, last_labelled_row_index)
    fields.append(config["label"]["name"])

    if last_row:
        last_row.append(last_label_value)
        append_row_to_csv_file(
            config["data"]["output"], delimiter, output_len, fields, last_row)

    if os.path.exists(config["data"]["output"]):
        labelled_rows = get_rows_of_csv_file(
            config["data"]["output"], delimiter)
        output_len = get_length_of_csv_file(config["data"]["output"])

    input_len = get_length_of_csv_file(config["data"]["input"])
    progress = output_len * 100 / input_len
    index, current_row = get_first_non_labelled_row(
        config["data"]["input"], delimiter, labelled_rows)
    color = "text-dark"
    if config["interface"]["theme"] == "dark":
        color = "text-light"

    return render_template("interface.html",
                           data=config["data"]["input"],
                           index=index,
                           row=current_row,
                           fields=selected_fields_indexes,
                           fields_names=fields,
                           label_name=config["label"]["name"],
                           label_values=config["label"]["values"],
                           progress=round(progress, 2),
                           count=output_len,
                           total=input_len,
                           theme=config["interface"]["theme"],
                           color=color)

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
    selected_fields = config["interface"]["fields"]
    last_labelled_row_index = request.args.get('index')
    last_label_value = request.args.get('label')
    output_len = 0

    if os.path.exists(config["output"]):
        output_len = get_length_of_csv_file(config["output"])

    fields, selected_fields_indexes, index, last_row = get_fields_indexes_of_csv_file(
        config["input"], selected_fields, last_labelled_row_index)
    fields.append(config["label"]["name"])

    if last_row:
        last_row.append(last_label_value)
        append_row_to_csv_file(config["output"], output_len, fields, last_row)

    labelled_rows = get_rows_of_csv_file(config["output"])
    output_len = get_length_of_csv_file(config["output"])
    input_len = get_length_of_csv_file(config["input"])
    progress = output_len * 100 / input_len
    index, current_row = get_first_non_labelled_row(
        config["input"], labelled_rows)
    color = "text-dark"
    if config["interface"]["theme"] == "dark":
        color = "text-light"

    return render_template("interface.html",
                           data=config["input"],
                           index=index,
                           row=current_row,
                           fields=selected_fields_indexes,
                           fields_names=fields,
                           label_values=config["label"]["values"],
                           progress=round(progress, 2),
                           count=output_len,
                           total=input_len,
                           theme=config["interface"]["theme"],
                           color=color)

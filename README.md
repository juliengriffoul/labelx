# labelx
Web application intending to make manual datasets labelling easier.
<p align="center"><img width="800" src="docs/demo.gif" /></p>

### Project setup
Installing virtual environment:
```
python3 -m pip install --user virtualenv
python3 -m venv env
source env/bin/activate
```
Installing dependencies:
```
make
```
Starting project:
```
make run
```
Labelling interface now available at `http://127.0.0.1:5000`.

### Configuration
Update the `config.json` file to configure project.
```
{
    "input": <path to input csv file>,
    "output": <path where output csv file will be generated>,
    "interface": {
        "fields": <array of fields to display on the interface (["id", "col_a", "col_c"])>,
        "theme": <"light" or "dark">
    },
    "label": {
        "name": <label field name (CSV column name)>,
        "values": [0, 1]
    }
}
```
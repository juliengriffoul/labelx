run:
	FLASK_APP=src/main.py FLASK_ENV=development flask run

setup: requirements.txt
	pip install -r requirements.txt

clean:
	rm -rf __pycache__

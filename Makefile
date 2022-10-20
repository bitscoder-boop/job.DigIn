run:
	python app.py 

setup: requirements.txt
	pip install -r requirements.txt

clean:
	rm -rf __pycache__

# if requirements.txt exists it will run the command
# venv/bin/activate: requirements.txt
# 	python3 -m venv venv
# 	./venv/bin/pip install -r requirements.txt

.PHONY: venv
venv:
	python3 -m venv ./venv; \
        source ./venv/bin/activate; \
	pip install -r requirements.txt; \

.PHONY: run 
run:
	cd src && uvicorn app:app --host 0.0.0.0 --port 9018 --reload	

execute:
	cd src && python3 main.py && cd ..

clean:
	find . -type f -name '*.pyc' -delete

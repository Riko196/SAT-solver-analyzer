execute:
	cd src && python main.py && cd ..

clean:
	find . -type f -name '*.pyc' -delete

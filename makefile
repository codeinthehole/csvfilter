install: clean
	pip install -r requirements.txt
	python setup.py develop

clean:
	find . -name "*.pyc" -delete
	-rm -rf *.egg-info dist

release:
	python setup.py sdist upload
	git push --tags

install: clean
	python setup.py develop
	pip install -r requirements.txt

clean:
	find . -name "*.pyc" -delete
	-rm -rf *.egg-info dist

release:
	python setup.py sdist upload
	git push --tags

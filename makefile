install:
	python setup.py develop
	pip install -r requirements.txt

clean:
	find . -name "*.pyc" -delete
	-rm -rf *.egg-info

release:
	python setup.py sdist upload
	git push --tags

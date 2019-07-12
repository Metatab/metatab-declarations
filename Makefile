.PHONY: default install reset check test tox readme docs publish clean


	
publish: 
	python setup.py sdist 
	twine upload dist/*
	$(MAKE) clean
	

.DEFAULT_GOAL := install

install:
	pip install --upgrade pip
	pip install --editable .[dev]
	make clean
clean:
	rm -rf ./build ./dist ./*.pyc ./*.tgz ./**/*.egg-info
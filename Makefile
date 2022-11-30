all:
	python main.py

vim:
	nvim main.py ./lang_processing/*.py

clean:
	rm -r ./lang_processing/__pycache__/

.PHONY: start format sh_file
LANG = python
PACKAGE_MANAGE = .venv/bin/pip
MAIN_FILE = arco_install.py

start:
	@echo '🏃 Install dependencies'
	${LANG} -m venv .venv
	. .venv/bin/activate
	${PACKAGE_MANAGE} install -r requirements.txt

format:
	@echo '🖊️  Format code'
	@black ${MAIN_FILE} src/

sh_file:
	${LANG} ${MAIN_FILE} -e
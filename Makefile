install:
	@sh arco-install.sh

software:
	@echo '📦 Build software json'
	@sh src/format-software.sh

.PHONY: install software
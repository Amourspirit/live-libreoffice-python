help:
	@echo "Run make build to compile into 'build/buld_table' folder."
	@echo "Run make macro to compile into 'macro/builder.py' file."

.PHONY: build macro help

build:
	oooscript compile --embed --config "$(PWD)/config.json" --embed-doc "$(PWD)/builder.ods" --build-dir "build/buld_table"

macro:
	oooscript compile --config "$(PWD)/config.json" --build-dir "macro"

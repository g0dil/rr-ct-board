install:
	poetry install

build:
	poetry build

clean:
	git clean -dfX

env-clean:
	poetry env list | cut -d' ' -f1 | xargs -n1 -r poetry env remove

gen: rr_ct_board/models.py ctclient/__init__.py

rr_ct_board/models.py: rr_ct_board/openapi.yaml
	poetry run datamodel-codegen \
		--input $< \
		--input-file-type openapi \
		--output $@

ctclient/__init__.py: churchtools-openapi.json
	poetry run poetry run openapi-python-client generate \
		--path churchtools-openapi.json \
		--overwrite \
		--meta=none \
		--config=ctclient-config.yaml

test:
	poetry run pytest

format:
	poetry run black .

run:
	poetry run rr-ct-board

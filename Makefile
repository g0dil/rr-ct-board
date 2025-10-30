install:
	poetry install

build:
	rm -rf dist
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
	poetry run black rr_ct_board

run:
	poetry run uvicorn rr_ct_board.app:main \
		--factory \
		--log-config=log-config.yaml \
		--host=127.0.0.1 \
		--port=8000

image:
	podman build . --tag rr-ct-board

run-image:
	podman run -v `pwd`:/app -p 8000:8000 rr-ct-board \
		--factory \
		--log-config /app/log-config.yaml \
		--host 0.0.0.0 \
		--port 8000

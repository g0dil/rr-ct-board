FROM python:3.10

RUN apt-get update && apt-get install -y tini && apt-get clean
RUN pip install uvicorn
COPY dist/*.whl /
RUN pip install /*.whl && rm -f /*.whl

ENV PATH "/root/.local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/sbin:/usr/bin:/bin"

ENTRYPOINT ["tini", "--", "uvicorn", "rr_ct_board.app:main", "--factory"]

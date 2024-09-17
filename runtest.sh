#!/bin/sh

docker compose exec -e DJANGO_TEST=true movies poetry run pytest -p no:warnings --cov=. --reuse-db




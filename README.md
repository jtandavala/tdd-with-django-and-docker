# Usefull command


# normal run
$ docker compose exec movies pytest

# disable warnings
$ docker compose exec movies pytest -p no:warnings

# run only the last failed tests
$ docker compose exec movies pytest --lf

# run only the tests with names that match the string expression
$ docker compose exec movies pytest -k "movie and not all_movies"

# stop the test session after the first failure
$ docker compose exec movies pytest -x

# enter PDB after first failure then end the test session
$ docker compose exec movies pytest -x --pdb

# stop the test run after two failures
$ docker compose exec movies pytest --maxfail=2

# show local variables in tracebacks
$ docker compose exec movies pytest -l

# list the 2 slowest tests
$ docker compose exec movies pytest --durations=2
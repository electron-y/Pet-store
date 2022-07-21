#!/bin/bash
# single run: pytest -v -rEf -m "smoke" -c pytest.ini
#             pytest -v -rEf -m "not smoke" -c pytest.ini
#
# run from sh file:
#             pipenv run sh run.sh smoke 1
#             pipenv run sh run.sh regression 1


if [ "$1" = smoke ]
then
    echo 'smoke'
    pytest -v -rEf -m "smoke" -c pytest.ini
    m1=$?

elif [ "$1" = regression ]
then
    echo 'regression'
    pytest -v -rEf -m "not smoke" -c pytest.ini
    m1=$?

fi

if [ "$m1" != 0 ]
    then
        echo "Some tests failed"
        exit 1
    else
        echo "All tests passed successfully"
fi

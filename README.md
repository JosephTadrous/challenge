# Challenge
This directory includes a script that combines csv files into one file with an added column representing the file name.

## Running the program
An example of how to use the script:

`python3 csv-combiner.py ./tests/real-madrid.csv ./tests/liverpool.csv ./tests/man-city.csv > output.csv`

The arguments of the program represent the csv files that needs to be combined. You can enter as many csv files as wanted.

## Testing the program
Some unit tests are included in the directory. Run using the following command:

`python3 ./tests/unit_tests.py`

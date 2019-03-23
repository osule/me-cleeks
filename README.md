# Me-Cleeks

A sample command line application exploring the [click command application library](http://click.palletsprojects.com)
for unit tested commands.

The [testing documentation in the click project](http://click.palletsprojects.com/en/7.x/setuptools/#testing-the-script) how to perform integration testing of commands.

This sample application explores where you only care about testing the command functions directly.
It is written in the latest and greatest **Python3**.

## Install

Install the application by cloning this repository with the following command.

    git clone git@github.com:osule/me-cleeks.git

Then install the application dependencies.

    pip install -r requirements.txt


## Test

Run the unit tests for the commands.

    pytest tests

## Run

Finally, run the application in your terminal with:

    python cli.py


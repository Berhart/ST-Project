# ST-Project
##How to run the game?
```
python3 Hangman_class_version.py
```
##How to execute the test suite?
```
python3 -m unittest -b -v TestingSuite.py
```
##How to calculate the code coverage?
To calculate the code coverage, a new package needs to be installed. To install the package, run the following command on shell:
```
pip3 install coverage
```
Then run the following to see coverage report:
```
coverage3 run -m unittest -b -v TestingSuite.py
coverage report
```
To have a visual look at how much of the code is actually traversed, generate a HTML report:
```
coverage html
```
This will create a folder at the current working directory with the name "htmlcov". Inside this folder there would be a file named "index.html". Open this file in any browser to have a visual overview of the coverage.
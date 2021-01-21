<h1 align="left">:computer: Technical_Challenge_Coodesh  </h1>

Technical Challenge resolution for Coodesh

## Introduction
This project contains an automated test suite for the Coodesh Technical Challenge related to the Beta Coodesh website. 

The test suite contains 5 functional test cases automated using Selenium and Python on a Page Object design. 

## Test Suite

* Load Home Page
* Navigate to positions
* Search positions
* Open specific position
* Position Enrollment


## Environment Setup
**Prerequisites:** 
* Python 3+ 
* pip3
* Chrome webdriver
* Update the driver in the root folder with the version of the browser on which you want to run the tests or set in the PATH (if using Windows).

Check the webdriver documentation:
- Chrome: https://chromedriver.chromium.org/getting-started


1. Clone the project

2. Create and activate a virtualenv:
```
virtualenv --python=/usr/bin/python3.7 automation_suite 
```
```
source automation_suite/bin/activate
```

3. To install the required dependencies issue the below command in project root directory.
```
pip3 install -r requirements.txt
```

Currently supported browsers:
- Chrome


## How to run?

Run one test case or the whole suite using Chrome web browser.

- Run the suite:

Load the project on PyCharm or other Python IDE and hit the green arrow to run the suite on Tests.py

Another option is to issue the below commands in project root directory
```
python3 Tests.py
```

- Run specific test cases: 

Load the project on PyCharm or other Python IDE and hit the green arrow to run a specific test on Tests.py

Or Issue the below commands in project root directory
```
python3 -m unittest testAll.TestContact.TEST_NAME
```
_Example: python3 -m unittest testAll.TestContact.test_send_message_with_empty_text_

The webdrivers were set to run headless, if you need to watch the execution, please, comment the line 12 on Tests.py.


## Author
<a target="_blank" href="https://github.com/diegohdb/diegohdb">👤 Diego Bezerra </a>

<a target="_blank" href="https://www.linkedin.com/in/diegohdb/">
  <img align="left" alt="LinkdeIN" width="22px" src="https://cdn.jsdelivr.net/npm/simple-icons@v3/icons/linkedin.svg" />
</a>
<a target="_blank" href="https://www.instagram.com/diegohdb/">
  <img align="left" alt="Instagram" width="22px" src="https://cdn.jsdelivr.net/npm/simple-icons@v3/icons/instagram.svg" />
</a>
<a target="_blank" href="mailto:diegohdb@gmail.com">
  <img align="left" alt="Gmail" width="22px" src="https://cdn.jsdelivr.net/npm/simple-icons@v3/icons/gmail.svg" />
</a>



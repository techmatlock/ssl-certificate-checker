# Python Web App SSL Checker

## Description
Python script to fetch SSL certificate data, return expiration dates, display HTML data, and much more.

## Demo
<img width="1567" alt="Screenshot 2023-11-26 at 7 39 01 PM" src="https://github.com/techmatlock/ssl-certificate-checker/assets/2618095/2363373c-f032-427a-958d-22d69bb13a23">

## Prerequisites
* Python <= 3.10.12 
* pip <= 22.3.1
* Docker Engine <= 24.0.7

## Installation
1. Clone this repository to your local machine.
```
git clone https://github.com/techmatlock/ssl-certificate-checker.git
```
2. On your local machine in the project directory, initialize your virtual environment. ```python -m venv venv```
3. Install the required packages: ```pip install -r requirements.txt```
4. Export DNS A records from Windows DNS or other DNS provider.
5. Format records so they look like the example in the websites/ folder.
6. (Optional) If you choose to run manually on your local machine, run the following:
   * Run the preprocess_data.py to generate the JSON files.
   * Once the files are generated, run: flask --app main run
   * Navigate to browser and go to localhost:<portnumber>

## Usage

* (Optional) You can configure GitLab CICD (with .gitlab-ci.yml file) to build the Docker container 
   or you can run the app standalone.
* The Failures section is for any websites that were unreachable by the program. Unreachable failures could be for reasons 
  including: A record exists but not pointed to any host.  Or special authentication methods (i.e. Mutual TLS, SSO).
* The cronjob runs the preprocess_data.py module every night at 11:59PM. preprocess_data.py is the module that collects all the SSL certificate data.
* (Optional) route53.py can be run separately if you have A records in AWS Route53.

## Contributing
Contributions to this project are welcome. Please fork the repository and submit a pull request.

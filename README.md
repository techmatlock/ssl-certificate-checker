# Python Web App SSL Checker

## Description
This projects aims to fetch SSL certificates using socket connections and then append the returned information to a list.  Python Flask handles the backend and renders an HTML template.

## Demo

![Screen Recording 2023-11-25 at 5 02 14 PM](https://github.com/techmatlock/ssl-certificate-checker/assets/2618095/cce7dc09-65b3-43f6-9611-71d27f82c9ec)

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
   * Run the preprocess_data.py to generate JSON (.json) files.
   * Once the files are generated, run: flask --app main run
   * Navigate to browser and go to localhost:<portnumber>

## Usage

* (Optional) You can either configure GitLab CICD to build the Docker container (with .gitlab-ci.yml file) 
   or you can run the app manually.
* When you go to the Flask app in the browser, the Failures section is for any websites 
   that were unreachable by the program.  The cronjob runs the preprocess_data.py module every night at 11:59PM.  
   preprocess_data is the module that collects all the SSL certificate data.
   Unreachable failures could be for reasons including: A record exists but not pointed to any host.  Or special authentication methods (i.e. Mutual TLS, SSO).
* (Optional) route53.py can be run separately if you have A records in AWS Route53.

## Contributing
Contributions to this project are welcome. Please fork the repository and submit a pull request.

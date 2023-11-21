# Python Web App SSL Checker

## Description
This projects aims to fetch SSL certificates using socket connections and then append the returned information to a list.  Python Flask handles the backend routing and renders an HTML template.

## Demo

## Prerequisites
* Python <= 3.10.12 
* pip <= 22.3.1
* Docker Engine <= 24.0.7

## Installation
Fork this repository.

1. Install packages - pip install -r requirements.txt
2. Export DNS A records from Windows DNS or other DNS provider.
3. Format records so they look like the example in the websites/ folder.
4. The cronjob runs the preprocess_data.py module every night at 11:59PM.  
   preprocess_data is the module that collects all the SSL data to display on the frontend.
5. (Optional) route53.py can be run separately if you have A records in AWS Route53.

## Usage

1.  You can either let GitLab build the Python via CICD (with .gitlab-ci.yml file) or you can run the app manually.
2. (Optional) If you choose to run manually on your local machine, run the following:
   1. Run the preprocess_data.py to generate JSON (.json) files.
   2. Once the files are generated, run: flask --app main run
   3. Navigate to browser and go to localhost:5000
3. When you go to the Flask app in the browser, the Failures section is for any websites that were unreachable by the program.
   Unreachable could be for reasons including: A record exists but not pointed to any host.  Or special authentication methods (i.e. Mutual TLS, SSO).

## Configuration

## Contributing
Contributions to this project are welcome. Please fork the repository and submit a pull request.

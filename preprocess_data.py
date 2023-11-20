import socket, ssl, threading
from datetime import datetime
from send_email import send_email
import json, os, csv

def format_date(cert):
    """Take certificate date and return formatted expiration date."""
    input_format = "%b %d %H:%M:%S %Y %Z"

    # Parse the input string into a datetime object
    date_time_obj = datetime.strptime(cert, input_format)

    # Format the datetime object into the desired output format
    expiry_date = date_time_obj
    current_date = datetime.utcnow()
    remaining_days = (expiry_date - current_date).days

    output_format = "%d %B %Y %I:%M %p"
    expiry_date = expiry_date.strftime(output_format)
    return expiry_date, remaining_days

def get_server_certificate(domain, results, exceptions):
    """Fetch certificate. Return domain and ssl certificate expiration."""
    try:
        context = ssl.create_default_context()
        context.set_ciphers(':HIGH:!DH:!aNULL')
        with socket.create_connection((domain, 443), timeout=5) as sock:
            with context.wrap_socket(sock, server_hostname=domain) as conn:
                cert = conn.getpeercert()  # Fetch the certificate
                expiry_date, remaining_days = format_date(cert["notAfter"])
                results.append((domain, expiry_date, remaining_days))
                results.sort(key=lambda x: x[2]) #Sort list by third element (remaining_days) in each tuple
        return results, exceptions
    except socket.gaierror as e:
        print(f"Error connecting to domain {domain}: {str(e)}")
        exceptions.append(f"Error connecting to domain {domain}: {str(e)}")
    except Exception as e:
        print(f"Other error connecting to domain {domain}: {str(e)}")
        exceptions.append(f"Other error connecting to domain {domain}: {str(e)}")
         
def extract_list():
    """Extract websites from text file(s) and append to list."""
    all_domains = []

    directory = './websites'
    files = os.listdir(directory)
    all_files = [f for f in files if f.endswith('.txt')]

    for file in all_files:
        file_path = os.path.join(directory, file)
        with open(file_path, "r") as file:
            lines = file.readlines()
            for line in lines:
                stripped_lines = line.strip()
                all_domains.append(stripped_lines)
    return all_domains

def generate_csv():
    with open('domain_list.json', 'r') as file:
        data = json.load(file)

    headers = ["Domain", "Expiration Date", "Remaining Days"]

    with open('output.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(headers)
        writer.writerows(data)

def main():
    all_domains = extract_list()

    results = []
    exceptions = []
    for domain in all_domains:
        t1 = threading.Thread(target=get_server_certificate, args=(domain,results,exceptions))
        t1.start()
        t1.join()

    with open('domain_list.json', 'w') as json_file:
        json.dump(results, json_file)
    
    with open('exception_list.json', 'w') as json_file:
        json.dump(exceptions, json_file)
    
    generate_csv()
    
    email_sent = False
    for _, _, remaining_days in results: #Only check remaining_days element in tuple list
        if remaining_days < 60 and not email_sent:
            send_email()
            email_sent = True

if __name__ == '__main__':
    main()

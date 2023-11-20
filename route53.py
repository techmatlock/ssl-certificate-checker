"""This script is only used to extract A records from AWS Route53 if you have
    records that exist outside internal DNS.  You need to copy + paste printed
    results to a text (.txt) file and add to the websites folder.
"""
import boto3

client = boto3.client('route53')
paginator = client.get_paginator('list_resource_record_sets')

def get_preprocessed_data():
    """Iterate through source_zone_records dictionary. Return list with only A record name(s)."""
    processed_list = []
    try:
        source_zone_records = paginator.paginate(HostedZoneId='')
        for record_set in source_zone_records:
            for record in record_set['ResourceRecordSets']:
                if record['Type'] == 'A':
                    # Remove the last character (.) of the record['Name'] and add to the processed list
                    processed_list.append(record['Name'][:-1])
    except Exception as error:
        print('An error occurred getting source zone records:')
        print(str(error))
        raise
    return processed_list

results = get_preprocessed_data()

stripped_str = '\n'.join(results)
print(stripped_str) #Only needed to grab A records that are generated in a list format

import requests
import csv

# Replace with your actual access token and community ID (from URL) you plan to query. 
# Note: do not share the token with the code.
ACCESS_TOKEN = 'access_token'
COMMUNITY_ID = 'community_id'

# Prompt for the CSV file name
csv_file = input("Enter the name for the CSV file (with .csv extension): ")

# Define the API endpoint without any filtering
url = f"https://zenodo.org/api/records/?communities={COMMUNITY_ID}"

# Initialize variables for pagination
all_records = []
page = 1
size = 100  # Number of records per page

while True:
    # Make the request with pagination
    response = requests.get(url, params={'access_token': ACCESS_TOKEN, 'page': page, 'size': size})
    
    if response.status_code == 200:
        data = response.json()
        records = data['hits']['hits']
        all_records.extend(records)
        
        # Check if there are more records to fetch
        if len(records) < size:
            break
        else:
            page += 1
    else:
        print(f"Error: {response.status_code}")
        break

# Define CSV headers
headers = ['Title', 'Publication Date', 'DOI', 'Creators', 'Abstract']

# Open the CSV file for writing with '|' as a separator
with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file, delimiter='|')
    
    # Write the headers
    writer.writerow(headers)
    
    # Write the record data
    for record in all_records:
        title = record['metadata'].get('title', 'N/A')
        publication_date = record['metadata'].get('publication_date', 'N/A')
        doi = record['metadata'].get('doi', 'N/A')
        creators = ', '.join([creator['name'] for creator in record['metadata'].get('creators', [])])
        abstract = record['metadata'].get('description', 'N/A')
        
        writer.writerow([title, publication_date, doi, creators, abstract])

print(f"Records have been saved to {csv_file}")

# Print the total number of records
number_of_records = len(all_records)
print(f"The total number of records in the community '{COMMUNITY_ID}' is {number_of_records}. It should match the number of lines in your CSV file.")
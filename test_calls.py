import os
import requests
from dotenv import load_dotenv

load_dotenv()

# Set your OpenSecrets API key here
api_key = os.getenv('OPEN_SECRETS_KEY')

def get_politicians():
    # Get politicians with getLegislator method
    response = requests.get(f'http://www.opensecrets.org/api/?method=getLegislators&id=NJ&apikey={api_key}&output=json')

    print(response.json())

# get_politicians()

# print("**************************")

def top_ten_donors(crp_id):
    response = response = requests.get(
            f'http://www.opensecrets.org/api/?method=candContrib&cid={crp_id}&cycle=2020&apikey={api_key}&output=json'
        )
    
    # Check that the request was successful
    if response.status_code == 200:
        # Retrieve the list of top donors from the response JSON
        top_donors = response.json()['response']['contributors']['contributor']
        # print(top_donors)
        print(top_donors[:10])

        # Print the top 10 donors and their contribution amounts
        print('Top donors for the politician:')
        for donor in top_donors[:10]:
            print(f"{donor['@attributes']['org_name']}: ${donor['@attributes']['total']}")
        return top_donors
    else:
        print(f"Error retrieving data: {response.status_code}")

top_ten_donors("N00035267")
import requests
import json  # Import the json library to use `json.dumps`

# Replace this with the actual API endpoint URL from your CloudFormation output
api_url = "https://exprl07kaj.execute-api.us-east-1.amazonaws.com/Prod/get"

def call_hello_world_api():
    try:
        # Make a GET request to the API endpoint
        response = requests.get(api_url)
        
        # Check if the request was successful
        if response.status_code == 200:
            print("API Response:", response.json())
        else:
            print(f"Failed to call API. Status Code: {response.status_code}")
            print("VisitorCount:", response.text[-1])

    except Exception as e:  
        print(f"An error occurred: {e}")

    # Lambda response with CORS headers and a dummy body for testing
    return {
        "headers": {
            "Access-Control-Allow-Origin": "*",  # Allow requests from any domain
            "Access-Control-Allow-Methods": "*",  # Allow all HTTP methods (GET, POST, etc.)
            "Access-Control-Allow-Headers": "*"  # Allow all headers
        },
        "statusCode": 200,
        "body": json.dumps({
            "message": "Visitor Count",
            "count":  2 # Dummy data for testing
        }),
    }

if __name__ == "__main__":
    call_hello_world_api()
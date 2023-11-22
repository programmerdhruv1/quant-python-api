from flask import Flask, jsonify,request
import requests
import json


app = Flask(__name__)

@app.route('/customerDetails', methods=['GET'])
def get_customer_details():
    
    # Retrieve SessionToken and AppKey from request form data
    session_token = request.args.get('SessionToken')
    print("fkd55656555jsklfjdsd")
    print(session_token)
    app_key = request.args.get('AppKey')
    url = "https://api.icicidirect.com/breezeapi/api/v1/customerdetails"

    payload = {
    "SessionToken":session_token,
  "AppKey": app_key
    }
    print(json.dumps(payload))
    headers = {
  'Content-Type': 'application/json',
  'Cookie': 'AlteonAPI=CffwNsdBEKyuNEEMtOfNMA$$; nginx_srv_id=f42f4592ab0c731e8c7a9c000e57162e'
}
     # Make the GET request
    response = requests.get(url, headers=headers, data=json.dumps(payload))

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Return the response as JSON
        return jsonify(response.json())
    else:
        # Return an error message if the request was not successful
        return jsonify({"error": f"Error: {response.status_code}", "message": response.text})


if __name__ == '__main__':
    app.run(debug=True)
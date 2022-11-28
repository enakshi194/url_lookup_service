# **Malware URL lookup service** 

This is a microservice written using Python, Flask and PyMongo to check if a given URL is malware or not. 
The service queries a database containing a list of urls, to verify if the URL is malware.

## DB Design
We are using MongoDB clustered server for data storage. This is a cloud based DB that is hosted on AWS.

**Table Name:** *malware.urls*

| Field | Type       | Null     | Key         | Default | Extra           |
|-------|------------|----------|-------------|---------|-----------------|
| _id   | ObjectID   | NOT NULL | Primary Key |         |                 |
| url   | string     | NOT NULL |             |         |                 |

**Table Access:**
The mongodb can be accessed using the application. No additional database creation is required from the user end.

## Instructions to build and run:- 
### Requirements:-
- Python 3.8+
- pip


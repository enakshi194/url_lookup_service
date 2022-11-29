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

### Instructions:-
1. Clone the project- `git clone https://github.com/enakshi194/url_lookup_service.git`
2. Go into the project folder- `cd  url_lookup_service`
3. Install Dependent python modules - `pip install - requirements.txt`
4. Run the app- `python run.py`

### API Documentation:-
1. **Get Url Info:** 

*GET* :  `/v1/urlinfo/malware_url?url=<url string>`

**Response**: 
True indicates url is malware, False indicates url is not malware
```
{data: True/False}, success_code
```
**Examples **: 
```
http://127.0.0.1:5000/v1/urlinfo/malware_url?url=http://222.138.204.18:39382/Mozi.m
```

2. **Insert Url Details** 

*POST* : `/v1/urlinfo/add_url?url=<url string>`

**Response**: 
True indicates url is successfully added, False indicates url is not successfully updated
```
{data: True/False}, success_code
```
**Examples **: 
```
http://127.0.0.1:5000/v1/urlinfo/add_url?url=http://222.138.204.18:39382/Mozi.m
```


### Bonus implementations:

1. The size of the URL list could grow infinitely, how might you scale this beyond the
memory capacity of the system? : The db has been implemented as a shared cluster using Mongo Atlas. This eradicates any memory capacity issues since the db cluster auto scales.

2. The number of requests may exceed the capacity of this system: Solution of this is to create a hosted service on cloud since flask’s built in server is not suitable for production. The application is packaged as a container image and run on google cloud. This solves system capacity limitation.  

3. What are some strategies you might use to update the service with new URLs? To decrease the number of write operations for adding new urls a queue has been implemented. When a request to add a new url is fired the url gets added in the queue. Once the queue is of a certain size i.e. 200 urls a bulk write is performed in the db. Hence for 5000 url entries distributed evernly over a day i.e.  a total of 5000/200 i.e. 25 writes are performed. Also this queue is queried to check if a malware url exists that is not present in database. In future the queue size can be left configurable to improve efficiency based on traffic.

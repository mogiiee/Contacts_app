# SwiftSKU Task

## Project Goal
Task is to create a simple phone book application with CRUD operations. You can use any front-end framework you want (e.g. React, Angular, Vue.js, etc.). For the back-end, you can use the language (Python, Node.js, etc.) and framework (Django, Flask, FastAPI for Python, Express for Node, etc.) of your choice as well along with the database (MySQL, PostgreSQL, MongoDB, etc.).

Your application should provide a form where you can enter in first name, last name, and phone number. You should then be able to perform 4 basic operations: create new entries in your database, read the entries, update entries by editing any of the properties, and delete the entries. 

## What I did:
- Well as a backend dev, I did exactly what I was told to do plus a little extra. The entire project has been Dockerized and is deady to go with 1 simple command.
- The app has also been hosted on Heroku, but as a student I use the free version. The Hosted app may not work from 25th to 31st of every month (end of the month) as I run out of credits :/
- This Readme will contain instuctions to use
    - How to run the docker container and run the server on port 8000

    - How to run the file locally without docker

    - How to use the hosted app and access enpoints

- As my expertise lies in Backend dev only, to work around the UI creation part I have used the help of [uvicorn swagger](https://www.uvicorn.org/) to create a "near-frontend-experience" like this using FastAPI

![alt-text](https://cdn.discordapp.com/attachments/991052554802712586/991225629301297162/Screenshot_2022-06-28_at_11.46.38_AM.png)

## Environment Variables In .env.sample

To run this project, you will need to add the following environment variables to your .env file

`CLUSTER`=

`DB`=

`COLLECTION`=

which you can get from your [mongodb](mongodb.com)

## BUILD INSTRUCTIONS

Simple Installaton

- clone the repository
```
git clone https://github.com/mogiiee/Contacts_app.git
``` 

- Create a Virtualenv with 
```
python3 -m venv virtualenv
```
- activate virtual env 

```
source virtualenv/bin/activate
```


- build the container locally
```
docker-compose up
```

should be able to see something like this
![](https://cdn.discordapp.com/attachments/991052554802712586/991229146376183848/Screenshot_2022-06-28_at_12.00.35_PM.png)

If done, skip DOWN to "Operating the endpoints on Swagger"
# Running the app without docker

- Create a Virtualenv with 
```
python3 -m venv virtualenv
```
- activate virtual env 

```
source virtualenv/bin/activate
```

- clone the repository
```
git clone https://github.com/mogiiee/Contacts_app.git
``` 
- Install requirements.txt

```
pip3 install -r requirements.txt
```
- run the server

```
uvicorn app.main:app --reload
```
If done, skip DOWN to "Operating the endpoints on Swagger"
# Running the file from the hosted server
Note
- You would not be needing to populate the .env file as it will be linked to my personal Mongodb. Please dont spam 😂

head over to 

```
https://contact-backend1.herokuapp.com/docs

```


# Operating the endpoints on Swagger

Once the server starts head over to (if you followed the first or sevond steps)

```
http://127.0.0.1:8000/docs
```
Here you would be greeted with 6 endpoints like 

![alt-text](https://cdn.discordapp.com/attachments/991052554802712586/991225629301297162/Screenshot_2022-06-28_at_11.46.38_AM.png)

Lets go over them one by one (click on Try it out and then click on execute to use the endpoint)

 - Root file gives you an amazing greeting!
 - Inserter using a post method can insert data into your mongodb 

 ![](https://cdn.discordapp.com/attachments/980468845519175743/991049725077758022/Screenshot_2022-06-28_at_12.07.40_AM.png)

 - get_all_data enpoint using the "get" method, gets all the data from the database as a JSON.

 ![](https://cdn.discordapp.com/attachments/980468845519175743/991050005282455562/Screenshot_2022-06-28_at_12.08.47_AM.png)
 
 - updater enpoint being a path method, it can update a contact given the objectID 

 ![](https://cdn.discordapp.com/attachments/980468845519175743/991050821569491015/Screenshot_2022-06-28_at_12.12.01_AM.png)

 - Search function takes in a query which can search in all 3 fields of "first_name", "last_name" and "phone_number" and returns in a paginated response

 ![](https://cdn.discordapp.com/attachments/991052554802712586/991227669830185000/Screenshot_2022-06-28_at_11.54.39_AM.png)

 - deleter endpoint can delete a contact given the objectID of the contact 

 ![](https://cdn.discordapp.com/attachments/980468845519175743/991051237988397126/Screenshot_2022-06-28_at_12.13.41_AM.png)

 - Finally delete_all endpoint can wipe out all data in the database clean. A RESET button of sorts.

# Notes
- In the inserter and updater endpoint, enter the parameters only inside the "string" field and leave the rest alone. Keep it in the form of a dictionary (JSON) only.

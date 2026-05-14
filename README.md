# CallManager
A simple Flask API for managing call logs and notes. This project uses PostgreSQL and is built to run entirely in Docker.

### Getting Started

You will need Docker and Docker Compose installed.

Clone the repository
```
git clone https://github.com/pipos4k/CallManager.git
cd CallManager
```
Setup your environment:
- Create a .env file based on .env.example file, and fill your credentials.

Run the application: 
- ```docker compose up --build```

- The dummy builder will create some data automatically. 

The API will be available at http://localhost:8080.
### Endpoints:

    GET /calls - Get all calls that are not archived.

    GET /calls/<callId> - Get a specific call by ID.

    PUT /calls/<callId>/archive - Archive a call.

#### About
This is a lightweight backend service for logging and managing voice calls, including note-taking capabilities and call archiving.

**More features will be added soon.**

Created for the <a href="https://www.devready.gr/" target="_blank">DevReady Bootcamp</a>.

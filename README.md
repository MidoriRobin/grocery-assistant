# Grocery Assistant
A project to set up an online grocery shopping platform with a strong user recommendation system.


### Running the application

1. Clone the repo
  ```
  $ git clone https://github.com/MidoriRobin/grocery-assistant.git
  $ cd grocery-assistant
  ```

#### Backend

2. Initialize and activate a virtualenv(from the terminal):
  ```
  $ python3 -m venv venv(you only need to do this the very first time)
  $ .venv/scripts/activate
  ```

3. Install the dependencies:
  ```
  $ pip install -r requirements.txt
  ```

5. Run the development server:
  ```
  $ python3 run.py
  or
  $ python run.py
  ```


#### Frontend

6. (In a different terminal) Navigate to the "frontend" directory and install dependencies 
  ```
  $ cd frontend (from grocery-assistant directory)
  $ npm install (installing all the frontend dependencies, and setting up the project, also only needs to be done once)
  ```
  
7. Run and serve the frontend
  ```
  $ npm run serve (running the application)
  ```

8. Navigate to [http://localhost:8080](http://localhost:8080)

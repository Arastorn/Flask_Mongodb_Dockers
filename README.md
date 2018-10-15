# Flask_Mongodb_Dockers

A docker compose project which will run a flask server connected to a mongodb database. The frontpage look the same as the one we made in our cloud_database course.

# Start the project :

  - Go to server directory : 'cd server'
  - Launch 'docker-compose up'
  - To see the web interface you can go on 'http://0.0.0.0:4000/' once the containers are running

# Details

  - Flask :
    - Acess : '0.0.0.0:4000'
    - Simple application connected with mongodb container
    - Container name: web_dev
  - Mongodb:
    - Ports: '27017:27017'
    - Mongodb Database connected with another mongodb container which import the data (mongo-seed)
  - Mongo-seed:
    - A simple container which wait that all the containers are running to send data to Mongodb database.

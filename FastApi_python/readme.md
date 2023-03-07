# FastApi introduction: Path operations, validations and authentication.

# Movie API using FastAPI
This API manages a list of movies and allows users to retrieve a list of movies, retrieve a single movie by its id, retrieve a list of movies by category, and add a new movie to the list.

# Dependencies
Python 3.6+
FastAPI
uvicorn
# Installation
Clone the repository
Install the dependencies using pip install -r requirements.txt
Run the server using uvicorn main:app --reload
# Endpoints
The API has the following endpoints:

Home
GET /
Returns a welcome message as an HTML response. The message includes a title and a list of news items.

Get all movies
GET /movies/
Returns a list of all movies.

Get movie by id
GET /movies/{id}
Returns a single movie with the specified id. If the movie is not found, an empty list is returned.

Get movies by category
GET /movies
Returns a list of movies filtered by the specified category.

Add new movie
POST /movies
Takes in a new movie as a request body and adds it to the list of movies.

# Usage
To use the API, send requests to the appropriate endpoint using a tool like curl or an API client like Postman.

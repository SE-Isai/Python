from fastapi import FastAPI, Body
from fastapi.responses import HTMLResponse, JSONResponse
from pydantic import BaseModel, Field
from typing import Optional


app = FastAPI()
app.title = "Mi primera aplicación con FastAPI"
app.version == "0.0.1"

class Movie(BaseModel):
    id: Optional[int] = None
    title: str = Field(default = 'Mi pelicula', min_lenght=5, max_lenght=15)
    overview: str = Field(default = 'Descripcion de la pelicula', min_lenght=15, max_lenght=50)
    year: int = Field(default = 2022, Le=2022)
    rating: float
    category: str


movies = [
    {
        'id': 1,
        'title': 'Avatar',
        'overview': "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
        'year': '2009',
        'rating': 7.8,
        'category': 'Acción'    
    },
    {
        'id': 2,
        'title': 'Infierno',
        'overview': "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
        'year': '2009',
        'rating': 7.8,
        'category': 'Narcos'    
    } 
]


@app.get("/", tags=["home"])

def message():
    html_content = """
    <!DOCTYPE html>
    <html>
      <head>
        <title>My FastAPI Website</title>
      </head>
      <body>
        <h1>Welcome to My FastAPI Website!</h1>
        <p>Here's some news:</p>
        <ul>
          <li>News item 1</li>
          <li>News item 2</li>
          <li>News item 3</li>
        </ul>
      </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)

@app.get("/movies/", tags=["movies"])

def get_movies():
    return JSONResponse(content = movies)

@app.get("/movies/{id}", tags=["movies"])
def get_movie(id: int):
    for item in movies:
        if item ["id"] == id:
            return JSONResponse(content = item)
    return JSONResponse(content = [])

@app.get("/movies", tags=["movies"])
def get_movies_by_category(category:str):
    data = list(filter(lambda item: item['category'] == category , movies))
    return JSONResponse(content = data)


@app.post("/movies", tags=["movies"])
def create_movie(movie: Movie):
    movies.append(movie.dict())
    return JSONResponse(content = {"message": "Se ha registrado la pelicula"})

@app.put("/movies/{id}", tags=["movies"])
def update_movie(id: int, movie: Movie):
    for item in movies:
        if item ["id"] == id:
            item["title"] = movie.title
            item["overview"] = movie.overview
            item["year"] = movie.year
            item["rating"] = movie.rating
            item["category"] = movie.category
            return JSONResponse(content = {"message": "Se ha modificado la pelicula"})
        else:
            return "ID no encontrado"

@app.delete("/movies/{id}", tags=["movies"])
def delete_movie(id : int):
    for item in movies:
        if item ["id"] == id:
            movies.remove(item)
    return JSONResponse(content = {"message": "Se ha eliminado la pelicula"})


        

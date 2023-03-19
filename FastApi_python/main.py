from fastapi import Depends, FastAPI, Body, HTTPException, Path, Query, Request
from fastapi.responses import HTMLResponse, JSONResponse
from pydantic import BaseModel, Field
from typing import Optional, List
from jwt_manager import create_token, validate_token
from fastapi.security import HTTPBearer


app = FastAPI()
app.title = "Mi primera aplicación con FastAPI"
app.version == "0.0.1"

class JWTBearer(HTTPBearer):
    async def __call__(self, request: Request):
        auth = await super().__call__(request)
        data = validate_token(auth.credentials)
        if data['email'] != "admin@gmail.com":
            raise HTTPException(status_code=403, detail="Credenciales son invalidas")

class User(BaseModel):
    email : str
    password: str

class Movie(BaseModel):
    id: Optional[int] = None
    title: str = Field(min_lenght=5, max_lenght=15)
    overview: str = Field(min_lenght=15, max_lenght=50)
    year: int = Field(le=2022)
    rating: float = Field(ge=0,le=10)
    category: str = Field(min_lenght=5, max_lenght=15)

    class Config:
        schema_extra = {
            'example':{
            'id':1,
            'title':'Mi pelicula',
            'overview': 'Descripcion de la pelicula',
            'year':2022,
            'rating': 9.0,
            'category': 'Accion'
            }
        }


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


@app.post('/login', tags = ['auth'])
def login(user: User):
    if user.email == 'admin@gmail.com' and user.password == '12345':
        token: str = create_token(user.dict())
        return JSONResponse(status_code=200,content=token)

@app.get('/movies/', tags=['movies'], response_model=List[Movie], status_code=200, dependencies=[Depends(JWTBearer())])
def get_movies() -> List[Movie]:
    return JSONResponse(status_code=200, content=movies)

@app.get("/movies/{id}", tags=["movies"], response_model=Movie)
def get_movie(id: int = Path(ge=1, le = 200)) -> Movie:
    for item in movies:
        if item ["id"] == id:
            return JSONResponse(content = item)
    return JSONResponse(status_code=404,content = [])

@app.get("/movies", tags=["movies"], response_model=List[Movie])
def get_movies_by_category(category: str = Query(min_length=5, max_length = 15)) -> List[Movie]:
    data = list(filter(lambda item: item['category'] == category , movies))
    return JSONResponse(content = data)


@app.post("/movies", tags=["movies"], response_model=dict, status_code=201)
def create_movie(movie: Movie) -> dict:
    movies.append(movie.dict())
    return JSONResponse(status_code = 201,content = {"message": "Se ha registrado la pelicula"})

@app.put("/movies/{id}", tags=["movies"], response_model=dict,status_code=200)
def update_movie(id: int, movie: Movie)-> dict:
    for item in movies:
        if item ["id"] == id:
            item["title"] = movie.title
            item["overview"] = movie.overview
            item["year"] = movie.year
            item["rating"] = movie.rating
            item["category"] = movie.category
            return JSONResponse(status_code=200,content = {"message": "Se ha modificado la pelicula"})
        else:
            return "ID no encontrado"

@app.delete("/movies/{id}", tags=["movies"], response_model=dict,status_code=200)
def delete_movie(id : int)-> dict:
    for item in movies:
        if item ["id"] == id:
            movies.remove(item)
    return JSONResponse(status_code=200, content = {"message": "Se ha eliminado la pelicula"})


        

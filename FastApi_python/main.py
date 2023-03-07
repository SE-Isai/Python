from fastapi import FastAPI, Body
from fastapi.responses import HTMLResponse


app = FastAPI()
app.title = "Mi primera aplicación con FastAPI"
app.version == "0.0.1"


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
    return movies

@app.get("/movies/{id}", tags=["movies"])
def get_movie(id: int):
    for item in movies:
        if item ["id"] == id:
            return item
    return []

@app.get("/movies", tags=["movies"])
def get_movies_by_category(category:str):
    return list(filter(lambda item: item['category'] == category , movies))

@app.post("/movies", tags=["movies"])
def create_movie(id: int = Body(), title:str= Body(), overview:str= Body(), year:str= Body(), rating:float= Body(), category:str= Body()):
    movies.append({
        "id":id,
        "title":title,
        "overview":overview,
        "year":year,
        "raiting":rating,
        "category":category
    })
    return "Listado actualizado"

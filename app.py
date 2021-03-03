from fastapi import FastAPI, Request,Body
import uvicorn
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from router import user

app = FastAPI()

app.include_router(
    user.router,
    prefix='/users',
    tags= ['users'],
    responses={
        401: {'description': 'error'}
    }
)


app.mount('/static', StaticFiles(directory='static'), name='static')
templates = Jinja2Templates(directory='templates')

@app.get('/index')
async def index(request: Request):
    return templates.TemplateResponse('index.html', context={'request':request})



if __name__ == "__main__":
    uvicorn.run("app:app", debug=True)

    
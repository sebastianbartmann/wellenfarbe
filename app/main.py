from fastapi import FastAPI, Request, Form, Depends, HTTPException, status
from fastapi.responses import HTMLResponse
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import subprocess
from contextlib import asynccontextmanager


@asynccontextmanager
async def lifespan(app: FastAPI):
    try:
        subprocess.run([
            "tailwindcss",
            "-i",
            "./static/tailwind.css",
            "-o",
            "./static/css/main.css",
            "--minify"
        ])
    except Exception as e:
        print(f"Error running tailwindcss: {e}")

    yield


app = FastAPI(lifespan=lifespan)

templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

security = HTTPBasic()
authorized_users = {"usr": "ptra"}


def authenticate(credentials: HTTPBasicCredentials = Depends(security)):
    if credentials.username in authorized_users and authorized_users[credentials.username] == credentials.password:
        return credentials.username
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid credentials",
        headers={"WWW-Authenticate": "Basic"},
    )


@app.get("/")
async def read_root(request: Request, user: str = Depends(authenticate)):
    return templates.TemplateResponse("index.html", {"request": request, "header_class": "transparent-header", "text_color_class": "text-white"})


@app.get("/about")
async def read_root(request: Request, user: str = Depends(authenticate)):
    return templates.TemplateResponse("about.html", {"request": request, "header_class": ""})


@app.get("/contact")
async def read_root(request: Request, user: str = Depends(authenticate)):
    return templates.TemplateResponse("contact.html", {"request": request, "header_class": "transparent-header", "text_color_class": "text-white"})


@app.get("/method")
async def read_root(request: Request, user: str = Depends(authenticate)):
    return templates.TemplateResponse("method.html", {"request": request, "header_class": ""})


# Serve robots.txt and sitemap.xml directly
@app.get("/robots.txt")
async def robots_txt():
    return StaticFiles(directory="static").lookup_path("/robots.txt")


@app.get("/sitemap.xml")
async def sitemap_xml():
    return StaticFiles(directory="static").lookup_path("/sitemap.xml")

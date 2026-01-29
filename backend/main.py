from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup: Connect to DB (placeholder)
    print("Starting up UNIManager API...")
    yield
    # Shutdown: Disconnect DB
    print("Shutting down UNIManager API...")

from routers import users, academic, operations

app = FastAPI(
    title="UNIManager API",
    description="University Management System API",
    version="3.0.0",
    lifespan=lifespan,
    docs_url="/docs",
    redoc_url="/redoc",
)

app.include_router(users.router)
app.include_router(academic.router)
app.include_router(operations.router)

# CORS Configuration
# CORS Configuration
# ALLOWING ALL ORIGINS FOR DEBUGGING
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
async def health_check():
    return {"status": "ok", "service": "unimanager-api"}

@app.get("/")
async def root():
    return {"message": "Welcome to UNIManager API v3"}

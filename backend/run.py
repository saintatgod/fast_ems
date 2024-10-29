import uvicorn

def run()->None:
    uvicorn.run(
        app="app:create_app",
        host="0.0.0.0",
        port=8000,
        lifespan="on",
        reload=True,
        factory=True)

if __name__ == "__main__":
    run()
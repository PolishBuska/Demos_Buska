from fastapi import FastAPI


app = FastAPI(
    title="Demos_Buska",
    description="This service provides with my own tracks"
)


@app.get('/')
def root():
    return "Hello world"




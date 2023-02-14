from fastapi import FastAPI
import os

app = FastAPI()

crt_data = "/home/andreo/Inuits/certiman/certs/example.localhost.crt"
pk = "/home/andreo/Inuits/certiman/certs/example.localhost.key"


@app.get("/")
def home():
    return "Welcome to the certificate API. Go to /certificate to get the certificate details"



@app.get("/certificate")
async def get_cert():
    with open(crt_data, "rb") as f, open(pk, "rb") as f2:
        crt_bytes = f.read()
        pk_bytes = f2.read()
    return {"crt_data": crt_bytes, "private_key": pk_bytes}


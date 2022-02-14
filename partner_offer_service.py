import uvicorn
from fastapi import FastAPI, Response
import time

app = FastAPI()


@app.get("/offer/hot")
async def get_offer():
    time.sleep(1)
    body = "Hot offer {}:{}".format(time.localtime().tm_min,
                                    time.localtime().tm_sec)
    return Response(content=body, status_code=200)


if __name__ == '__main__':
    uvicorn.run('partner_offer_service:app', port=8000, reload=True)

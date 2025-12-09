from fastapi import APIRouter, File, UploadFile, Form, HTTPException
from fastapi.responses import JSONResponse
from models.params import EdgeParams
from services.edge_processor import EdgeProcessor
import base64

router = APIRouter(prefix="/edges", tags=["Image Transforms"])
processor = EdgeProcessor()

@router.post("/process")
async def process_edges(
    image: UploadFile = File(...),
    blur_ksize: int = Form(5),
    blur_sigma: float = Form(0.0),
    sobel_ksize: int = Form(3),
    canny_low: int = Form(50),
    canny_high: int = Form(150),
    thickness: int = Form(1),
):
    params = EdgeParams(
        blur_ksize=blur_ksize,
        blur_sigma=blur_sigma,
        sobel_ksize=sobel_ksize,
        canny_low=canny_low,
        canny_high=canny_high,
        thickness=thickness,
    )

    contents = await image.read()

    try:
        outputs = processor.process_image(contents, params)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

    def to_b64(img_bytes):
        return base64.b64encode(img_bytes).decode("utf-8")

    return JSONResponse({
        "sobel": to_b64(outputs["sobel"]),
        "laplacian": to_b64(outputs["laplacian"]),
        "canny": to_b64(outputs["canny"]),
        "scharr": to_b64(outputs["scharr"]),
        "histogram": to_b64(outputs["histogram"]),
        "hog": to_b64(outputs["hog"])
    })

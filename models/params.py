from pydantic import BaseModel

class EdgeParams(BaseModel):
    blur_ksize: int = 5
    blur_sigma: float = 0.0
    sobel_ksize: int = 3
    canny_low: int = 50
    canny_high: int = 150
    thickness: int = 1

import cv2
import numpy as np
from skimage.feature import hog
from utils.img_utils import ensure_odd
from models.params import EdgeParams

class EdgeProcessor:

    def process_image(self, image_bytes: bytes, params: EdgeParams):
        nparr = np.frombuffer(image_bytes, np.uint8)
        frame = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

        if frame is None:
            raise ValueError("Invalid or corrupted image file")

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Gaussian Blur
        k = ensure_odd(params.blur_ksize)
        blurred = cv2.GaussianBlur(gray, (k, k), params.blur_sigma) if k > 1 else gray.copy()

        # Sobel
        sx = cv2.Sobel(blurred, cv2.CV_64F, 1, 0, ksize=params.sobel_ksize)
        sy = cv2.Sobel(blurred, cv2.CV_64F, 0, 1, ksize=params.sobel_ksize)
        sobel_mag = cv2.magnitude(sx, sy)
        sobel_mag = np.uint8((sobel_mag / (sobel_mag.max() + 1e-9)) * 255)

        # Laplacian
        lap = cv2.Laplacian(blurred, cv2.CV_64F)
        lap = np.uint8((np.abs(lap) / (lap.max() + 1e-9)) * 255)

        # Canny
        low, high = min(params.canny_low, params.canny_high), max(params.canny_low, params.canny_high)
        canny = cv2.Canny(blurred, low, high)

        # Scharr
        scharr_x = cv2.Scharr(blurred, cv2.CV_64F, 1, 0)
        scharr_y = cv2.Scharr(blurred, cv2.CV_64F, 0, 1)
        scharr_mag = cv2.magnitude(scharr_x, scharr_y)
        scharr_mag = np.uint8((scharr_mag / (scharr_mag.max() + 1e-9)) * 255)

        # Histogram visualization
        hist = cv2.calcHist([gray], [0], None, [256], [0,256])
        hist_img = np.zeros((300, 256), dtype=np.uint8)
        cv2.normalize(hist, hist, 0, 300, cv2.NORM_MINMAX)
        for x, y in enumerate(hist):
            cv2.line(hist_img, (x, 300), (x, 300 - int(y)), 255)
        hist_img = cv2.cvtColor(hist_img, cv2.COLOR_GRAY2BGR)

        # HOG visualization
        hog_feat, hog_img = hog(gray, pixels_per_cell=(16,16), cells_per_block=(1,1),
                                 visualize=True, feature_vector=False)
        hog_img = np.uint8(hog_img * 255)

        # Thickness dilation
        if params.thickness > 1:
            kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))
            iterations = params.thickness - 1
            sobel_mag = cv2.dilate(sobel_mag, kernel, iterations=iterations)
            lap = cv2.dilate(lap, kernel, iterations=iterations)
            canny = cv2.dilate(canny, kernel, iterations=iterations)
            scharr_mag = cv2.dilate(scharr_mag, kernel, iterations=iterations)

        # Encode all images to bytes
        def encode(img):
            _, buf = cv2.imencode(".png", img)
            return buf.tobytes()

        return {
            "sobel": encode(sobel_mag),
            "laplacian": encode(lap),
            "canny": encode(canny),
            "scharr": encode(scharr_mag),
            "histogram": encode(hist_img),
            "hog": encode(hog_img)
        }

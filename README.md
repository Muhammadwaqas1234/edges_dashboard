# Edge Detection Dashboard

A **real-time edge detection dashboard** built with **FastAPI** and **OpenCV**, allowing users to upload images and visualize multiple edge detection and image processing techniques, including:

* Sobel Edge Detection
* Laplacian Edge Detection
* Canny Edge Detection
* Scharr Operator
* Histogram Visualization
* HOG (Histogram of Oriented Gradients)

The frontend is fully **dynamic, responsive, and interactive**, allowing parameter adjustment via sliders.

---

## Features

* Upload any image and apply multiple edge detection filters.
* Adjust processing parameters in real-time:

  * Gaussian Blur Kernel & Sigma
  * Sobel Kernel
  * Canny Thresholds
  * Edge Thickness
* View results for all transformations in a clean dashboard.
* Responsive design, works on desktop and tablet screens.

---


## Tech Stack

* **Backend:** FastAPI, Python, OpenCV, NumPy
* **Frontend:** HTML, CSS, JavaScript
* **Deployment:** Localhost or any FastAPI compatible hosting

---

## Installation

1. **Clone the repository:**

```bash
git clone https://github.com/yourusername/edge-detection-dashboard.git
cd edge-detection-dashboard
```

2. **Create a virtual environment and activate it:**

```bash
python -m venv env
# Windows
env\Scripts\activate
# macOS/Linux
source env/bin/activate
```

3. **Install dependencies:**

```bash
pip install -r requirements.txt
```

> Make sure you have **OpenCV** and **scikit-image** installed if using HOG:

```bash
pip install opencv-python scikit-image numpy fastapi uvicorn
```

4. **Run the FastAPI server:**

```bash
uvicorn main:app --reload
```

The backend API will be available at:
`http://127.0.0.1:8000/`

---

## Usage

1. Open your browser and navigate to:
   `http://127.0.0.1:8000/frontend/index.html`

2. Upload an image using the **file input**.

3. Adjust parameters using sliders:

* Gaussian blur kernel & sigma
* Sobel kernel size
* Canny thresholds
* Edge thickness

4. Click **Process Image**.

5. View results for **Sobel, Laplacian, Canny, Scharr, Histogram, and HOG** in the results grid.

---

## Project Structure

```
edge_api/
│── main.py                  # FastAPI entrypoint
│── routers/
│     └── edges.py           # API routes
│── services/
│     └── edge_processor.py  # Image processing logic
│── models/
│     └── params.py          # Pydantic model for parameters
│── utils/
│     └── img_utils.py       # Utility functions
│── frontend/
│     ├── index.html         # Frontend HTML
│     ├── style.css          # Styling
│     └── script.js          # Frontend logic
│── requirements.txt         # Python dependencies
│── README.md                # Project documentation
```

---

## Future Improvements

* Add **real-time webcam input**.
* Add **additional edge detection algorithms** like Prewitt, Roberts, and Laplacian of Gaussian (LoG).
* Add **download option** for processed images.
* Add **batch processing** for multiple images.


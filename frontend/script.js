document.getElementById("imageInput").addEventListener("change", function() {
    const file = this.files[0];
    if (file) {
        const reader = new FileReader();
        reader.onload = function(e) {
            document.getElementById("previewImg").src = e.target.result;
        }
        reader.readAsDataURL(file);
    }
});

async function processImage() {
    const file = document.getElementById("imageInput").files[0];
    if (!file) {
        alert("Please select an image");
        return;
    }

    const loading = document.getElementById("loading");
    loading.style.display = "flex";

    const form = new FormData();
    form.append("image", file);
    form.append("blur_ksize", document.getElementById("blur_ksize").value);
    form.append("blur_sigma", document.getElementById("blur_sigma").value);
    form.append("sobel_ksize", document.getElementById("sobel_ksize").value);
    form.append("canny_low", document.getElementById("canny_low").value);
    form.append("canny_high", document.getElementById("canny_high").value);
    form.append("thickness", document.getElementById("thickness").value);

    try {
        const res = await fetch("http://127.0.0.1:8000/edges/process", {
            method: "POST",
            body: form
        });

        if (!res.ok) throw new Error("Processing failed!");

        const data = await res.json();

        // Update all images
        document.getElementById("sobelImg").src = "data:image/png;base64," + data.sobel;
        document.getElementById("lapImg").src = "data:image/png;base64," + data.laplacian;
        document.getElementById("cannyImg").src = "data:image/png;base64," + data.canny;
        document.getElementById("scharrImg").src = "data:image/png;base64," + data.scharr;
        document.getElementById("histogramImg").src = "data:image/png;base64," + data.histogram;
        document.getElementById("hogImg").src = "data:image/png;base64," + data.hog;

    } catch (err) {
        alert(err.message);
    } finally {
        loading.style.display = "none";
    }
}

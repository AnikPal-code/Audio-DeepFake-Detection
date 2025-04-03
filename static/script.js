document.addEventListener("DOMContentLoaded", function () {
    const form = document.getElementById("upload-form");
    const resultDiv = document.getElementById("result");

    form.addEventListener("submit", function (event) {
        event.preventDefault(); // Prevent page reload

        const formData = new FormData();
        const fileInput = document.getElementById("audio-file");
        
        if (fileInput.files.length === 0) {
            resultDiv.innerHTML = "<p style='color:red;'>Please select an audio file.</p>";
            return;
        }

        formData.append("file", fileInput.files[0]);

        // Disable button to prevent multiple clicks
        const submitButton = form.querySelector("button");
        submitButton.disabled = true;
        submitButton.innerText = "Processing...";

        fetch("/predict", {
            method: "POST",
            body: formData,
            cache: "no-cache" // Prevents caching
        })
        .then(response => response.json())
        .then(data => {
            resultDiv.innerHTML = `<p><strong>Result:</strong> ${data.result}</p>`;
        })
        .catch(error => {
            console.error("Error:", error);
            resultDiv.innerHTML = "<p style='color:red;'>Error processing the file.</p>";
        })
        .finally(() => {
            submitButton.disabled = false;
            submitButton.innerText = "Check Audio";
        });
    });
});

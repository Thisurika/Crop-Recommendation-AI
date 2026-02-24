

document.getElementById('crop-form').addEventListener('submit', async function(e) {
    e.preventDefault();  // This must stay first

    const form = e.target;
    const resultDiv = document.getElementById('result');

    // Show loading state
    resultDiv.innerHTML = "Predicting...";
    resultDiv.style.color = "#555";

    try {
        // Use URLSearchParams — more reliable than FormData for this case
        const formData = new URLSearchParams();
        for (const [key, value] of new FormData(form)) {
            formData.append(key, value);
        }

        const response = await fetch('/predict', {
            method: 'POST',
            body: formData,
            headers: {
                'Accept': 'application/json'
            }
        });

        if (!response.ok) {
            throw new Error(`Server error: ${response.status}`);
        }

        const data = await response.json();

        // Show result
        resultDiv.innerHTML = `Recommended Crop: <strong>${data.crop}</strong>`;
        resultDiv.style.color = "#4CAF50";

        // Optional: clear form after success (uncomment if you want)
        // form.reset();

    } catch (error) {
        console.error('Prediction failed:', error);
        resultDiv.innerHTML = "Error predicting crop. Check console & try again.";
        resultDiv.style.color = "#d32f2f";
    }
});

// Reset button functionality
document.getElementById('reset-btn').addEventListener('click', function() {
    const form = document.getElementById('crop-form');
    form.reset();                      // Built-in method – clears all inputs
    document.getElementById('result').innerHTML = '';  // Also clear the result text
});


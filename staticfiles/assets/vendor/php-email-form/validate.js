document.addEventListener("DOMContentLoaded", function () {
  let form = document.querySelector(".php-email-form");

  if (form) {
    // Remove existing event listeners before adding a new one
    form.removeEventListener("submit", handleSubmit);
    form.addEventListener("submit", handleSubmit);
  }
});

function handleSubmit(event) {
  event.preventDefault(); // Stop the form from submitting normally

  let form = event.target;
  let formData = new FormData(form);
  let action = form.getAttribute("action");

  // Get success, error, and loading messages
  let loadingDiv = form.querySelector(".loading");
  let errorDiv = form.querySelector(".error-message");
  let successDiv = form.querySelector(".sent-message");

  // Hide previous messages before showing new ones
  loadingDiv.style.display = "none";
  errorDiv.style.display = "none";
  successDiv.style.display = "none";

  // Show loading state
  loadingDiv.style.display = "block";

  fetch(action, {
    method: "POST",
    body: formData,
    headers: {
      "X-Requested-With": "XMLHttpRequest",
    },
  })
    .then(response => response.text())
    .then(data => {
      loadingDiv.style.display = "none"; // Hide loading

      if (data.trim().toLowerCase() === "ok") {
        successDiv.style.display = "block"; // Show success message
        form.reset(); // Clear form fields
      } else {
        errorDiv.style.display = "block";
        errorDiv.innerHTML = data;
      }
    })
    .catch(error => {
      loadingDiv.style.display = "none";
      errorDiv.style.display = "block";
      errorDiv.innerHTML = "An error occurred. Please try again.";
    });
}

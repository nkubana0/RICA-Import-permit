function submitFormData(formData) {
  fetch("/submit-form", {
    method: 'POST',
    body: formData,  // Send form data directly without JSON.stringify
  })
    .then((response) => {
      if (response.ok) {
        alert("Form submitted successfully!");
        sendEmail(formData); // Send email after successful form submission
      } else {
        throw new Error("Failed to submit form");
      }
    })
    .catch((error) => {
      alert("Failed to submit form. Please try again.");
    });
}

function sendEmail(formData) {
  fetch("/send-email", {
    method: 'POST',
    body: formData,  // Send form data directly without JSON.stringify
  })
    .then((response) => {
      if (!response.ok) {
        throw new Error("Failed to send email");
      }
    })
    .catch((error) => {
      console.error("Failed to send email:", error);
    });
}

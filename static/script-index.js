document.addEventListener("DOMContentLoaded", () => {
  document.querySelector(".form").addEventListener("submit", async (event) => {
    event.preventDefault();

    const fname = document.getElementById("first-name-input").value;
    const lname = document.getElementById("last-name-input").value;
    const email = document.getElementById("form-email").value;
    const messageDiv = document.getElementById("error-message");
    const data = { fname, lname, email };

    try {
      const response = await fetch("/submit-form", {
        method: "POST",
        body: JSON.stringify(data),
        headers: {
          "Content-Type": "application/json",
        },
      });

      const responseData = await response.json();
      if (response.ok) {
        const email_id = responseData.email;
        window.location.href = `/user/${email_id}`;
      } else {
        const email_id = responseData.email;
        messageDiv.style.display = "block";
        messageDiv.style.color = "#2e1c97";
        messageDiv.innerHTML = `An API key already exists for the user ${email_id}`;
      }
    } catch (error) {
      console.error("An error occurred:", error);
    }
  });
});

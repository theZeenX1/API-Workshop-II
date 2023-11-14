document.addEventListener("DOMContentLoaded", function () {
  const logo = document.querySelector(".logo");

  if (logo) {
    logo.addEventListener("click", function () {
      window.location.href = "/";
    });
  }
});

const copyButton = document.getElementById("btn");
const _idText = document.getElementById("_id");
const originalButtonText = copyButton.textContent;

copyButton.addEventListener("click", function () {
  const textarea = document.createElement("textarea");
  textarea.value = _idText.textContent;

  document.body.appendChild(textarea);
  textarea.select();
  document.execCommand("copy");

  document.body.removeChild(textarea);

  copyButton.textContent = "Copied!";
  copyButton.style.transition = "all 1.5s";
  setTimeout(function () {
    copyButton.textContent = originalButtonText;
  }, 1500);
});

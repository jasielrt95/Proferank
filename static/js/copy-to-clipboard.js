function tempAlert(msg, duration, button) {
  var alert = document.createElement("div");
  alert.className = "alert";
  alert.textContent = msg;
  alert.style.background = "white";
  alert.style.borderRadius = "5px";
  alert.style.color = "#5046e5";
  alert.style.padding = "10px";
  button.parentNode.insertBefore(alert, button);

  setTimeout(function () {
    alert.parentNode.removeChild(alert);
  }, duration);
}
function copyToClipboard(button) {
  const url = button.getAttribute("confesion-id");
  if (!url) {
    console.error("No confesion-id attribute found on the button");
    return;
  }
  navigator.clipboard
    .writeText(url)
    .then(() => {
      tempAlert("Copiado, compartelo!", 2000, button);
    })
    .catch((error) => {
      console.error("Error copying text: ", error);
    });
}

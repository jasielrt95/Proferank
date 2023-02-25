function tempAlert(msg, duration, button) {
  var alert = document.createElement("div");
  alert.className = "alert";
  alert.textContent = msg;

  /* Add the alert element just before the button */
    button.parentNode.insertBefore(alert, button);

    /* Remove the alert element after the specified duration */
    setTimeout(function () {
        alert.parentNode.removeChild(alert);
        }
    , duration);
}
function copyToClipboard(button) {
  /* Get the confesion-id property value of the button that was clicked */
  const url = button.getAttribute("confesion-id");
  if (!url) {
    console.error("No confesion-id attribute found on the button");
    return;
  }

  /* Write the text to the clipboard */
  navigator.clipboard
    .writeText(url)
    .then(() => {
      tempAlert("Copiado, compartelo!", 2000, button);
    })
    .catch((error) => {
      console.error("Error copying text: ", error);
    });
}

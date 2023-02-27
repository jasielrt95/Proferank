let likeButtons = document.getElementsByClassName("like-button");
let dislikeButtons = document.getElementsByClassName("dislike-button");

// add event listener to each button
for (let i = 0; i < likeButtons.length; i++) {
  likeButtons[i].addEventListener("click", likeRequest);
  dislikeButtons[i].addEventListener("click", dislikeRequest);
}

function likeRequest() {
  console.log("like button clicked");
  let likeButton = this;
  let confession_id = likeButton.getAttribute("data-confession-id");
  console.log(confession_id);
  if (confession_id) {
    sendLikeRequest(likeButton, confession_id);
  }
}

function dislikeRequest() {
  console.log("dislike button clicked");
  let dislikeButton = this;
  let confession_id = dislikeButton.getAttribute("data-confession-id");
  console.log(confession_id);
  if (confession_id) {
    sendDislikeRequest(dislikeButton, confession_id);
  }
}

function sendLikeRequest(likeButton, confession_id) {
  let request = new XMLHttpRequest();
  request.open("POST", "/confessions/" + confession_id + "/like");
  request.setRequestHeader("X-CSRFToken", csrftoken);
  request.setRequestHeader("Content-Type", "application/json");
  request.onload = function () {
    let data = JSON.parse(request.responseText);
    console.log(data);
    if (data) {
      updateScore(likeButton, data.score, "like");
    }
  };
  request.send();
}

function sendDislikeRequest(dislikeButton, confession_id) {
  let request = new XMLHttpRequest();
  request.open("POST", "/confessions/" + confession_id + "/dislike");
  request.setRequestHeader("X-CSRFToken", csrftoken);
  request.setRequestHeader("Content-Type", "application/json");
  request.onload = function () {
    let data = JSON.parse(request.responseText);
    console.log(data);
    if (data) {
      updateScore(dislikeButton, data.score, "dislike");
    }
  };
  request.send();
}

function updateScore(Button, score, Type) {
  if (Type == "like") {
    let scoreParagraph = Button.previousElementSibling;
    scoreParagraph.innerHTML = score;
  } else {
    let scoreParagraph = Button.previousElementSibling.previousElementSibling;
    scoreParagraph.innerHTML = score;
  }
}

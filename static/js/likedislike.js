
let likeButtons = document.getElementsByClassName('like-button');
let dislikeButtons = document.getElementsByClassName('dislike-button');

// add event listener to each button
for (let i = 0; i < likeButtons.length; i++) {
    likeButtons[i].addEventListener('click', likeRequest);
    dislikeButtons[i].addEventListener('click', dislikeRequest);
}

function likeRequest() {
    console.log('like button clicked');
    let likeButton = this;
    let comment_id = likeButton.getAttribute('data-comment-id');
    console.log(comment_id);
    if (comment_id) {
        sendLikeRequest(likeButton, comment_id)
    }
}

function dislikeRequest() {
    console.log('dislike button clicked');
    let dislikeButton = this;
    let comment_id = dislikeButton.getAttribute('data-comment-id');
    console.log(comment_id);
    if (comment_id) {
        sendDislikeRequest(dislikeButton, comment_id)
    }
}

function sendLikeRequest(likeButton, comment_id) {
    let request = new XMLHttpRequest();
    request.open('POST', '/comments/' + comment_id +'/like');
    request.setRequestHeader('X-CSRFToken', csrftoken);
    request.setRequestHeader('Content-Type', 'application/json');
    request.onload = function () {
        let data = JSON.parse(request.responseText);
        console.log(data);
        if (data) {
            updateScore(likeButton, data.score, "like");
        };
    }
    request.send();
}

function sendDislikeRequest(dislikeButton, comment_id) {
    let request = new XMLHttpRequest();
    request.open('POST', '/comments/' + comment_id +'/dislike');
    request.setRequestHeader('X-CSRFToken', csrftoken);
    request.setRequestHeader('Content-Type', 'application/json');
    request.onload = function () {
        let data = JSON.parse(request.responseText);
        console.log(data);
        if (data) {
            updateScore(dislikeButton, data.score, "dislike");
        };
    }
    request.send();
}

function updateScore(Button, score, Type) {

    if (Type == "like") {
        let scoreParagraph = Button.previousElementSibling;
        scoreParagraph.innerHTML = score;
    };
    if (Type == "dislike") {
        let scoreParagraph = Button.previousElementSibling.previousElementSibling;
        scoreParagraph.innerHTML = score;
    };
}

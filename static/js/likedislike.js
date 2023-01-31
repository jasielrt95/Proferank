// get all the like buttons
let likeButtons = document.getElementsByClassName('like-button');
console.log(likeButtons);

// add event listener to each button
for (let i = 0; i < likeButtons.length; i++) {
    likeButtons[i].addEventListener('click', likeRequest);
}

function likeRequest() {
    console.log('like button clicked');
    let likeButton = this;
    let comment_id = likeButton.getAttribute('data-comment-id');
    if (comment_id) {
        sendLikeRequest(likeButton, comment_id)
    }
}

function sendLikeRequest(likeButton, comment_id) {
    let request = new XMLHttpRequest();
    request.open('POST', '/comments/' + comment_id +'/like');
    request.setRequestHeader('X-CSRFToken', csrftoken);
    request.setRequestHeader('Content-Type', 'application/json');
    request.onload = function () {
        updateLikeCount(request, likeButton);
    }
    request.send();
}

function updateLikeCount(request, likeButton) {
    let data = JSON.parse(request.responseText);
    let likecount = data['likecount'];
    likeButton.parentElement.querySelector('.like-count').innerHTML = likecount;
}
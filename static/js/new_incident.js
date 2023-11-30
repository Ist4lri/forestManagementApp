
document.addEventListener('DOMContentLoaded', function() {
    blinkImage();
});

function blinkImage() {
    var image = document.querySelector('#incidents img');

    if (image) {
        var isVisible = true;

        setInterval(function() {
            isVisible = !isVisible;
            image.style.visibility = isVisible ? 'visible' : 'hidden';
        }, 300);
    }
}

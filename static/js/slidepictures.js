let slideIndex = 0;
showSlides();

function showSlides() {
    let slides = document.getElementsByClassName("mySlides");

    // Hide all slides
    for (let i = 0; i < slides.length; i++) {
        slides[i].style.display = "none";
    }

    // Display the current slide
    slides[slideIndex].style.display = "block";
}

// Set up click event listeners for arrows
document.querySelector(".prev").addEventListener("click", function() {
    let slides = document.getElementsByClassName("mySlides");
    slideIndex--;
    if (slideIndex < 0) {
        slideIndex = slides.length - 1;
    }
    showSlides();
});

document.querySelector(".next").addEventListener("click", function() {
    let slides = document.getElementsByClassName("mySlides");
    slideIndex++;
    if (slideIndex >= slides.length) {
        slideIndex = 0;
    }
    showSlides();
});

let dot = document.querySelector('.cursor-dot');
let circle = document.querySelector('.cursor-circle');

// actual cursor coordinates
let mouseX = 0;
let mouseY = 0;

// current coordinates of the smooth circle
let circleX = 0;
let circleY = 0;

let cursorInitialized = false;



const speed = 0.1;

document.addEventListener('mousemove', (event) => {
  mouseX = event.clientX;
  mouseY = event.clientY;

  // small dot always follows the cursor precisely, without any lag.
  dot.style.left = `${mouseX}px`;
  dot.style.top = `${mouseY}px`;

  if (!cursorInitialized) {
    // upon the first movement, immediately place a circle at the cursor's position.
    circleX = mouseX;
    circleY = mouseY;

    dot.classList.add('active');
    circle.classList.add('active');

    cursorInitialized = true;

    // starting a smooth motion cycle.
    animate();
  }

});

function animate() {
  // calculating a smooth approximation (linear interpolation)
  circleX += (mouseX - circleX) * speed;
  circleY += (mouseY - circleY) * speed;

  circle.style.left = `${circleX}px`;
  circle.style.top = `${circleY}px`;

  // requesting the next frame.
  requestAnimationFrame(animate);
}
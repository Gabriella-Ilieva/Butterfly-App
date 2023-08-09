function openFilterMenu() {
  document.getElementById("filterMenu").style.display = "block";
  document.getElementById("myOverlay").style.display = "block";
}

function closeFilterMenu() {
  document.getElementById("filterMenu").style.display = "none";
  document.getElementById("myOverlay").style.display = "none";
}

function openRightMenu() {
  document.getElementById("rightMenu").style.display = "block";
  document.getElementById("myOverlay").style.display = "block";
}

function closeRightMenu() {
  document.getElementById("rightMenu").style.display = "none";
  document.getElementById("myOverlay").style.display = "none";
}

var slideIndexBase = 0;
carousel();

function carousel() {
  var i;
  var x = document.getElementsByClassName("quoteSlides");
  for (i = 0; i < x.length; i++) {
    x[i].style.display = "none";
  }
  slideIndexBase++;
  if (slideIndexBase > x.length) {slideIndexBase = 1}
  x[slideIndexBase-1].style.display = "block";
  setTimeout(carousel, 15000);
}

var slideIndex = 1;
showDivs(slideIndex);

function plusDivs(n) {
  showDivs(slideIndex += n);
}

function currentDiv(n) {
  showDivs(slideIndex = n);
}

function showDivs(n) {
  var i;
  var x = document.getElementsByClassName("mySlides");
  var dots = document.getElementsByClassName("demo");
  if (n > x.length) {slideIndex = 1}
  if (n < 1) {slideIndex = x.length}
  for (i = 0; i < x.length; i++) {
    x[i].style.display = "none";
  }
  for (i = 0; i < dots.length; i++) {
    dots[i].className = dots[i].className.replace(" w3-white", "");
  }
  x[slideIndex-1].style.display = "block";
  dots[slideIndex-1].className += " w3-white";
}
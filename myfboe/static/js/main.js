const toggleBtnEl = document.querySelector(".navbar__toogleBtn");
const menuEl = document.querySelector('.navbar__menu');
const navbarEl = document.querySelector('.navbar');

toggleBtnEl.addEventListener('click', () => {
  menuEl.classList.toggle('active')
})


//<!-- Initialize Swiper -->
var swiper = new Swiper(".mySwiper", {
  effect: "coverflow",
  grabCursor: true,
  centeredSlides: true,
  slidesPerView: "auto",
  coverflowEffect: {
  rotate: 50,
  stretch: 0,
  depth: 100,
  modifier: 1,
  slideShadows: true,
  },
  loop: true,
  autoplay: true,
  pagination: {
  el: ".swiper-pagination",
  },
});
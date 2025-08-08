// sticky navbar
document.addEventListener('DOMContentLoaded', () => {
  const navSticky = document.querySelector('.nav_bar');

  window.addEventListener('scroll', function () {
    navSticky.classList.toggle('sticky', window.scrollY > 0);
  });
})

// navmenu 
// document.addEventListener('DOMContentLoaded', () => {
//   const menuItems = document.querySelectorAll('.items_list');

//   menuItems.forEach(menuItem => {
//     menuItem.addEventListener('click', () => {
//       const currentlyActive = document.querySelector('.active');
//       if (currentlyActive) {
//         currentlyActive.classList.remove('active');
//       }
//       menuItem.classList.add('active');
//     });
//   });
// });


// header-slider images
document.addEventListener('DOMContentLoaded', () => {
  const sliderItems = document.querySelectorAll('.mySwiper .swiper-slide')

  sliderItems.forEach(sliderItem => {
    sliderItem.addEventListener('click', () => {
      document.querySelector('.active_slider')?.classList.remove('active_slider')
      sliderItem.classList.add('active_slider')
    })
  })
})

// slider
var swiper = new Swiper(".mySwiper", {
  loop: true,
  slidesPerView: 3,
  freeMode: true,
  watchSlidesProgress: true,
});
var swiper2 = new Swiper(".mySwiper2", {
  loop: true,
  spaceBetween: 10,
  autoplay: {
    delay: 3000,
  },
  effect: "creative",
  creativeEffect: {
    prev: {
      shadow: true,
      translate: [0, 0, -400],
    },
    next: {
      translate: ["100%", 0, 0],
    },
  },
  navigation: {
    nextEl: ".arrow-next",
    prevEl: ".arrow-prev",
  },
  thumbs: {
    swiper: swiper,
  },
});

// tesimonials swiper
var swiper = new Swiper(".testimonial_swiper1", {
  loop: true,
  spaceBetween: 20,
  slidesPerView: 3,
  freeMode: true,
  watchSlidesProgress: true,
});
var swiper2 = new Swiper(".testimonial_swiper2", {
  loop: true,
  spaceBetween: 5,
  autoplay: {
    delay: 3000,
  },
  // effect: "fade",

  navigation: {
    nextEl: ".arrow-testi-next",
    prevEl: ".arrow-testi-prev",
  },
  thumbs: {
    swiper: swiper,
  },
});

document.addEventListener('DOMContentLoaded', () => {
  const hamMenu = document.querySelector('.hamburger_menu_wrapper');
  const menuBar = document.querySelectorAll('.bar')
  const menuItems = document.querySelector('.menu_items')

  hamMenu.addEventListener('click', () => {
    menuItems.classList.toggle('show_menu')
    menuBar.forEach(bar => {
      bar.classList.toggle('change');
    })
  })
})

// gallery modal
document.addEventListener("DOMContentLoaded", function () {
  var buttons = document.querySelectorAll(".text");

  buttons.forEach(function (button) {
    button.addEventListener("click", function () {
      // Get the parent image-wrapper
      var imageWrapper = this.closest(".image-wrapper");

      // Get the image source from the clicked image
      var imageUrl = imageWrapper.querySelector(".image").src;

      // Create a modal element
      var modal = document.createElement("div");
      modal.classList.add("modal");

      // // Create a close button
      var closeButton = document.createElement("button");
      closeButton.classList.add("close-button");
      closeButton.innerHTML = "&times;"; // '×' for close symbol

      // Add click event listener to close the modal
      closeButton.addEventListener("click", function () {
        document.body.removeChild(modal);
      });

      //Create a cmodal-wrapper inside the modal
      var modal_wrapper = document.createElement("div");
      modal_wrapper.classList.add("modal_wrapper");

      // Create a content div inside the modal-wrapper
      var contentDiv = document.createElement("div");
      contentDiv.classList.add("content-div");

      var modalImage = document.createElement("img");
      modalImage.src = imageUrl;
      modalImage.alt = "Modal Image";

      // Append the close button and image to the modal
      modal_wrapper.appendChild(closeButton);
      contentDiv.appendChild(modalImage);

      // Append the content div to the modal
      modal.appendChild(modal_wrapper);
      modal_wrapper.appendChild(contentDiv);

      // Append the modal to the body
      document.body.appendChild(modal);
    });
  });
});


// gallery show image and video
document.addEventListener("DOMContentLoaded", function () {
  const clickImage = document.querySelector('.click_image')
  const clickVideo = document.querySelector('.click_video')
  const showImage = document.querySelector('.show_image')
  const showVideo = document.querySelector('.show_video')

  clickImage.addEventListener("click", function () {
    showVideo.classList.remove('hide')
    showImage.classList.add('hide')
    clickImage.classList.add('active_btn')
    clickVideo.classList.remove('active_btn')
  })
  clickVideo.addEventListener("click", function () {
    showVideo.classList.add('hide')
    showImage.classList.remove('hide')
    clickImage.classList.remove('active_btn')
    clickVideo.classList.add('active_btn')
  })
});

// close and open gallery videos
document.addEventListener("DOMContentLoaded", function () {
  const playVideo = document.querySelectorAll('.play')
  const ModalVideo = document.querySelector('.modals_video')
  const videoClose = document.querySelector('.video_close')


  playVideo.forEach(playVideos => {
    playVideos.addEventListener("click", () => {
      ModalVideo.classList.add('visible_video')
    })
  })
  videoClose.addEventListener("click", () => {
    ModalVideo.classList.remove('visible_video')
  })
});

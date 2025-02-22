(function() {
  "use strict";

  function toggleScrolled() {
    const selectBody = document.querySelector('body');
    const selectHeader = document.querySelector('#header');
    if (!selectHeader) return;
    if (!selectHeader.classList.contains('scroll-up-sticky') &&
        !selectHeader.classList.contains('sticky-top') &&
        !selectHeader.classList.contains('fixed-top')) {
      return;
    }
    window.scrollY > 100 ? selectBody.classList.add('scrolled') : selectBody.classList.remove('scrolled');
  }

  document.addEventListener('DOMContentLoaded', function() {
    var nameInput = document.getElementById('name1');
    var emailInput = document.getElementById('email1');
    var subjectInput = document.getElementById('subject');

    if (nameInput) nameInput.classList.add('form-control');
    if (emailInput) emailInput.classList.add('form-control');
    if (subjectInput) subjectInput.classList.add('form-control');

    const mobileNavToggleBtn = document.querySelector('.mobile-nav-toggle');
    if (mobileNavToggleBtn) {
      mobileNavToggleBtn.addEventListener('click', function() {
        document.querySelector('body').classList.toggle('mobile-nav-active');
        mobileNavToggleBtn.classList.toggle('bi-list');
        mobileNavToggleBtn.classList.toggle('bi-x');
      });
    }

    document.querySelectorAll('#navmenu a').forEach(navmenu => {
      navmenu.addEventListener('click', () => {
        if (document.querySelector('.mobile-nav-active') && mobileNavToggleBtn) {
          mobileNavToggleBtn.click();
        }
      });
    });

    document.querySelectorAll('.navmenu .toggle-dropdown').forEach(navmenu => {
      navmenu.addEventListener('click', function(e) {
        e.preventDefault();
        if (this.parentNode) {
          this.parentNode.classList.toggle('active');
          if (this.parentNode.nextElementSibling) {
            this.parentNode.nextElementSibling.classList.toggle('dropdown-active');
          }
        }
        e.stopImmediatePropagation();
      });
    });

    const preloader = document.querySelector('#preloader');
    if (preloader) {
      window.addEventListener('load', () => {
        preloader.remove();
      });
    }

    let scrollTop = document.querySelector('.scroll-top');
    if (scrollTop) {
      scrollTop.addEventListener('click', (e) => {
        e.preventDefault();
        window.scrollTo({ top: 0, behavior: 'smooth' });
      });

      function toggleScrollTop() {
        window.scrollY > 100 ? scrollTop.classList.add('active') : scrollTop.classList.remove('active');
      }
      window.addEventListener('load', toggleScrollTop);
      document.addEventListener('scroll', toggleScrollTop);
    }

    function aosInit() {
      if (typeof AOS !== "undefined") {
        AOS.init({ duration: 600, easing: 'ease-in-out', once: true, mirror: false });
      }
    }
    window.addEventListener('load', aosInit);

    /** Fix: Auto generate carousel indicators correctly **/
    document.querySelectorAll('.carousel-indicators').forEach((carouselIndicator) => {
      const carousel = carouselIndicator.closest('.carousel');
      if (!carousel) return;

      const carouselItems = carousel.querySelectorAll('.carousel-item');
      carouselIndicator.innerHTML = ''; // Clear previous indicators

      carouselItems.forEach((_, index) => {
        let indicator = document.createElement('li');
        indicator.setAttribute('data-bs-target', `#${carousel.id}`);
        indicator.setAttribute('data-bs-slide-to', index);
        if (index === 0) indicator.classList.add('active');
        carouselIndicator.appendChild(indicator);
      });
    });

    if (typeof GLightbox !== "undefined") {
      GLightbox({ selector: '.glightbox' });
    }

    function initSwiper() {
      document.querySelectorAll(".init-swiper").forEach(function(swiperElement) {
        const configElement = swiperElement.querySelector(".swiper-config");
        if (configElement) {
          let config = JSON.parse(configElement.innerHTML.trim());
          new Swiper(swiperElement, config);
        }
      });
    }
    window.addEventListener("load", initSwiper);

    window.addEventListener('load', function() {
      if (window.location.hash) {
        const section = document.querySelector(window.location.hash);
        if (section) {
          setTimeout(() => {
            let scrollMarginTop = getComputedStyle(section).scrollMarginTop;
            window.scrollTo({ top: section.offsetTop - parseInt(scrollMarginTop), behavior: 'smooth' });
          }, 100);
        }
      }
    });

    let navmenulinks = document.querySelectorAll('.navmenu a');
    function navmenuScrollspy() {
      navmenulinks.forEach(navmenulink => {
        if (!navmenulink.hash) return;
        let section = document.querySelector(navmenulink.hash);
        if (!section) return;
        let position = window.scrollY + 200;
        if (position >= section.offsetTop && position <= (section.offsetTop + section.offsetHeight)) {
          document.querySelectorAll('.navmenu a.active').forEach(link => link.classList.remove('active'));
          navmenulink.classList.add('active');
        } else {
          navmenulink.classList.remove('active');
        }
      });
    }
    window.addEventListener('load', navmenuScrollspy);
    document.addEventListener('scroll', navmenuScrollspy);
  });
})();

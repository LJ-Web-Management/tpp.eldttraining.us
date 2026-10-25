document.documentElement.classList.add("js-reveal");

document.addEventListener("DOMContentLoaded", function () {
  var toggle = document.getElementById("navToggle");
  var nav = document.getElementById("mainNav");

  if (toggle && nav) {
    toggle.addEventListener("click", function () {
      var isOpen = nav.classList.toggle("open");
      toggle.classList.toggle("open", isOpen);
      toggle.setAttribute("aria-expanded", isOpen ? "true" : "false");
    });
  }

  // On the mobile menu, tapping a dropdown parent expands it instead of navigating
  document.querySelectorAll(".has-dropdown > a").forEach(function (link) {
    link.addEventListener("click", function (e) {
      if (window.matchMedia("(max-width: 1040px)").matches) {
        e.preventDefault();
        link.parentElement.classList.toggle("open");
      }
    });
  });

  var header = document.querySelector(".site-header");
  if (header) {
    var setScrolled = function () {
      header.classList.toggle("scrolled", window.scrollY > 8);
    };
    setScrolled();
    addEventListener("scroll", setScrolled, { passive: true });
  }

  // Fade cards in as they scroll into view
  var revealTargets = document.querySelectorAll(".cat-card, .guide-card, .plan-card, .step, .benefit-item, .card, .cta-banner");
  if ("IntersectionObserver" in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add("is-visible");
          io.unobserve(entry.target);
        }
      });
    }, { rootMargin: "0px 0px -40px 0px" });
    revealTargets.forEach(function (el) {
      el.classList.add("reveal");
      io.observe(el);
    });
  }

  // Guides hub audience filter
  var filters = document.querySelectorAll(".guide-filter");
  filters.forEach(function (btn) {
    btn.addEventListener("click", function () {
      var tag = btn.getAttribute("data-filter");
      filters.forEach(function (b) { b.classList.toggle("active", b === btn); });
      document.querySelectorAll(".guide-grid .guide-card").forEach(function (card) {
        var tags = (card.getAttribute("data-audience") || "").split(" ");
        card.hidden = tag !== "all" && tags.indexOf(tag) === -1;
      });
    });
  });

  // Highlight the current section in an article's table of contents
  var tocLinks = document.querySelectorAll(".toc a");
  if (tocLinks.length && "IntersectionObserver" in window) {
    var byId = {};
    tocLinks.forEach(function (a) { byId[a.getAttribute("href").slice(1)] = a; });
    var tocIo = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting && byId[entry.target.id]) {
          tocLinks.forEach(function (a) { a.classList.remove("active"); });
          byId[entry.target.id].classList.add("active");
        }
      });
    }, { rootMargin: "0px 0px -70% 0px" });
    Object.keys(byId).forEach(function (id) {
      var h = document.getElementById(id);
      if (h) tocIo.observe(h);
    });
  }
});

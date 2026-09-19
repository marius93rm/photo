(function () {
  "use strict";

  const body = document.body;
  const header = document.querySelector("#header");
  const navMenu = document.querySelector("#navmenu");
  const navLinks = Array.from(document.querySelectorAll("#navmenu a"));
  const mobileNavToggle = document.querySelector(".mobile-nav-toggle");
  const scrollTop = document.querySelector("#scroll-top");
  const prefersReducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)");

  function toggleScrolled() {
    if (!header || (!header.classList.contains("scroll-up-sticky") && !header.classList.contains("sticky-top") && !header.classList.contains("fixed-top"))) {
      return;
    }

    body.classList.toggle("scrolled", window.scrollY > 100);
  }

  function toggleScrollTop() {
    if (scrollTop) {
      scrollTop.classList.toggle("active", window.scrollY > 100);
    }
  }

  function setMobileNav(open, restoreFocus = false) {
    body.classList.toggle("mobile-nav-active", open);

    if (!mobileNavToggle) return;

    mobileNavToggle.setAttribute("aria-expanded", String(open));
    mobileNavToggle.setAttribute("aria-label", open ? "Close navigation" : "Open navigation");

    const icon = mobileNavToggle.querySelector("use");
    if (icon) {
      icon.setAttribute("href", open ? "#icon-close" : "#icon-menu");
    }

    if (open) {
      navLinks[0]?.focus();
    } else if (restoreFocus) {
      mobileNavToggle.focus();
    }
  }

  document.addEventListener("scroll", () => {
    toggleScrolled();
    toggleScrollTop();
  }, { passive: true });

  window.addEventListener("load", () => {
    toggleScrolled();
    toggleScrollTop();
  });

  if (mobileNavToggle) {
    mobileNavToggle.addEventListener("click", () => {
      setMobileNav(!body.classList.contains("mobile-nav-active"));
    });
  }

  navLinks.forEach((link) => {
    link.addEventListener("click", () => {
      if (body.classList.contains("mobile-nav-active")) {
        setMobileNav(false);
      }
    });
  });

  if (navMenu) {
    navMenu.addEventListener("click", (event) => {
      if (event.target === navMenu && body.classList.contains("mobile-nav-active")) {
        setMobileNav(false, true);
      }
    });
  }

  document.addEventListener("keydown", (event) => {
    if (!mobileNavToggle || !body.classList.contains("mobile-nav-active")) return;

    if (event.key === "Escape") {
      event.preventDefault();
      setMobileNav(false, true);
      return;
    }

    if (event.key !== "Tab" || navLinks.length === 0) return;

    const firstFocusable = navLinks[0];
    const lastFocusable = mobileNavToggle;

    if (event.shiftKey && document.activeElement === firstFocusable) {
      event.preventDefault();
      lastFocusable.focus();
    } else if (!event.shiftKey && document.activeElement === lastFocusable) {
      event.preventDefault();
      firstFocusable.focus();
    }
  });

  window.addEventListener("resize", () => {
    if (window.innerWidth >= 1200 && body.classList.contains("mobile-nav-active")) {
      setMobileNav(false);
    }
  });

  if (scrollTop) {
    scrollTop.addEventListener("click", (event) => {
      event.preventDefault();
      window.scrollTo({ top: 0, behavior: prefersReducedMotion.matches ? "auto" : "smooth" });
    });
  }

  if (typeof GLightbox === "function" && document.querySelector(".glightbox")) {
    GLightbox({ selector: ".glightbox" });
  }
})();

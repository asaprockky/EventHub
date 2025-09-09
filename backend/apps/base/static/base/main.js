// UI Animations & Interactivity

// Helper: Animate elements on scroll
function animateOnScroll(selector, animationClass = 'animate-in') {
  const elements = document.querySelectorAll(selector);
  const observer = new IntersectionObserver(entries => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add(animationClass);
        observer.unobserve(entry.target);
      }
    });
  }, { threshold: 0.15 });
  elements.forEach(el => observer.observe(el));
}

// Animate hero section on load
window.addEventListener('DOMContentLoaded', () => {
  const hero = document.querySelector('.hero-content');
  if (hero) {
    hero.classList.add('animate-hero');
  }
});

// Animate category cards
animateOnScroll('.category-card', 'fade-in-up');

// Animate event cards
animateOnScroll('.event-card', 'fade-in-up');

// Animate "How It Works" steps
animateOnScroll('.step', 'fade-in-up');

// Mobile menu toggle
const menuToggle = document.querySelector('.mobile-menu-toggle');
const navLinks = document.querySelector('.nav-links');
if (menuToggle && navLinks) {
  menuToggle.addEventListener('click', () => {
    navLinks.classList.toggle('nav-open');
    menuToggle.classList.toggle('open');
  });
}

// Card hover effect (for touch devices too)
function addCardHover(selector) {
  document.querySelectorAll(selector).forEach(card => {
    card.addEventListener('mouseenter', () => card.classList.add('hovered'));
    card.addEventListener('mouseleave', () => card.classList.remove('hovered'));
    card.addEventListener('touchstart', () => card.classList.add('hovered'));
    card.addEventListener('touchend', () => card.classList.remove('hovered'));
  });
}
addCardHover('.category-card');
addCardHover('.event-card');

// Optional: Animate footer social icons on hover
document.querySelectorAll('.social-links a').forEach(link => {
  link.addEventListener('mouseenter', () => link.classList.add('icon-bounce'));
  link.addEventListener('mouseleave', () => link.classList.remove('icon-bounce'));
});
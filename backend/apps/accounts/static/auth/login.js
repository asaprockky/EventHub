// Password visibility toggle
document.querySelectorAll('.password-toggle').forEach(btn => {
  btn.addEventListener('click', function () {
    const input = this.parentElement.querySelector('input[type="password"], input[type="text"]');
    if (input) {
      if (input.type === 'password') {
        input.type = 'text';
        this.querySelector('i').classList.remove('fa-eye');
        this.querySelector('i').classList.add('fa-eye-slash');
      } else {
        input.type = 'password';
        this.querySelector('i').classList.remove('fa-eye-slash');
        this.querySelector('i').classList.add('fa-eye');
      }
    }
  });
});

// Mobile menu toggle
const menuToggle = document.querySelector('.mobile-menu-toggle');
const navLinks = document.querySelector('.nav-links');
menuToggle?.addEventListener('click', () => {
  navLinks.classList.toggle('active');
  menuToggle.classList.toggle('open');
});

// Optional: Prevent multiple form submissions
const authForm = document.querySelector('.auth-form');
authForm?.addEventListener('submit', function (e) {
  const btn = this.querySelector('button[type="submit"]');
  btn.disabled = true;
  btn.textContent = 'Signing in...';
});
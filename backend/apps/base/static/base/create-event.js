// Show/hide gender balance details based on radio selection
document.querySelectorAll('input[name="genderBalance"]').forEach(radio => {
  radio.addEventListener('change', function () {
    const details = document.querySelector('.gender-balance-details');
    if (this.value === 'mixed') {
      details.style.display = 'block';
    } else {
      details.style.display = 'none';
      document.getElementById('male-spots').value = '';
      document.getElementById('female-spots').value = '';
    }
  });
});

// Image upload preview
const imageInput = document.getElementById('event-image');
const uploadArea = document.querySelector('.upload-area');
imageInput?.addEventListener('change', function () {
  if (this.files && this.files[0]) {
    const reader = new FileReader();
    reader.onload = function (e) {
      uploadArea.innerHTML = `<img src="${e.target.result}" alt="Cover Preview" style="max-width:100%;border-radius:12px;">`;
    };
    reader.readAsDataURL(this.files[0]);
  }
});

// Drag & drop for image upload
uploadArea?.addEventListener('click', () => imageInput.click());
uploadArea?.addEventListener('dragover', e => {
  e.preventDefault();
  uploadArea.classList.add('dragover');
});
uploadArea?.addEventListener('dragleave', () => {
  uploadArea.classList.remove('dragover');
});
uploadArea?.addEventListener('drop', e => {
  e.preventDefault();
  uploadArea.classList.remove('dragover');
  if (e.dataTransfer.files.length) {
    imageInput.files = e.dataTransfer.files;
    imageInput.dispatchEvent(new Event('change'));
  }
});

// Mobile menu toggle
const menuToggle = document.querySelector('.mobile-menu-toggle');
const navLinks = document.querySelector('.nav-links');
menuToggle?.addEventListener('click', () => {
  navLinks.classList.toggle('active');
  menuToggle.classList.toggle('open');
});

// Optional: Form validation feedback
document.querySelector('.event-form')?.addEventListener('submit', function (e) {
  const title = document.getElementById('event-title').value.trim();
  const desc = document.getElementById('event-description').value.trim();
    if (!title || !desc) {
      alert('Please fill in all required fields.');
    }
  });
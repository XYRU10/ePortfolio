// Get modal elements
const modal = document.getElementById('myModal');
const closeModal = document.getElementById('closeModal');

// Function to open the modal and display project details
function openModal(title, description, image) {
    console.log('Modal Opened'); // Add this line to check if the function is triggered
    // Set the modal content
    document.getElementById('modalTitle').innerText = title;
    document.getElementById('modalDescription').innerText = description;
    document.getElementById('modalImage').src = image;
  
    // Show the modal
    modal.classList.remove('hidden');
}
  
// Close the modal when the user clicks the close button
closeModal.addEventListener('click', () => {
  modal.classList.add('hidden');
});

// Close the modal if the user clicks outside the modal content
window.addEventListener('click', (e) => {
  if (e.target === modal) {
    modal.classList.add('hidden');
  }
});

function openModal(title, description, image) {
  console.log('Modal Opened'); // Add this line to check if the function is triggered
  // Set the modal content
  document.getElementById('modalTitle').innerText = title;
  document.getElementById('modalDescription').innerText = description;
  document.getElementById('modalImage').src = image;

  // Show the modal
  modal.classList.remove('hidden');
}


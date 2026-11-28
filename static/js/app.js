// Get the HTML elements
const imageInput = document.querySelector('#item-image');
const imagePreview = document.querySelector('#image-preview');
const imageMessage = document.querySelector('#image-message');
const removeButton = document.querySelector('#remove-image');

// When the user chooses an image
imageInput.addEventListener('change', function() {

    const file = imageInput.files[0];

    if (file) {

        // Create a temporary URL for the image
        const imageURL = URL.createObjectURL(file);

        // Show the image preview
        imagePreview.src = imageURL;
        imagePreview.style.display = 'block';

        // Update the message
        imageMessage.textContent = 'Image added ✓';

        // Disable choosing another image
        imageInput.disabled = true;

        // Show the remove button
        removeButton.style.display = 'block';
    }

});

// When the user clicks Remove image
removeButton.addEventListener('click', function() {

    // Clear the selected file
    imageInput.value = '';

    // Hide the preview
    imagePreview.src = '';
    imagePreview.style.display = 'none';

    // Reset the message
    imageMessage.textContent = 'No image selected';

    // Allow the user to choose again
    imageInput.disabled = false;

    // Hide the remove button
    removeButton.style.display = 'none';

});
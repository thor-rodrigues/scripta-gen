// Wait until the DOM is fully loaded
document.addEventListener("DOMContentLoaded", function () {
    // Get the document type buttons and the style section container
    const documentTypeButtons = document.querySelectorAll('.option-buttons .btn');
    let styleSection;
    let generateButton = document.querySelector('.generate-btn');
    let downloadButton = document.querySelector('.download-btn');

    // Variables to store the selected document type and style
    let selectedDocumentType = null;
    let selectedStyle = null;

    // Initially hide the Generate and Download buttons
    generateButton.style.display = 'none';
    downloadButton.style.display = 'none';

    // Function to create the style selection section
    function createStyleSection() {
        // If the style section already exists, remove it to create a new one
        if (styleSection) {
            styleSection.remove();
        }

        // Create the style section div
        styleSection = document.createElement('div');
        styleSection.classList.add('style-section');

        // Create the heading for the style section
        const heading = document.createElement('h2');
        heading.textContent = 'Choose Your Style';
        heading.classList.add('container-heading'); // Apply the heading style

        // Create the container for the style buttons
        const buttonContainer = document.createElement('div');
        buttonContainer.classList.add('option-buttons');

        // Create style buttons with the updated names
        const styles = ['Modern', 'Elegant', 'Energy'];
        styles.forEach(style => {
            const button = document.createElement('button');
            button.type = 'button';
            button.classList.add('btn', 'btn-outline-primary');
            button.textContent = style;

            // Add click event to set active class and remove from others
            button.addEventListener('click', function () {
                // Remove active class from all style buttons
                document.querySelectorAll('.style-section .btn').forEach(btn => btn.classList.remove('active'));
                button.classList.add('active');

                // Save the selected style to the variable
                selectedStyle = style;

                // Show the "Generate Revised File" button after style selection
                generateButton.style.display = 'block';
            });

            buttonContainer.appendChild(button);
        });

        // Append the heading and buttons to the style section
        styleSection.appendChild(heading);
        styleSection.appendChild(buttonContainer);

        // Insert the style section before the "Generate Revised File" button
        generateButton.parentNode.insertBefore(styleSection, generateButton);
    }

    // Add click event listeners to the document type buttons
    documentTypeButtons.forEach(button => {
        button.addEventListener('click', function () {
            // Remove active class from all document type buttons and add it to the clicked one
            documentTypeButtons.forEach(btn => btn.classList.remove('active'));
            this.classList.add('active');

            // Save the selected document type to the variable
            selectedDocumentType = this.textContent.trim();

            // After the user selects a document type, show the "Choose Your Style" section
            createStyleSection();

            // Hide the Generate and Download buttons (in case they were previously visible)
            generateButton.style.display = 'none';
            downloadButton.style.display = 'none';
        });
    });

    // Add click event listener to the "Generate Revised File" button
    generateButton.addEventListener('click', function () {
        // Show the "Download Revised File" button after clicking the Generate button
        downloadButton.style.display = 'block';

        // Now the selectedDocumentType and selectedStyle can be used
        console.log("Selected Document Type:", selectedDocumentType);
        console.log("Selected Style:", selectedStyle);

        // You can pass these variables to another function or store them for further use
    });
});

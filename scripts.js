// Wait until the DOM is fully loaded
document.addEventListener("DOMContentLoaded", function () {
    // Variables to store the section and buttons
    const optionButtons = document.querySelectorAll('.option-buttons .btn');
    let styleSection;

    // Function to create the new style selection section
    function createStyleSection(styles) {
        if (styleSection) {
            // Remove existing section if already present
            styleSection.remove();
        }

        // Create a new section div
        styleSection = document.createElement('div');
        styleSection.classList.add('style-section');

        // Create h2 heading
        const heading = document.createElement('h2');
        heading.textContent = 'Choose Your Style';
        heading.classList.add('container-heading'); // Apply the same class as the Upload Your File h2

        // Create button container
        const buttonContainer = document.createElement('div');
        buttonContainer.classList.add('option-buttons');

        // Create buttons for the styles
        styles.forEach((style, index) => {
            const button = document.createElement('button');
            button.type = 'button';
            button.classList.add('btn', 'btn-outline-primary');
            button.textContent = `Style ${style}`;
            buttonContainer.appendChild(button);
        });

        // Append heading and buttons to the style section
        styleSection.appendChild(heading);
        styleSection.appendChild(buttonContainer);

        // Insert the new section between the option buttons and the file-drop-area
        const container = document.querySelector('.container');
        const fileDropArea = document.querySelector('.file-drop-area'); // Target the file-drop-area

        container.insertBefore(styleSection, fileDropArea); // Insert the new section before file-drop-area
    }

    // Function to update styles based on the selected option
    function updateStyles(option) {
        let styles;
        switch (option) {
            case 'Resume':
                styles = [1, 2, 3];
                break;
            case 'Letter':
                styles = [4, 5, 6];
                break;
            case 'Report':
                styles = [7, 8, 9];
                break;
        }
        createStyleSection(styles);
    }

    // Add event listener for the option buttons
    optionButtons.forEach(button => {
        button.addEventListener('click', function () {
            const selectedOption = this.textContent.trim();
            updateStyles(selectedOption);
        });
    });
});
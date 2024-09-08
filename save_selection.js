const fs = require('fs');

// Retrieve the command line arguments for the selected values
const selectedDocumentType = process.argv[2];
const selectedStyle = process.argv[3];

// Define the data structure to store the selected values
const data = {
    user_selected_document: selectedDocumentType,
    user_selected_style: selectedStyle
};

// Write the data to a JSON file
fs.writeFileSync('user_selection.json', JSON.stringify(data, null, 2));

console.log("User selection saved successfully.");
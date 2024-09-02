from langflow.load import run_flow_from_json
from weasyprint import HTML, CSS
import os

# Ask the user to enter the directory path (this will not be used for saving files)
directory_path = input("Please enter the directory path: ")

# Define the tweaks dictionary with the user-provided directory path
TWEAKS = {
    "Directory-iIPoR": {
        "path": directory_path,
    },
    "AnthropicModel-3yGtO": {
        "anthropic_api_key": "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",
    }
}

result = run_flow_from_json(flow="src/resume-generator.json",
                            input_value="message",
                            fallback_to_env_vars=True,  # False by default
                            tweaks=TWEAKS)

answer = result[0].outputs[0].results["message"].text

# Define project root directory (assuming this script is run from the project root)
project_root = os.path.dirname(os.path.abspath(__file__))

# Define paths for saving files within the project directory
html_directory = os.path.join(project_root, 'temp', 'html')
pdf_directory = os.path.join(project_root, 'temp', 'pdf')

# Define file paths
html_file_path = os.path.join(html_directory, 'output.html')
pdf_file_path = os.path.join(pdf_directory, 'output.pdf')

# Save the HTML content to a file
with open(html_file_path, 'w') as html_file:
    html_file.write(answer)

# Convert the HTML file to PDF
HTML(html_file_path).write_pdf(pdf_file_path)

print(f"HTML file saved at: {html_file_path}")
print(f"PDF file generated and saved at: {pdf_file_path}")

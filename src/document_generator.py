from langflow.load import run_flow_from_json
from weasyprint import HTML, CSS

# Ask the user to enter the directory path
directory_path = input("Please enter the directory path: ")

# Define the tweaks dictionary with the user-provided directory path
TWEAKS = {
    "Directory-iIPoR": {
        "path": directory_path,
    },
    "AnthropicModel-3yGtO": {
        "anthropic_api_key": "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",
}}

# Run the flow with the directory path provided by the user
result = run_flow_from_json(flow="src/resume-generator.json",
                            input_value="message",
                            tweaks=TWEAKS)

# Extract the answer from the result
answer = result[0].outputs[0].results["message"].text


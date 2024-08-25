import streamlit as st
import time
import tempfile
import os

# Function to inject custom CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Inject additional CSS to change background color
st.markdown(
    """
    <style>
    /* Set background color for the main content area */
    .main {
        background-color: #fffefa;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Load the main CSS file
local_css("styles/styles.css")

# Create a header for the landing page using a custom CSS class
st.markdown('<h1 class="custom-title">ScriptaGen is the best way to create documents</h1>', unsafe_allow_html=True)

# Add a centered "Start creating" button with custom styling
start_button_html = """
<div style="text-align: center;">
    <button class="custom-button selected">Start creating</button>
</div>
"""
st.markdown(start_button_html, unsafe_allow_html=True)

# Add a customized horizontal line divider
st.markdown('<hr class="custom-hr">', unsafe_allow_html=True)

# Description text
st.markdown("""
<div class="custom-markdown">
    ScriptaGen allows you to effortlessly create professional-looking content, such as resumes, letters, and reports.  
    Simply upload your existing documents, and ScriptaGen's powerful AI will ensure your new documents are polished and presented in the best possible format.
</div>
""", unsafe_allow_html=True)

# Add the vertical steps section
st.markdown(
    """
    <div class="step-container">
        <div class="step-box">
            <div class="step-number">01</div>
            <div class="step-text">Select the document type and format you want.</div>
        </div>
        <div class="step-box">
            <div class="step-number">02</div>
            <div class="step-text">Upload files containing the information you want to use.</div>
        </div>
        <div class="step-box">
            <div class="step-number">03</div>
            <div class="step-text">Select "Generate" and download your document!</div>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

# Initialize session state variables
if 'document_type' not in st.session_state:
    st.session_state['document_type'] = None

if 'formatting_option' not in st.session_state:
    st.session_state['formatting_option'] = None

if 'generate_clicked' not in st.session_state:
    st.session_state['generate_clicked'] = False

# Add buttons for selecting the type of document using HTML
st.markdown("#### Select the type of document you want to work on:")

# Use HTML to render buttons
button_html = """
<div style="text-align: center;">
    <button class="custom-button {0}" onclick="window.location.href='?document_type=Resume'">Resume</button>
    <button class="custom-button {1}" onclick="window.location.href='?document_type=Letter'">Letter</button>
    <button class="custom-button {2}" onclick="window.location.href='?document_type=Report'">Report</button>
</div>
""".format(
    "selected" if st.session_state['document_type'] == "Resume" else "",
    "selected" if st.session_state['document_type'] == "Letter" else "",
    "selected" if st.session_state['document_type'] == "Report" else ""
)

st.markdown(button_html, unsafe_allow_html=True)

# Display formatting options if a document type is selected
if st.session_state['document_type']:
    st.markdown("#### Select the formatting option:")

    format_html = """
    <div style="text-align: center;">
        <button class="custom-button {0}" onclick="window.location.href='?formatting_option=Modern'">Modern</button>
        <button class="custom-button {1}" onclick="window.location.href='?formatting_option=Classic'">Classic</button>
        <button class="custom-button {2}" onclick="window.location.href='?formatting_option=Dynamic'">Dynamic</button>
        <button class="custom-button {3}" onclick="window.location.href='?formatting_option=Bold'">Bold</button>
    </div>
    """.format(
        "selected" if st.session_state['formatting_option'] == "Modern" else "",
        "selected" if st.session_state['formatting_option'] == "Classic" else "",
        "selected" if st.session_state['formatting_option'] == "Dynamic" else "",
        "selected" if st.session_state['formatting_option'] == "Bold" else ""
    )

    st.markdown(format_html, unsafe_allow_html=True)

# Show image and file uploader if both document type and formatting option are selected
if st.session_state['document_type'] and st.session_state['formatting_option']:
    # Define the image path based on the selected options (corrected)
    image_path = os.path.join('images', f"{st.session_state['document_type'].lower()}_{st.session_state['formatting_option'].lower()}.png")
    
    # Display the image with resizing to 50% of original width
    if os.path.exists(image_path):
        st.image(image_path, caption=f"Example of a {st.session_state['document_type']} in {st.session_state['formatting_option']} format", width=400)
    else:
        st.error(f"Image not found: {image_path}")

    # Add a file uploader component
    uploaded_file = st.file_uploader("Upload a document to begin", type=["docx", "pdf", "txt"])

    # Check if a file is uploaded
    if uploaded_file is not None:
        st.success("File uploaded successfully!")

        # Create a temporary directory to store uploaded files
        with tempfile.TemporaryDirectory() as temp_dir:
            # Save the uploaded file to the temporary directory
            file_path = os.path.join(temp_dir, uploaded_file.name)
            with open(file_path, "wb") as f:
                f.write(uploaded_file.getbuffer())

            st.write(f"File saved at: {file_path}")

            # Show the "Generate" button
            if st.button("Generate"):
                st.session_state['generate_clicked'] = True

            # If the "Generate" button is clicked, show a progress spinner for 5 seconds
            if st.session_state['generate_clicked']:
                with st.spinner('Processing your document...'):
                    time.sleep(5)  # Simulate processing time
                st.success("Document generated successfully!")

                # Display the "Download document" button
                st.button("Download document")

# Footer or contact information
st.markdown("---")
st.markdown("For support or more information, contact [support@scripta-gen.com](mailto:support@scripta-gen.com).")

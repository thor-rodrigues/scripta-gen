import streamlit as st
import time
import tempfile
import os

# Load external CSS file
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Load the CSS file
local_css("src/styles/styles.css")

# Create a header for the landing page using custom CSS class
st.markdown('<h1 class="custom-title">ScriptaGen is the best way to create documents</h1>', unsafe_allow_html=True)

# Continue with the rest of your Streamlit app
st.markdown("""
<div class="custom-markdown">
    **ScriptaGen allows you to effortlessly create professional-looking content, such as resumes, letters, and reports.**  
    Simply upload your existing documents, and ScriptaGen's powerful AI will ensure your new documents are polished and presented in the best possible format.
</div>
""", unsafe_allow_html=True)

# The rest of your Streamlit code here...

# Initialize session state variables
if 'document_type' not in st.session_state:
    st.session_state['document_type'] = None

if 'formatting_option' not in st.session_state:
    st.session_state['formatting_option'] = None

if 'generate_clicked' not in st.session_state:
    st.session_state['generate_clicked'] = False

# Add buttons for selecting the type of document
st.markdown("#### Select the type of document you want to work on:")
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("Resume"):
        st.session_state['document_type'] = "Resume"
        st.session_state['formatting_option'] = None  # Reset formatting option on new selection

with col2:
    if st.button("Letter"):
        st.session_state['document_type'] = "Letter"
        st.session_state['formatting_option'] = None  # Reset formatting option on new selection

with col3:
    if st.button("Report"):
        st.session_state['document_type'] = "Report"
        st.session_state['formatting_option'] = None  # Reset formatting option on new selection

# Display formatting options if a document type is selected
if st.session_state['document_type']:
    st.markdown("#### Select the formatting option:")
    col4, col5, col6, col7 = st.columns(4)

    with col4:
        if st.button("Modern"):
            st.session_state['formatting_option'] = "Modern"

    with col5:
        if st.button("Classic"):
            st.session_state['formatting_option'] = "Classic"

    with col6:
        if st.button("Dynamic"):
            st.session_state['formatting_option'] = "Dynamic"

    with col7:
        if st.button("Bold"):
            st.session_state['formatting_option'] = "Bold"

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

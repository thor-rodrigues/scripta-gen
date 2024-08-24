import streamlit as st

# Set the title of the landing page
st.set_page_config(page_title="ScriptaGen - Document Generator", page_icon=":memo:")

# Create a header for the landing page
st.title("ScriptaGen is the best way to create documents")

# Combined and concise introduction text
st.markdown("""
**ScriptaGen allows you to effortlessly create professional-looking content, such as resumes, letters, and reports.**  
Simply upload your existing documents, and ScriptaGen's powerful AI will ensure your new documents are polished and presented in the best possible format.
""")

# Section to get started
st.markdown("### Get Started")

# Initialize session state variables
if 'document_type' not in st.session_state:
    st.session_state['document_type'] = None

if 'formatting_option' not in st.session_state:
    st.session_state['formatting_option'] = None

# Add buttons for selecting the type of document
st.markdown("#### Select the type of document you want to work on:")
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("Resume"):
        st.session_state['document_type'] = "Resume"

with col2:
    if st.button("Letter"):
        st.session_state['document_type'] = "Letter"

with col3:
    if st.button("Report"):
        st.session_state['document_type'] = "Report"

# Display formatting options regardless of document type selection
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

# Show image based on the selected document type and formatting option
if st.session_state['document_type'] and st.session_state['formatting_option']:
    # Define the image path based on the selected options
    image_path = f"images/{st.session_state['document_type'].lower()}_{st.session_state['formatting_option'].lower()}.png"
    
    # Display the image
    st.image(image_path, caption=f"Example of a {st.session_state['document_type']} in {st.session_state['formatting_option']} format")

    # Add a file uploader component, only show if both selections are made
    uploaded_file = st.file_uploader("Upload a document to begin", type=["docx", "pdf", "txt"])

    # Check if a file is uploaded and provide feedback
    if uploaded_file is not None:
        st.success("File uploaded successfully!")

# Footer or contact information
st.markdown("---")
st.markdown("For support or more information, contact [support@scripta-gen.com](mailto:support@scripta-gen.com).")

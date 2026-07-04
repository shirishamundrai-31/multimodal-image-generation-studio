import streamlit as st
from PIL import Image
from image_generator import generate_image

st.set_page_config(
    page_title="Multimodal Image Generation Studio",
    page_icon="🎨",
    layout="centered"
)

st.title("🎨 Multimodal Image Generation Studio")

st.write("Generate AI images from text prompts for free!")

prompt = st.text_area(
    "Enter your prompt",
    placeholder="Example: A futuristic AI engineer working in a cyberpunk city"
)

if st.button("Generate Image"):

    if prompt.strip() == "":
        st.warning("Please enter a prompt.")

    else:

        with st.spinner("Generating image..."):

            image_path = generate_image(prompt)

            if image_path:

                st.success("Image Generated Successfully!")

                image = Image.open(image_path)

                st.image(image, use_container_width=True)

                with open(image_path, "rb") as file:
                    st.download_button(
                        label="⬇ Download Image",
                        data=file,
                        file_name="generated_image.png",
                        mime="image/png"
                    )

            else:

                st.error("Failed to generate image.")

# import streamlit as st
# import requests
#
# st.title("AI Storyteller")
#
# genre = st.selectbox("Choose a genre", ["Fantasy", "Mystery", "Sci-Fi"])
# characters = st.text_input("Enter character names (comma separated)")
# num_paragraphs = st.slider("Number of paragraphs", 1, 10, 3)
#
# if st.button("Generate Story"):
#     data = {
#         "genre": genre,
#         "characters": characters,
#         "sections": num_paragraphs
#     }
#     with st.spinner("Generating..."):
#         res = requests.post("http://localhost:8000/generate", json=data)
#         result = res.json()
#         print(result)
#         st.subheader("Summary")
#         st.write(result.get("summary", "No summary found."))
#         st.subheader("Story")
#         paragraphs = result.get("paragraphs", [])
#         # images = result.get("images", [])
#         # for i, (para, img) in enumerate(zip(paragraphs, images)):
#         #     st.markdown(f"**Paragraph {i+1}:** {para}")
#         #     st.image(img)
#         for i, (para) in enumerate(zip(paragraphs)):
#             st.markdown(f"**Paragraph {i + 1}:** {para}")


import streamlit as st
import requests

st.title("📝 AI Storyteller")

# --- User Input ---
genre = st.selectbox("Choose a genre", ["Fantasy", "Mystery", "Sci-Fi"])
characters = st.text_input("Enter character names (comma separated)")
num_paragraphs = st.slider("Number of paragraphs", 1, 10, 3)

layout = st.radio("Choose layout", ["Image above text", "Image beside text"])

# --- Generate Story ---
if st.button("Generate Story"):
    data = {
        "genre": genre,
        "characters": characters,
        "sections": num_paragraphs
    }

    with st.spinner("Generating story and images..."):
        res = requests.post("http://localhost:8000/generate", json=data)
        result = res.json()

    st.subheader("📖 Summary")
    st.write(result.get("summary", "No summary found."))

    st.subheader("📚 Story")
    paragraphs = result.get("paragraphs", [])
    images = result.get("images", [])

    for i, (para, img_path) in enumerate(zip(paragraphs, images)):
        img_url = f"http://localhost:8000{img_path}"

        st.markdown(f"### Paragraph {i + 1}")

        if layout == "Image above text":
            st.image(img_url, use_column_width=True)
            st.write(para)

        elif layout == "Image beside text":
            col1, col2 = st.columns([1, 2])
            with col1:
                st.image(img_url, use_column_width=True)
            with col2:
                st.write(para)

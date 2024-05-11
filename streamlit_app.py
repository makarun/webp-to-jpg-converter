import streamlit as st
from PIL import Image

st.title('webp-to-jpg-converter')
uploaded_files = st.file_uploader("", accept_multiple_files=True, type=['webp'])
for im in uploaded_files:
    im_name = im.name[:-5]+'.jpg'
    im = Image.open(im).convert('RGB')
    im.save('images/'+im_name, 'jpeg')
    st.image(im, width=600)
    with open("images/" + im_name,"rb") as file:
        st.download_button(
            label="Download image",
            data=file,
            file_name=im_name,
            mime="images/"+im_name.split('.')[-1]
        )
    
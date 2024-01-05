import streamlit as st
from langchain.prompts import PromptTemplate
from langchain_community.llms import CTransformers


# Function to get response from LLAma 2 model
def getLLamaresponse(input_text, no_words, product_category):
    llm = CTransformers(
        model="models/llama-2-7b-chat.ggmlv3.q8_0.bin",
        model_type="llama",
        config={
            "max_new_tokens": 256,
            "temperature": 0.01
        }
    )

    template = """
        Write a product description in bullet points for product '{input_text}' 
        under category '{product_category}' to list on an ecommerce website within {no_words} words.
        """

    prompt = PromptTemplate(
        template=template, input_variables=["product_category", "input_text", "no_words"])

    response = llm(
        prompt.format(product_category=product_category, input_text=input_text, no_words=no_words))

    print(response)
    return response


st.set_page_config(
    page_title="Generate Product Description",
    page_icon='🤖',
    layout='centered',
    initial_sidebar_state='collapsed')

st.header("Generate Product Description 🤖")
input_text = st.text_input("Enter the Product Title")

col1, col2 = st.columns([5, 5])

with col1:
    no_words = st.text_input('No of Words')
with col2:
    product_category = st.selectbox(
        "Product Category",
        ("Women's Fashion", "Men's Fashion", "Girls' Fashion", "Boys' Fashion"), index=0)

submit = st.button("Generate")

# Final response
if submit:
    st.write(getLLamaresponse(input_text, no_words, product_category))

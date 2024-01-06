# LLM-Demos
This repo will contain LLM demo projects

## Projects
### Product Description Generation using LLAma2-7B-Chat
- https://python.langchain.com/docs/integrations/llms/ctransformers
- Download the `llama-2-7b-chat.ggmlv3.q8_0.bin` GGML model from: https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGML/tree/main and put it in `models` dir inside the `llama2-product-description` dir

- Goto project dir `llama2-product-description` and run all the following commands from project dir,
```bash 
cd llama2-product-description
```

- Run the below command to Install dependencies,
```bash 
pip install -r requirements.txt 
```

- To run the project, run the below command from `llama2-product-description` dir,
```bash 
streamlit run app.py
```

- To test the app, enter the `localhost:8501` (default streamlit port) in the browser


### Q&A using OpenAI embeddings & OpenAI text-davinci model with Pinecone Database
- Signup & login on `Pinecone` with this link: https://app.pinecone.io/

- Goto project dir `openai-question-answer` and run all the following commands from project dir,
```bash 
cd llama2-product-description
```

- create a dir `documents` and put your relevant PDF documents inside this dir

- Run the below command to Install dependencies,
```bash 
pip install -r requirements.txt 
```

- To run the project, run the below command dir,
```bash 
python3 app.py
```

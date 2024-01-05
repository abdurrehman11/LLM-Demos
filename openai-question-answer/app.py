import os
import openai
import langchain
import pinecone 
from langchain.document_loaders import PyPDFDirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings.openai import OpenAIEmbeddings
from langchain_community.llms import OpenAI
from langchain.chains.question_answering import load_qa_chain
from langchain.vectorstores import Pinecone
from dotenv import load_dotenv


load_dotenv()


def read_doc(directory):
    file_loader = PyPDFDirectoryLoader(directory)
    documents = file_loader.load()
    return documents


def chunk_data(docs, chunk_size=800, chunk_overlap=50):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    texts = text_splitter.split_documents(docs)
    return texts


docs = read_doc('documents/')
print(len(docs))

texts = chunk_data(docs=docs)
print(len(texts))


embeddings = OpenAIEmbeddings(api_key=os.environ['OPENAI_API_KEY'])
# print(embeddings)
# vectors = embeddings.embed_query("How are you?")
# print(len(vectors))

pinecone.init(
    api_key="5445b3e0-903f-4d57-9481-835d8cf35d0a",
    environment="gcp-starter"
)

index_name = "langchainvector"

if index_name not in pinecone.list_indexes():
    pinecone.create_index(name=index_name, metric="cosine", dimension=1536)
    print("Index created successfully.")
    docsearch = Pinecone.from_documents(docs, embeddings, index_name=index_name)
    print("Docsearch created successfully.")
else:
    docsearch = Pinecone.from_existing_index(index_name, embeddings)
    print(f"Loaded alraedy existing Docsearch from index: {index_name}")


def retrieve_query(query, topk=2):
    matching_results = docsearch.similarity_search(query, k=topk)
    return matching_results


llm = OpenAI(model_name="text-davinci-003", temperature=0.5)
chain = load_qa_chain(llm, chain_type="stuff")


# Search answers from VectorDB
def retrieve_answers(query):
    doc_search = retrieve_query(query)
    response = chain.run(input_documents=doc_search, question=query)
    return response


our_query = "How much the agriculture target will be increased by how many crore?"
answer = retrieve_answers(our_query)
print(answer)

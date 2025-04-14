import chromadb
from chromadb.utils import embedding_functions
from chromadb.config import Settings

# Connect with no authentication on the port of your choice 
chroma_client = chromadb.HttpClient(host='localhost', 
                                    port=8000,)

chroma_client.count_collections()

chroma_client.list_collections()

collection = chroma_client.get_collection(name='document_store')

collection.get()['ids'][:5]

from langchain_ollama import OllamaLLM

llm = OllamaLLM(model="llama2")

llm.invoke("how can I be better at coding ?")

from langchain_core.prompts import ChatPromptTemplate
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a world class engineer with more than 20y of experience."),
    ("user", "{input}")
])
chain = prompt | llm 
chain.invoke("how can I be better at coding ?")

from langchain_core.output_parsers import StrOutputParser

output_parser = StrOutputParser()
chain = prompt | llm | output_parser

chain.invoke("how can I be better at coding ?")

type(chain.invoke("how can I be better at coding ?"))

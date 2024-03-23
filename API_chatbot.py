import logging
import sys
import torch
from llama_index.llms.huggingface import HuggingFaceLLM
from llama_index.core import PromptTemplate
from llama_index.core import SimpleDirectoryReader
from llama_index.core import (
        VectorStoreIndex,
        ServiceContext,
        set_global_service_context,
        )

LLAMA2_7B_CHAT = "meta-llama/Llama-2-7b-hf"
VICUNA_7B = "lmsys/vicuna-7b-v1.5"

logging.basicConfig(stream=sys.stdout, level=logging.INFO)
logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))

selected_model = VICUNA_7B

SYSTEM_PROMPT = """You are an AI assistant that answers questions in a friendly manner, based on the given source documents. Here are some rules you always follow:
- Generate human readable output, avoid creating output with gibberish text.
- Generate only the requested output, don't include any other language before or after the requested output.
- Never say thank you, that you are happy to help, that you are an AI agent, etc. Just answer directly.
- Generate professional language typically used in business documents in North America.
- Never generate offensive or foul language.
"""

query_wrapper_prompt = PromptTemplate(
    "[INST]<<SYS>>\n" + SYSTEM_PROMPT + "<</SYS>>\n\n{query_str}[/INST] "
)

#Huggingface pipeline
llm = HuggingFaceLLM(
    context_window=4096,
    max_new_tokens=2048,
    generate_kwargs={"temperature": 0.0, "do_sample": False},
    #query_wrapper_prompt=query_wrapper_prompt,
    tokenizer_name=selected_model,
    model_name=selected_model,
    device_map="auto",
    # change these settings below depending on your GPU
    model_kwargs={"torch_dtype": torch.float16, "load_in_8bit": True},
)

#Cargamos los documentos
documents = SimpleDirectoryReader("./data/").load_data()

# De aqui es donde se crea algo similar a RAG
service_context = ServiceContext.from_defaults(
    llm=llm, embed_model="local:BAAI/bge-small-en"
)
# Indicamos el contexto global para el llm
set_global_service_context(service_context)
# Indicamos a VectorStore que cree indices en base a los documentos ya pasados por el modelo de embedding
index = VectorStoreIndex.from_documents(documents)

query_engine = index.as_query_engine()



from flask import Flask, request, jsonify


app = Flask(__name__)

@app.route('/prompt', methods=['POST'])
def prompt():
    try:
        # Get the input query from the request
        prompt = request.json.get('prompt')

        # Use the query engine to get a response
        response = query_engine.query(prompt)

        # Return the response in JSON format
        return jsonify({'response': str(response)})

    except Exception as e:
        # Handle any exceptions and return an error message
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    # Run the Flask app on port 5000
    app.run(port=5000)
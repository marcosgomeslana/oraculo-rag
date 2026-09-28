import os
import streamlit as st
from dotenv import load_dotenv, find_dotenv

# Componentes do LangChain e GROQ
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_groq import ChatGroq
from langchain_huggingface import HuggingFaceEmbeddings  # <-- Nova importação (Sem Ollama)

# 1. Carrega as variáveis de ambiente (Sua GROQ_API_KEY do .env)
load_dotenv(find_dotenv())

# 2. Inicializa o modelo de chat da GROQ (Nuvem)
model_groq = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0.2  # Baixa temperatura para manter a precisão jurídica
)

# 3. Função para processar PDFs e criar o banco de dados vetorial
@st.cache_resource
def load_pdf_data():
    path_dir = "documentos_juridicos"
    
    if not os.path.exists(path_dir):
        os.makedirs(path_dir)
        st.warning(f"Pasta '{path_dir}' criada. Adicione seus arquivos PDF nela e recarregue a página.")
        st.stop()

    loader = PyPDFDirectoryLoader(path_dir)
    documents = loader.load()
    
    if not documents:
        st.error(f"Nenhum arquivo PDF encontrado na pasta '{path_dir}'. Insira os documentos para o Oráculo funcionar.")
        st.stop()

    # Divisão do PDF em pedaços menores
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )
    docs_splitted = text_splitter.split_documents(documents)

    # Criamos os embeddings direto na memória do Python (Sem depender de servidores locais)
    # Esse modelo é multilíngue e funciona muito bem com termos em português
    embeddings = HuggingFaceEmbeddings(
        model_name="intfloat/multilingual-e5-small"
    )

    # Guarda os blocos de texto no FAISS
    vectorstore = FAISS.from_documents(docs_splitted, embeddings)
    return vectorstore.as_retriever(search_kwargs={"k": 4})

# Inicializa o buscador de contexto
retriever = load_pdf_data()

# 4. Interface do Usuário (Streamlit)
st.set_page_config(page_title="Oráculo Jurídico", page_icon="⚖️")
st.title("⚖️ Lex Metrics")
st.subheader("Base de Conhecimento: Documentos PDF (Groq Cloud)")

# Prompt Jurídico Formal
rag_template = """
Você é um assistente jurídico inteligente, altamente qualificado, detalhista e formal.
Seu objetivo é auxiliar estudantes de Direito, advogados e líderes jurídicos com base estrita nos documentos fornecidos.

Diretrizes de comportamento:
1. Responda de forma clara, objetiva, profissional e com tom juridicamente adequado.
2. Baseie sua resposta estritamente no contexto fornecido abaixo.
3. Se a resposta não puder ser determinada estritamente a partir do contexto, responda exatamente: "Não encontrei informações suficientes nos documentos disponíveis para responder a essa solicitação." Não tente inventar fatos.

Contexto dos documentos:
{context}

Pergunta do usuário: {question}
Resposta jurídica:
"""

prompt = ChatPromptTemplate.from_template(rag_template)

# Criação da Chain de execução na nuvem da Groq
chain = (
    {"context": retriever, "question": RunnablePassthrough()}
    | prompt
    | model_groq
)

# 5. Histórico de Mensagens
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if user_input := st.chat_input("Digite sua dúvida jurídica aqui..."):
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    with st.chat_message("assistant"):
        response_placeholder = st.empty()
        full_response = ""
        
        # Executa a chamada acelerada da Groq
        response_stream = chain.stream(user_input)
        
        for partial_response in response_stream:
            full_response += str(partial_response.content)
            response_placeholder.markdown(full_response + "▌")
            
        response_placeholder.markdown(full_response)

    st.session_state.messages.append({"role": "assistant", "content": full_response})
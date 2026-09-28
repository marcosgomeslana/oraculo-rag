# Oráculo IA

Aplicação de Inteligência Artificial desenvolvida em **Python** para consulta de documentos PDF utilizando **RAG (Retrieval-Augmented Generation)**.

O sistema processa documentos jurídicos, cria uma base de conhecimento vetorial e permite realizar perguntas sobre seu conteúdo. As respostas são geradas a partir dos trechos relevantes recuperados dos documentos.

## Tecnologias

* Python
* Streamlit
* LangChain
* Groq
* Llama 3.1
* Hugging Face Embeddings
* FAISS
* RAG
* PyPDF

## Como funciona

1. Os documentos PDF são adicionados à pasta `documentos_juridicos`.
2. O sistema processa e divide os documentos em trechos.
3. Os conteúdos são transformados em embeddings e armazenados no FAISS.
4. O sistema recupera os trechos relevantes para cada pergunta.
5. O modelo Llama 3.1 gera a resposta com base no contexto recuperado.

## Execução

Instale as dependências:

```bash
pip install -r requirements.txt
```

Configure sua chave da Groq no arquivo `.env`:

```env
GROQ_API_KEY=sua_chave_aqui
```

Execute a aplicação:

```bash
.\.venv\Scripts\python.exe -m streamlit run oracle.py
```

## Status

Projeto em desenvolvimento.

## Autor

**Marcos Gomes de Oliveira Lana**
Estudante de Análise e Desenvolvimento de Sistemas.

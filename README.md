<small>**🗺️ O Plano de Construção (Dividido em Partes)**</small>

Fase 1: Estruturação do Projeto e Instalação de Dependências (Onde estamos agora).

Fase 2: Criação da Base de Dados Simulada (O arquivo Excel de Jurimetria e a pasta de PDFs).

Fase 3: Construção do "Esqueleto" da Interface no Streamlit (Criando as abas/páginas).

Fase 4: Desenvolvimento do Dashboard de Jurimetria (Gráficos interativos com o Excel).

Fase 5: Integração do Oráculo Jurídico (O chatbot RAG com Groq que já validamos).

Fase 6: Testes, Ajustes de Prompt e Ajustes Finais.


<small>**Protótipo da Tela - WireFrame de Alta finalidade básico**</small>


<img width="1408" height="768" alt="tela-lexmetrics" src="https://github.com/user-attachments/assets/8278b902-3345-4659-9662-ef7e907f1b4d" />

##### Descrição
Dashboard de Jurimetria (Painel Superior): Esta seção apresenta as métricas que você planeja extrair do PostgreSQL. Ela é focada em dados estruturados:

      Gráficos e Estatísticas: Inclui gráficos de barra ("Taxas de Condenação por Juiz", "Tempo Médio de Julgamento"), gráficos de rosca ("Distribuição de Sentenças") e tabelas ("Valor Médio de Condenações").

      Filtros de Pesquisa: Localizados no canto superior direito, permitem refinar os dados por tribunal, ano, classe processual e origem (DataJud).

Oráculo (Painel Inferior): Esta seção é o chatbot que você está construindo, focada em dados não estruturados (o conteúdo dos PDFs):

      Interface de Chat: Mostra o fluxo da conversa, incluindo a sua pergunta ("Olá Oráculo..."), a resposta gerada pela IA e as referências diretas aos documentos jurídicos (documentos.juridicos).

      Status e Tecnologias: Indica que o sistema utiliza a nuvem (RAG Cloud) e exibe os estados das conexões (DataJud, Elasticsearch e Groq) no canto inferior direito.

Navegação Lateral: O menu à esquerda facilita a alternância entre as diferentes áreas do sistema (Dashboard, Jurimetria, Oráculo, etc.).



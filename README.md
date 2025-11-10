# sprint_5_project
Projeto da Sprint 5
🧩 Projeto: Dashboard de Vendas de Carros com Streamlit
📖 Descrição
Este projeto consiste em um aplicativo web interativo desenvolvido com Streamlit, que permite analisar anúncios de vendas de carros nos Estados Unidos.
O app carrega um conjunto de dados em formato CSV e possibilita a visualização gráfica de informações importantes sobre os veículos anunciados.

🚗 Funcionalidades
📊 Criação de Histogramas:
Exibe a distribuição da quilometragem (odometer) dos veículos, ajudando a entender quantos carros estão em faixas de uso semelhantes.
💡 Gráfico de Dispersão (Scatter Plot):
Mostra a relação entre o preço e a quilometragem dos veículos, permitindo identificar padrões, tendências e possíveis outliers.
✅ Interatividade via Caixas de Seleção:
O usuário pode escolher facilmente, por meio de checkboxes, qual tipo de gráfico deseja visualizar — histograma, dispersão ou ambos ao mesmo tempo.
🛠️ Tecnologias Utilizadas
Python 3.x
Streamlit
Pandas
Plotly Express
📂 Estrutura do Projeto
project/
│
├── app.py                # Código principal do aplicativo Streamlit
├── vehicles_us.csv       # Conjunto de dados de anúncios de carros
├── README.md             # Documentação do projeto
└── requirements.txt      # Lista de dependências do projeto

▶️ Como Executar o Aplicativo
Certifique-se de ter o Python instalado.
Instale as dependências necessárias (caso ainda não tenha):
pip install streamlit pandas plotly
No terminal, navegue até o diretório do projeto e execute:
streamlit run app.py
O aplicativo abrirá automaticamente no navegado (http://localhost:8501)

📈 Exemplo de Uso
Ao abrir o aplicativo:
Marque a opção “Criar um histograma” para visualizar a distribuição da quilometragem dos veículos.
Marque a opção “Criar um gráfico de dispersão” para ver a relação entre preço e quilometragem.

👨‍💻 Autor
Desenvolvido por Murilo Kono como parte de um exercício prático de criação de dashboards com Streamlit.

Render:
URL do aplicativo no Render (https://sprint-5-project-dash.onrender.com)
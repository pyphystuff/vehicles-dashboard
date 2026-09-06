# Dashboard de Anúncios de Venda de Carros

## Descrição do projeto

Este projeto é um aplicativo web interativo criado com Streamlit para explorar
um conjunto de dados de anúncios de venda de carros nos EUA (`vehicles_us.csv`).
O aplicativo permite ao usuário visualizar rapidamente a distribuição de
quilometragem dos veículos e a relação entre quilometragem e preço, sem
necessidade de escrever código.

## Funcionalidades

- Cabeçalho com a descrição do aplicativo.
- Caixa de seleção para gerar um **histograma** da quilometragem (`odometer`)
  dos veículos anunciados.
- Caixa de seleção para gerar um **gráfico de dispersão** entre quilometragem
  e preço.

## Estrutura do projeto

```
.
├── README.md
├── app.py
├── vehicles_us.csv
├── requirements.txt
├── notebooks
│   └── EDA.ipynb
└── .streamlit
    └── config.toml
```

## Como executar localmente

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Aplicativo implantado

O aplicativo está disponível em: https://<APP_NAME>.onrender.com/

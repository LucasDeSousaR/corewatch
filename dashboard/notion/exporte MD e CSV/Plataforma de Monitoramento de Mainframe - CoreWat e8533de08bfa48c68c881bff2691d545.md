# Plataforma de Monitoramento de Mainframe - CoreWatch

## FATEC Campinas

### Análise e Desenvolvimento de Sistemas

Discente: @Lucas de Sousa Rodrigues 
Orientador: @Nelson H 

# 📄Índice

[Introdução](Plataforma%20de%20Monitoramento%20de%20Mainframe%20-%20CoreWat%20e8533de08bfa48c68c881bff2691d545.md)
[Proposta](Plataforma%20de%20Monitoramento%20de%20Mainframe%20-%20CoreWat%20e8533de08bfa48c68c881bff2691d545.md)
[Viabilidade](Plataforma%20de%20Monitoramento%20de%20Mainframe%20-%20CoreWat%20e8533de08bfa48c68c881bff2691d545.md)
[Cronograma](Plataforma%20de%20Monitoramento%20de%20Mainframe%20-%20CoreWat%20e8533de08bfa48c68c881bff2691d545.md)
[Gráfico de Gantt](Plataforma%20de%20Monitoramento%20de%20Mainframe%20-%20CoreWat%20e8533de08bfa48c68c881bff2691d545.md)
[Bibliografia](Plataforma%20de%20Monitoramento%20de%20Mainframe%20-%20CoreWat%20e8533de08bfa48c68c881bff2691d545.md)

# 📃Documentos

[Termo de Abertura de Projeto](Termo%20de%20Abertura%20de%20Projeto%2012b61454bd2580958b12fe5d44a33c97.md)

[Análise de Requisitos](Ana%CC%81lise%20de%20Requisitos%2013161454bd25804a9115fa73deb203f3.md)

[Caso de Uso do Corewatch](Caso%20de%20Uso%20do%20Corewatch%2015761454bd2580b0ab9ed1ca23179f23.md)

[Diagrama de Classes do CoreWatch](Diagrama%20de%20Classes%20do%20CoreWatch%2015a61454bd258062ab13cec78af4cfdf.md)

[Diagrama de Sequência](Diagrama%20de%20Seque%CC%82ncia%2015a61454bd25803aad75c8ed02946db8.md)

[Diagrama de Estado de Máquina](Diagrama%20de%20Estado%20de%20Ma%CC%81quina%2015a61454bd258067b627cd948cad1da4.md)

[Diagrama Entidade Relacionamento](Diagrama%20Entidade%20Relacionamento%2016c61454bd258015bf38d761408bddb6.md)

# 🛠️Testes

[Teste de Caso de Uso](Teste%20de%20Caso%20de%20Uso%2016861454bd25807ab950cd33d713a207.md)

[Teste de Regressão](Teste%20de%20Regressa%CC%83o%2017961454bd258055aae3e2bd468d951c.md)

[Teste de Integração](Teste%20de%20Integrac%CC%A7a%CC%83o%2017961454bd258037b64fc259742452e9.md)

[TesteDeAceitacao](TesteDeAceitacao%2017961454bd2581f98260f1ced43b29e1.md)

[Teste de Sanidade](Teste%20de%20Sanidade%2017961454bd2580d1a5e1cafc48f63212.md)

# 🛠️Ferramentas

[Jira](https://fatec-campinas-tg-corewatch.atlassian.net/jira/software/projects/SCRUM/boards/1/timeline?shared=&atlOrigin=eyJpIjoiYjAxMTVlNDIyMmZiNGJlNWE4ODYwOTNlYzJkYjNkN2IiLCJwIjoiaiJ9) 

[Lucid](https://lucid.app/documents#/home)

[GitHub](https://github.com/LucasDeSousaR/corewatch)

[Protótipo](Proto%CC%81tipo%2021a61454bd258084a4ece4d4d93ce238.md)

# 📃Apresentação

[Apresentação TG I](Apresentac%CC%A7a%CC%83o%20TG%20I%2022161454bd25808ba5b2f5d1184b0b4d.md)

# 🧠Introdução

**Contextualização**
Desde a sua introdução na década de 1950, os computadores mainframe têm desempenhado um papel fundamental na revolução da tecnologia da informação. Embora muitos acreditem que essas máquinas tenham sido aposentadas pela crescente popularidade dos servidores de pequeno porte e pela proliferação da computação em nuvem, a realidade é que os mainframes continuam a desempenhar um papel vital na atualidade. 

**Justificativa**
Será explorada a importância contínua dos computadores mainframe na atualidade, com base nas informações e conceitos apresentados no livro "Introduction to the New Mainframe: z/OS Basics". Embora muitos possam associar o mainframe a uma era tecnológica anterior, este livro e suas lições essenciais ilustram a relevância duradoura dessa tecnologia nos ambientes empresariais modernos.
Ao analisar os princípios fundamentais do mainframe e do sistema operacional z/OS, bem como suas aplicações práticas, vamos revelar como essas máquinas robustas desempenham um papel crítico na manutenção da infraestrutura tecnológica de muitas organizações. Além disso, exploraremos como a sua capacidade de processamento inigualável, confiabilidade incomparável e escalabilidade contínua fazem dos mainframes uma escolha estratégica em setores críticos, como serviços financeiros, saúde e governo.
Também será abordado como o mainframe não é apenas uma peça de tecnologia do passado, mas uma ferramenta relevante e valiosa na era digital, especialmente no contexto da modernização de aplicativos e integração em ambientes de nuvem híbrida como é mostrado em "Mainframe Application Modernization Patterns for Hybrid Cloud" e "Getting Started Journey to Modernization with IBM Z". Vamos destacar a importância do mainframe como uma tecnologia confiável em um mundo que está em constante evolução. 

**Objetivo**
À medida que avançamos, lembramos que a compreensão dos princípios do mainframe e de seu sistema operacional é essencial para apreciar sua importância contínua e seu impacto duradouro nas operações empresariais. Juntos, exploraremos a relevância do mainframe na atualidade e seu lugar sólido em nosso cenário tecnológico em constante transformação, dentre os principais objetivos, temos:
Demonstrar o funcionamento e a relevância do mainframe na atualidade.
Destacar a importância da modernização no mainframe.
Construir uma plataforma web para exibir informações relacionadas a uma LPAR mainframe, como por exemplo, consumo de CPU (*Central Process Unit*) e uso de MSUs (*MIllion Service Unit*) entre outros parâmetros úteis para monitoração do ambiente.

# 🦾Proposta

Desenvolver uma aplicação web que exiba informações úteis para monitorar o ambiente e a saúde de uma LPAR mainframe. A aplicação utilizará uma API para gerar dados no mainframe, que serão então consumidos e apresentados de maneira intuitiva e coerente para o usuário final.

# 👀Viabilidade

A ideia inicial é aplicar um script JCL no mainframe, disponibilizado pela IBM para ensino e teste chamado [IBM Z Xplore (influitive.com)](https://ibmzxplore.influitive.com/forum/), para extrair dados relativos ao uso e à saúde do ambiente. Esses dados serão inicialmente transformados em formato JSON para serem consumidos pela aplicação web e armazenados em um banco de dados Mongo DB. A aplicação será provavelmente construída utilizando um framework web da biblioteca Python, possivelmente utilizando framework Django.

# ⏲️Cronograma

| Entregas | SET | OUT | NOV | DEZ | JAN | FEV | MAR | ABR | MAI | JUN |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Revisão Bibliográfica | x | x | x | x | x | x | x | x |  |  |
| Estudo de Viabilidade | x | x |  |  |  |  |  |  |  |  |
| Modelagem do sistema |  | x | x | x |  |  |  |  |  |  |
| Modelagem dos teste |  |  |  | x | x | x |  |  |  |  |
| Codificação |  |  |  |  | x | x | x | x | x |  |
| Testes |  |  |  |  |  | x | x | x | x | x |
| Entrega final |  |  |  |  |  |  |  |  |  | x |
| Apresentação |  |  |  |  |  |  |  |  |  | x |

### [Gráfico de Gantt](https://fatec-campinas-tg-corewatch.atlassian.net/jira/software/projects/SCRUM/boards/1/timeline?timeline=MONTHS&shared=&atlOrigin=eyJpIjoiNDkxMWIxZTEzYTE3NDFkN2I2ODllNTgyYzY5MDEzNDEiLCJwIjoiaiJ9)

[Agile Board - Jira](https://fatec-campinas-tg-corewatch.atlassian.net/jira/software/projects/SCRUM/boards/1/timeline?timeline=MONTHS&shared=&atlOrigin=eyJpIjoiNDkxMWIxZTEzYTE3NDFkN2I2ODllNTgyYzY5MDEzNDEiLCJwIjoiaiJ9)

# 📚Bibliografia

AKULA, Ravinder; COUSENS, Matthew; MANNA, Makenzie; MUKHOPADHYAY, Pabitra; SHUKLA, Anad. **Getting Started Journey to Modernization with IBM Z**. Estados Unidos da América: IBM Redbooks, 2021. 72 p.

CHART.JS. *Getting started – Chart.js documentation*. Disponível em: [https://www.chartjs.org/docs/latest/getting-started/](https://www.chartjs.org/docs/latest/getting-started/). Acesso em: 30 maio 2025.

DJANGO SOFTWARE FOUNDATION. *Django documentation (versão 5.2)*. Disponível em: [https://docs.djangoproject.com/en/5.2/](https://docs.djangoproject.com/en/5.2/). Acesso em: 10 maio 2025.

EBBERS, Mike; KETTNER, John; O'BRIEN, Wayne; OGDEN, Bill. **Introduction to the New Mainframe z/OS Basics**. 3. ed. Estados Unidos da América: IBM Redbooks, 2011. 758 p.

IBM. *IBM Z Xplore*. Disponível em: [https://ibmzxplore.influitive.com/](https://ibmzxplore.influitive.com/). Acesso em: 19 set. 2024.

MONGODB INC. *MongoDB Manual*. Disponível em: [https://www.mongodb.com/docs/manual/](https://www.mongodb.com/docs/manual/). Acesso em: 25 abr. 2025.

OPEN MAINFRAME PROJECT. *The Linux Foundation*. 2023. Disponível em: [https://openmainframeproject.org/](https://openmainframeproject.org/). Acesso em: 19 set. 2024.

PARZIALE, Lydia; ADESANYA, Yinka; SOUZA, Elton de; HAUMER, Peter; IRMES, Sandor; PATIL, Amey; LI, Lauren K; LI, Liyong; MIRANDA, Felipe; VARONI, Sidney. **Mainframe Application Modernization Patterns for Hybrid Cloud**. Estados Unidos da América: Ibm Redbooks, 2023. 148 p.
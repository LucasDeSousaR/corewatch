# Análise de Requisitos

[Home](Plataforma%20de%20Monitoramento%20de%20Mainframe%20-%20CoreWat%20e8533de08bfa48c68c881bff2691d545.md)

---

[Requisitos Funcionais](Ana%CC%81lise%20de%20Requisitos%2013161454bd25804a9115fa73deb203f3.md)

[Requisitos Não Funcionais](Ana%CC%81lise%20de%20Requisitos%2013161454bd25804a9115fa73deb203f3.md)

---

# Requisitos *Funcionais*

| **Código** | **Identificação** | **Descrição** |
| --- | --- | --- |
| RF1 | Integrar com API Mainframe | O sistema irá se conectar com a API que extrai os dados do ambiente mainframe, convertendo para um formato compatível (JSON) |
| RF2 | Monitorar recursos | O sistema receberá informações para monitoração em intervalos configuráveis. |
| RF3 | Visualizar dashboard | O sistema deve exibir dashboard com informações gerais da LPAR, como:
CPU (em porcentagem;)
Utilização da memória;
Consumo de MSUs;
Taxas de I/O. |
| RF4 | Configurar alertas | Configurar alertas quando parâmetros ultrapassarem certos limites |
| RF5 | Visualizar histórico | O sistema deve armazenar os dados de monitoramento em um banco de dados para consulta e análise posterior; |
| RF6 | Gerar Relatórios de uso | O sistemas deve gerar relatórios detalhados de uso de recursos da LPAR. |
| RF7 | Configurar intervalo de coleta de dados | O sistema deve permitir o usuário selecionar o intervalo de captura de dados pela API |
| RF8 | Notificar eventos críticos | O sistema deve notificar via mensagem assim que os parâmetros colocados como limite forem alcançados. |
| RF9 | Administrar usuários | O sistema deve permitir o gerenciamento de usuário por meio de um admin. |
| RF10 | Administrar parâmetros globais | O sistema deve permitir que usuário autorizados possam modificar os parâmetros de alerta. |
| RF11 | Manter log de acesso e atividades | O sistema deve guardar um log de acesso e atividades. |
| RF12 | Manter log de atividades relevantes | O sistema deve guardar um log de atividade disruptivas como alteração dos parâmetros globais. |

---

# *Requisitos Não Funcionais*

| **Código** | **Identificação** | **Descrição** |
| --- | --- | --- |
| RNF1 | Segurança | Todas as ações devem estar sujeitas a permissões, com controle de acesso. |
| RNF2 | Desempenho | O sistema deve ser capaz de processar e exibir dados de uso de recursos da LPAR em menos de 2 segundos |
| RNF3 | Escalabilidade | O sistema deve ser capaz de suportar o aumento no número de LPARs monitoradas sem afetar o desempenho. |
| RNF4 | Usabilidade | A interface deve ser intuitiva e fácil de navegar, com informações dispostas de forma clara e organizada. |
| RNF5 | Disponibilidade | O sistema deve estar disponível pelo menos 99% do tempo. |
| RNF6 | Confiabilidade | Os alertas e notificações devem ser confiáveis e acionados com precisão, evitando alertas falsos. |
| RNF7 | Portabilidade | A aplicação deve ser compatível com navegadores modernos;
Deve ser possível hospedar a aplicação em diferentes ambientes de nuvem e infraestrutura, sem mudanças significativas na configuração |
| RNF8 | Manutenibilidade | O sistema deve ser modular e documentado para facilitar futuras modificações, integrações ou manutenção. |
# TesteDeAceitacao

| **ID** | **Descrição do Teste** | **Entradas** | **Critérios de Aceitação** | **Requisitos Relacionados** |
| --- | --- | --- | --- | --- |
| TA01 | Verificar integração com a API do mainframe para coleta de dados. | Configuração válida da API, endpoint e credenciais. | Dados do mainframe são convertidos e armazenados em formato JSON compatível. | RF1, RNF2 |
| TA02 | Monitorar recursos em intervalos configuráveis. | Recurso selecionado e intervalo de 5 minutos configurado. | Sistema atualiza as métricas do recurso monitorado dentro do intervalo configurado. | RF2, RNF4 |
| TA03 | Exibir informações da LPAR no dashboard. | Dados válidos no sistema referentes à CPU, memória e I/O. | Dashboard apresenta os dados em gráficos claros e atualizados em tempo real. | RF3, RNF4 |
| TA04 | Configurar alertas para parâmetros críticos. | Limite configurado para CPU > 80%. | Alerta acionado quando CPU ultrapassa o limite, com notificação por e-mail. | RF4, RF8, RNF6 |
| TA05 | Visualizar histórico de monitoramento. | Período de 7 dias selecionado no filtro. | Histórico exibido corretamente com dados do período solicitado. | RF5, RNF4 |
| TA06 | Gerar relatórios detalhados de uso da LPAR. | Seleção de período e formato (PDF). | Relatório gerado com dados corretos e exportado no formato escolhido. | RF6, RNF8 |
| TA07 | Configurar intervalo de coleta de dados. | Intervalo ajustado para 10 minutos. | Sistema coleta os dados no intervalo configurado e exibe o resultado. | RF7, RNF6 |
| TA08 | Notificar eventos críticos automaticamente. | Evento de uso de memória ultrapassando 90%. | Notificação enviada por SMS com a mensagem detalhada do evento. | RF8, RNF6 |
| TA09 | Gerenciar usuários do sistema como administrador. | Criar novo usuário com permissões padrão. | Usuário criado com sucesso e registrado no banco de dados. | RF9, RNF1 |
| TA10 | Alterar parâmetros globais do sistema. | Configurar limite de alerta de MSUs para 50. | Parâmetro alterado com sucesso e notificação enviada aos administradores. | RF10, RNF6 |
| TA11 | Registrar log de acessos ao sistema. | Acessar e sair do sistema como usuário comum. | Log de acesso contendo o usuário, data e hora é registrado no sistema. | RF11, RNF1, RNF6 |
| TA12 | Registrar log de atividades disruptivas. | Alterar limite global de CPU como administrador. | Log detalhado da atividade é armazenado no sistema com o usuário, data, hora e descrição da alteração. | RF12, RNF6 |
| TA13 | Garantir desempenho no carregamento do dashboard. | Acessar dashboard com 50 LPARs configuradas. | Dados do dashboard carregam em menos de 2 segundos. | RNF2, RNF3 |
| TA14 | Validar escalabilidade com aumento de LPARs monitoradas. | Adicionar 100 LPARs ao sistema. | Sistema continua monitorando todas as LPARs sem degradação perceptível no desempenho. | RNF3 |
| TA15 | Verificar usabilidade da interface do usuário. | Executar todas as funcionalidades principais. | Todas as funcionalidades são acessíveis e compreensíveis, e os dados são exibidos de forma clara e intuitiva. | RNF4 |
| TA16 | Avaliar disponibilidade do sistema. | Realizar acesso em horários aleatórios durante 1 semana. | Sistema está disponível pelo menos 99% do tempo conforme especificado. | RNF5 |
| TA17 | Garantir portabilidade da aplicação em navegadores diferentes. | Acessar a aplicação nos navegadores Chrome, Firefox e Edge. | Aplicação funciona corretamente em todos os navegadores testados. | RNF7 |
| TA18 | Verificar manutenibilidade do sistema. | Realizar uma modificação simples na configuração do código-fonte. | Modificação implementada sem impactar outras funcionalidades, e documentação é suficiente para orientar o processo. | RNF8 |
| TA19 | Validar funcionamento do dashboard em dispositivos móveis. | Acessar o dashboard em um smartphone. | Dashboard ajusta layout e funcionalidades para tela pequena, sem perda de usabilidade. | RNF7, RNF4 |
| TA20 | Garantir precisão das notificações de alertas críticos. | Definir alertas para CPU > 70%. | Alertas são enviados somente quando o limite é ultrapassado, sem falsos positivos. | RF4, RNF6 |
| TA21 | Testar compatibilidade com múltiplos ambientes de nuvem. | Configurar o sistema em AWS e Azure. | Sistema funciona sem erros em ambos os ambientes, com configurações mínimas necessárias. | RNF7 |
| TA22 | Verificar exportação do relatório para diferentes formatos. | Gerar relatório em PDF e Excel. | Relatórios gerados corretamente em ambos os formatos, com conteúdo idêntico e formato adequado. | RF6, RNF8 |
| TA23 | Testar recuperação em caso de falha. | Simular queda do sistema durante o monitoramento. | Sistema retoma a coleta de dados corretamente após ser restaurado. | RNF5 |
| TA24 | Validar tempo de resposta da API com grande volume de dados. | Configuração com 200 LPARs. | API retorna dados em menos de 2 segundos por LPAR. | RNF2, RNF3 |
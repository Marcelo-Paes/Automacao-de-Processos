# Automação de Interface Gráfica com PyAutoGUI

Este aplicativo automatiza interações com a interface gráfica de um sistema, utilizando uma combinação de bibliotecas Python, incluindo `PyAutoGUI`, `Pillow`, `Keyboard`, e `Threading`. Ele é projetado para realizar uma série de ações em um aplicativo ou sistema, como cliques em locais específicos da tela, pressionamento de teclas, e monitoramento de eventos de teclado.

## Funcionalidades

- **Automação de CLIQUES e TECLAS**: O programa é capaz de simular cliques do mouse e pressionamento de teclas em pontos específicos da tela. Isso é feito para automatizar tarefas repetitivas ou que requerem interação com a interface gráfica de um software.
  
- **Detecção de Cores**: Utilizando `Pillow`, o aplicativo captura a tela do sistema e busca por cores específicas para determinar onde o mouse deve clicar. Isso é útil em casos onde a posição dos botões ou elementos da interface é dinâmica e baseada em cores.

- **Monitoramento de Tecla "Esc"**: A biblioteca `Keyboard` permite monitorar se a tecla "Esc" foi pressionada. Caso o usuário deseje interromper a automação a qualquer momento, ele pode pressionar a tecla "Esc", e o programa irá parar imediatamente.

- **Execução Simultânea**: Utilizando o módulo `Threading`, o programa pode monitorar a tecla "Esc" enquanto a automação está em andamento, sem bloquear a execução das outras ações.

- **Controle de Tempo**: O `time.sleep()` é utilizado para adicionar pausas entre as ações, garantindo que as interações com a interface gráfica ocorram de forma natural e com tempo suficiente para o sistema responder.

## Tecnologias Utilizadas

- **PyAutoGUI**: Para automatizar cliques, movimentos de mouse e pressionamento de teclas.
- **Pillow (PIL)**: Para capturar imagens da tela e analisar pixels em busca de cores específicas.
- **Keyboard**: Para monitorar eventos de teclas pressionadas, permitindo ao usuário interromper a automação.
- **Threading**: Para executar tarefas paralelas, como monitorar a tecla "Esc", enquanto o código principal realiza a automação.
- **Time**: Para adicionar pausas entre as ações, controlando o tempo entre os eventos simulados.

## Como Funciona

1. **Início da Automação**: O programa começa a execução com uma série de ações predefinidas, como clicar em posições específicas, pressionar teclas de atalho, etc.
2. **Monitoramento da Tela**: O código captura a tela e verifica se as cores definidas estão presentes em áreas específicas.
3. **Interrupção da Automação**: A qualquer momento, o usuário pode pressionar "Esc" para interromper o processo.
4. **Execução de Ações de Navegação**: O programa navega pelo sistema, realizando cliques e pressionando teclas, até concluir o ciclo de automação.

## Uso

1. Execute o script Python para iniciar a automação.
2. A automação começará automaticamente após uma pequena pausa.
3. Se desejar interromper a execução, pressione a tecla **Esc**.
4. O processo continuará até o término das tarefas programadas.

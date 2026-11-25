# Auditoria comparativa — 25/11/2026

## Antes (inspeção textual do site público)
Fonte: https://dracarolinadamasceno.com/consultorio-pediatra/
- 2 H1 na extração; título Sobre repetido; chamadas de agendamento repetidas; apresentação profissional ao fim da página; questionário antes dos serviços.
- 6 serviços, 7 questões, consulta particular presencial/online, informações de contato, mapa e Instagram identificados. E-book verificado em https://dracarolinadamasceno.com/sono-infantil/.
- Sem acesso a HTML/CSS bruto por HTTP no ambiente, sem navegador no site original; contraste computado, desempenho, posição de CTA e pontuação Chicote não medidos.

## Depois (Chromium local, rede externa bloqueada)
| Medida | Antes | Depois |
|---|---|---|
| H1 | 2 na extração | 1 |
| Título sobre duplicado | Sim | Não |
| CTA principal totalmente visível 360×640 | Não medido | Sim, y=371–423 |
| CTA principal totalmente visível 390×844 | Não medido | Sim, y=378–430 |
| CTA principal totalmente visível 1440×900 | Não medido | Sim, y=567–619 |
| Altura CTA principal | Não medido | 52px nas três resoluções |
| Overflow horizontal | Não medido | Zero nas três resoluções |
| Âncoras internas inválidas | Não medido | Zero |
| Elementos img com alt | Não medido | 19/19 |
| Menu mobile abre e fecha por Escape | Não medido | Sim |
| Questionário | 7 itens identificados | 7 itens, contagem atualizada |
| Mapa | Embed identificado | Criação do iframe sob demanda OK; rede não testada |
| Erros JS em execução | Não medido | Zero nos fluxos testados |
| LCP, CLS, peso real, contraste automatizado, acessibilidade integral | Não medido | Não medido |
| Chicote 70+30 | Não medido | Não medido |

Método: HTML, CSS e JS inseridos em Chromium por Playwright (navegação file/localhost bloqueada), viewport 360×640, 390×844 e 1440×900. Imagens/fontes remotas bloqueadas. Não representa renderização com assets reais, nem teste 4G/CPU. Não foram testados cliques externos, carregamento do mapa, fonte remota nem entrega WordPress.

## Pendências
1. Baixar imagens e testar os 18 URLs distintos; converter para WebP com o script fornecido. Se alguma imagem falhar, solicitar arquivo ao titular.
2. Validar a identidade com o arquivo original da mascote; validar texto médico e registros antes da publicação. Não foi incluída regra rígida de febre baseada em tempo/temperatura do site anterior, por segurança clínica.
3. Executar Chicote oficial antes e depois, gerar rubrica com evidência, revisar capturas e corrigir os pontos reais. Sem nota estimada.
4. Validar links externos e navegação com teclado/leitor de tela e verificar a implementação na hospedagem após aprovação.

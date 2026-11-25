# Dra. Carolina Damasceno — prévia de prospecção

HTML, CSS e JavaScript sem build. Abra `index.html` em um navegador com internet ou execute `python -m http.server 8080` nesta pasta e abra http://localhost:8080. Não é o site oficial; a prévia inclui `noindex,nofollow`.

As imagens originais estão referenciadas por URL. O ambiente de criação não tinha acesso direto à rede para baixá-las. Para torná-las locais e otimizar em WebP, instale Pillow (`python -m pip install Pillow`) e execute `python preparar-imagens.py`. O script mantém um inventário das fontes e só substitui as URLs cujo download e conversão foram bem-sucedidos.

Publicação: faça upload dos arquivos para um repositório ou para a pasta `dracarolinadamasceno` em previa.taisgb.com.br, após revisão e aprovação. Não houve publicação nem alteração no WordPress oficial.

## Auditoria oficial Chicote (PowerShell)

Com o repositório Chicote instalado em `D:\_para_teste\chicote` e o servidor local acima aberto, execute em outro terminal:

```powershell
cd D:\_para_teste\chicote
node scripts/chicotada.mjs https://dracarolinadamasceno.com/consultorio-pediatra/ --publico geral --saida ./auditorias/carolina-antes
node scripts/chicotada.mjs http://localhost:8080/ --publico geral --saida ./auditorias/carolina-depois
```

Compare os relatórios e prints em 360×640, 390×844 e 1440×900. A nota oficial não foi calculada neste ambiente. `chicote/resultado-local.json` contém testes de layout e interações em Chromium, com CSS/JS inseridos diretamente e rede externa bloqueada, não uma execução da chicotada original. O script local requer Python, Playwright e Chromium (`pip install playwright`); o caminho do executável no arquivo deve ser ajustado para o seu sistema.

# Ronaldinho Soccer - Relatório do projeto - Equipe 9

Relatório de desenvolvimento do jogo Ronaldinho Soccer feito para a disciplina de Introdução a Programação do curso de Engenharia da Computação do CIn/UFPE.

## Índice
- [1. Equipe](#equipe)
    - [1.1 Desenvolvido por](#equipe)
    - [1.2 Divisão de tarefas](#divisao)
- [2. Ideação e Design](#ideacao)
- [3. Bibliotecas Utilizadas](#bibliotecas)
- [4. Organização do código](#organizacao)
- [5. Conceitos aprendidos na disciplina](#conceitos)
- [6. Desafios enfrentados](#desafios)
- [7. Capturas de tela](#capturas)
- [8. Como instalar](#como-instalar)

<a id="equipe"></a>
## Equipe

### Desenvolvido por

<table>
  <tr>
<td align="center"><a href="https://www.linkedin.com/in/iamichelly/"><img src="https://i.imgur.com/77ixAeU.jpeg" width="100px;" alt=""/><br /><sub><b>Michelly Silva</b></sub></a><br/></td>

<td align="center"><a href="https://www.linkedin.com/in/thalesvgfraga/"><img src="https://i.imgur.com/K39AuNm.jpeg" width="100px;" alt=""/><br /><sub><b>Thales Fraga</b></sub></a><br/></td>

<td align="center"><a href="https://www.linkedin.com/"><img src="https://i.imgur.com/uOYWpTS.png" width="100px;" alt=""/><br /><sub><b></b></sub>Lucas Brito</a><br/></td>

<td align="center"><a href="https://www.linkedin.com/"><img src="https://i.imgur.com/46Xw3u3.png" width="100px;" alt=""/><br /><sub><b></b></sub>Marcus Antônio</a><br/></td>
</tr>
 </table>

<a id="divisao"></a>
### Divisão de tarefas
- <strong>Michelly Silva</strong>: Criação e implementação dos assets de imagem, correção de bugs, realização de melhorias
- <strong>Thales Fraga</strong>: Implementação dos coletáveis, correção de bugs e realização de melhorias
- <strong>Lucas Brito</strong>: Criação e implementação dos assets sonoros, correção de bugs e realização de melhorias
- <strong>Marcus Antônio</strong>: Criação do jogador e adversários e mecânica básica do jogo, correção de bugs e realização de melhorias

<a id="ideacao"></a>
## Ideação e design

O processo de ideação e design em grupo para o nosso projeto de jogo teve início com um brainstorm escrito no [whimsical](https://whimsical.com/projeto-ip-brainstoming-23fNbDga6oa6N2Xy1pBtRL) seguido por uma votação baseada em critérios pré-definidos. O tema mais votado foi eleito como nossa ideia de jogo. Abaixo, descreveremos em detalhes as etapas desse processo.

<strong>1. Brainwriting Colaborativo</strong>

Para gerar ideias e conceitos inovadores para o jogo, utilizamos uma técnica chamada "brainwriting". Cada membro da equipe recebeu um bloco de anotações virtual e teve 3 minutos para registrar suas ideias sobre o jogo. Após esse tempo, o membro do grupo passava para o bloco à direita, adicionando suas contribuições por mais 3 minutos. Esse processo continuou até que todos os membros tivessem a oportunidade de participar.

<strong>2. Votação para seleção do tema</strong>

Após a geração de um grande número de ideias durante o processo de brainwriting, realizamos uma votação para escolher o tema que fosse instigante, inovador, esteticamente agradável e de fácil desenvolvimento. Após uma análise criteriosa, o tema escolhido foi: "tiro ao alvo com obstáculos móveis, em que cada rodada pode incluir um dardo premium (prata, ouro ou diamante) que vale mais pontos". Esse tema oferecia desafios específicos e uma experiência de jogo que atendia aos critérios estabelecidos.

<a id="bibliotecas"></a>
## Bibliotecas Utilizadas
- [ PyGame ]( https://www.pygame.org/news ): É a principal biblioteca utilizada no projeto. Usada majoritariamente para montar as cenas e mecânicas do jogo.
- [ Random ]( https://docs.python.org/pt-br/3/library/random.html ): Usada para randomizar spawn de coletáveis e movimentos dos adversáriobs e deixar o jogo mais dinâmico.
- [ Math ]( https://docs.python.org/pt-br/3/library/math.html ): Usada para facilitar cálculos matemáticos com funções como seno e cosseno.


<a id="organizacao"></a>
## Organização do código

### main.py

Esse arquivo possui o loop principal do jogo. Além disso, é nele que configuramos e utilizamos as outras classes existentes no projeto.

### jogador.py

Esse arquivo contém a classe Jogador, responsável por desenhar e controlar as ações do player

### adversario.py

Esse arquivo contém a classe Adversario, responsável por desenhar e controlar as ações dos adversários

### gol.py

Esse arquivo contém a classe Gol, responsável por desenhar e gerenciar as colisões do gol

### coletavel.py

Esse arquivo contém a classe Coletavel, responsável por desenhar e gerenciar as colisões dos coletáveis

### bola.py

Esse arquivo contém a classe Bola, responsável por desenhar e controlar o movimento da bola quando chutada

### audio.py

Esse arquivo contém as configurações referentes a audio e efeitos sonoros

### constantes.py

Esse arquivo contém constantes usadas para definir padrões no jogo, usadas em todos os arquivos

### utils.py

Esse arquivo contém funções uteis que podem ser compartilhadas por todos os arquivos


<a id="conceitos"></a>
## Conceitos aprendidos na disciplina
- <strong>Funções</strong>: De longe esse foi o conceito aprendido na disciplina que foi mais utilizado durante o desenvolvimento do jogo, sendo usada para quase todas as mecânicas e elementos essenciais, geração de inimigos/coletáveis e telas de menu. Possibilitou o reuso e a organização do código.
- <strong>Loop</strong>: Conceito essencial para o desenvolvimento de jogos, pois esse tipo de mídia se baseia em um grande loop para execução e processamento de inputs. 
- <strong>Orientação a objetos</strong>: Outro conceito aprendido na disciplina e amplamente utilizado no projeto, que permitiu uma maior organização, reuso e legibilidade do código graças às diversas classes mencionadas anteriormente.
- <strong>Listas</strong>: Muito utilizada para lidar com posições, realizar cálculos matemáticos e gerenciar itens na tela.
- <strong>Condicionais</strong>: Estruturas condicionais são fundamentais em um jogo, pois várias funcionalidades possuem pré-requisitos. Por exemplo, checar se deve começar o jogo, se dois objetos colidiram, etc.

<a id="desafios"></a>
## Desafios enfrentados

Desde o começo esse foi um projeto desafiador por se tratar de um sistema interativo baseado na biblioteca PyGame, biblioteca que apenas um integrante da equipe conhecia. Foi necessário estudo para iniciar o desenvolvimento. Também foi um desafio o uso do git para o trabalho em equipe, sendo necessário para gerenciar cada adição com o time remotamente. A criação de assets também foi um bom desafio.

<a id="capturas"></a>
## Capturas de tela

Tela Inicial | Tela de Jogo
:-------------------------:|:-------------------------:
<img src="https://i.imgur.com/1P978sw.png" alt="Tela Inicial" height="240"> | <img src="https://i.imgur.com/aRhFCqN.png" alt="Tela de Jogo" height="240"> 

Game Over | Tela de Vitória
:-------------------------:|:-------------------------:
<img src="https://i.imgur.com/L4gQ6cJ.png" alt="Jogador sem vida" height="240"> | <img src="https://i.imgur.com/iBAeDK4.png" alt="Jogador em rodada avançada" height="240">

<a id="como-instalar"></a>
## Como instalar
### Certifique-se de ter Python3 e PyGame instalados em seu computador

### Abra o terminal do seu sistema em uma pasta à sua escolha, copie e cole o seguinte comando:

#### Se você usa Windows, execute esse comando:
```
#Clone esse repositório
git clone https://github.com/ditthales/ip-game.git
#Entre na pasta do projeto
cd ip-game
#Execute o arquivo 'main.py'
py main.py
```
#### Se você usa MacOS ou Linux, execute esse comando:
```
#Clone esse repositório
git clone https://github.com/ditthales/ip-game.git
#Entre na pasta do projeto
cd ip-game
#Execute o arquivo 'main.py'
python3 main.py
```
 Ou apenas baixe o arquivo .zip, extraia em algum lugar da sua escolha e execute o arquivo 'main.py'.

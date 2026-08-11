# 🔁 Anki — Setup do zero

> Guia do **Módulo 0**. Se você nunca usou Anki, siga na ordem. Leva ~30 minutos.
> Ao final você tem os 2 decks criados, 104 cards importados e a rotina rodando.

---

## 1. O que o Anki é — e o que ele não é

**Anki não ensina nada.** Ele resolve um problema só: **impedir que você esqueça**
o que já aprendeu em outro lugar.

```
Aula / leitura / erro corrigido  →  você ENTENDE
                Anki             →  você NÃO ESQUECE
```

Consequência prática: **nunca crie um card sobre algo que você ainda não entendeu.**
Card de conteúdo não compreendido vira decoreba sem transferência — você acerta no
Anki e continua errando ao escrever.

Ele funciona por **repetição espaçada**: mostra o card pouco antes de você esquecer.
Acertou fácil? Volta daqui a 3 dias, depois 9, depois 25… Errou? Volta amanhã.
Por isso 20 minutos por dia sustentam milhares de cards.

---

## 2. Instalação

### 2.1 Desktop — obrigatório

O desktop é onde você **cria e edita** cards. É gratuito e open source.

1. Baixe em **[apps.ankiweb.net](https://apps.ankiweb.net)** (Windows/Mac/Linux)
2. Instale e abra
3. `Tools → Preferences → Language` → deixe em **English**
   *(Regra do Módulo 0: tudo em inglês. Vale para o Anki também.)*

### 2.2 Conta AnkiWeb — faça agora, não depois

Sem conta, você perde tudo se o PC morrer, e não sincroniza com o celular.

1. Crie em **[ankiweb.net](https://ankiweb.net)**
2. No desktop: clique em **Sync** (canto superior direito) e faça login
3. Sincronize **no fim de toda sessão**. Vira parte do ritual de fechamento.

### 2.3 Celular — onde você de fato vai revisar

| Sistema | App | Custo |
|---------|-----|-------|
| **Android** | AnkiDroid (Play Store / F-Droid) | Grátis |
| **iPhone** | AnkiMobile | ~US$ 25, pago uma vez |
| **Qualquer um** | [ankiweb.net](https://ankiweb.net) pelo navegador | Grátis, mas limitado |

> 💰 No iPhone, o app é a única parte paga do ecossistema — ela financia o
> desenvolvimento de todo o resto. Se não quiser pagar agora, use o AnkiWeb pelo
> navegador do celular: funciona para revisar, só é mais lento e não funciona offline.

O celular é o que salva a rotina: fila do mercado, café, 5 minutos entre reuniões.

---

## 3. Criar os 2 decks

Deck = coleção de cards. O Módulo 0 pede dois — **não crie mais que isso agora**.

No desktop: **`Create Deck`** (rodapé) → digite o nome → OK.

| Deck | O que vai nele |
|------|----------------|
| `English::Vocabulary` | Palavras e expressões que você encontrou lendo/ouvindo |
| `English::Grammar Patterns` | Estruturas — os cards das aulas do [modules/](../modules/) |

> 💡 O `::` cria **subdecks**. `English::Vocabulary` fica aninhado dentro de `English`,
> e você pode estudar tudo de uma vez clicando no deck pai.

---

## 4. Importar os 104 cards do Módulo 1A

Este repositório já gera um baralho pronto a partir das seções *"Cards pro Anki"* das aulas.

1. Baixe o arquivo **[`1A-fundacao-gramatical.tsv`](1A-fundacao-gramatical.tsv)**
   *(no GitHub: abra o arquivo → botão **Download raw file**)*
2. No Anki: **`File → Import`**
3. Selecione o `.tsv`
4. **Confira a tela de importação.** O arquivo já traz as instruções embutidas, então
   deve aparecer sozinho:

   | Campo | Valor esperado |
   |-------|----------------|
   | Notetype | `Basic` |
   | Deck | `English::Grammar Patterns` |
   | Field 1 | Front |
   | Field 2 | Back |
   | Field 3 | Tags |

5. **`Import`**

Os cards vêm com tag por aula (`1A::04-articles`), então você pode filtrar, suspender
ou revisar só uma aula específica pelo **Browse**.

> ⚠️ **Não importe os 104 de uma vez e saia estudando.** Eles entram na fila de
> "novos" e o Anki vai te dar só a quantidade configurada por dia (próxima seção).
> Isso é proposital.

**Regerar o arquivo** depois de editar alguma aula:

```bash
python scripts/build_anki_deck.py
```

---

## 5. Configuração — as 6 opções que importam

Clique na engrenagem ⚙️ ao lado do deck → **`Options`**.

| Opção | Onde | Valor | Por quê |
|-------|------|-------|---------|
| **New cards/day** | Daily Limits | **5** *(sim, cinco)* | Ver a matemática abaixo |
| **Maximum reviews/day** | Daily Limits | **9999** | Se limitar, o backlog se esconde e vira bola de neve |
| **FSRS** | FSRS | **ligado** | Algoritmo moderno, agenda melhor que o antigo |
| **Desired retention** | FSRS | **0.90** | Não mexa. Subir para 0.95 dobra sua carga diária. |
| **Leech threshold** | Lapses | **4** | Card errado 4x é card ruim — quero saber cedo |
| **Leech action** | Lapses | **Tag Only** | Marca em vez de sumir com ele silenciosamente |

> Se alguma opção estiver com nome ou lugar diferente, é versão do Anki. Procure pelo
> nome dela na busca das opções — os conceitos não mudaram.

### 🔴 A matemática que ninguém conta

Cada card novo gera **cerca de 10 revisões** ao longo do tempo. No regime estável:

| Cards novos/dia | Revisões/dia | Tempo real/dia |
|-----------------|--------------|----------------|
| **5** | ~50 | ~8 min |
| **10** | ~100 | ~15–20 min |
| **20** | ~200 | **~35 min** |

O [README](../README.md) fala em *20 cards novos/dia* e *20 min/dia* — **os dois números
não cabem juntos**. 20 min/dia sustenta confortavelmente ~10 cards novos/dia. Para
manter 20 novos/dia você precisa de 35 min/dia, todos os dias, para sempre.

**A escalada segura:**

| Quando | New cards/day |
|--------|---------------|
| Semanas 1–2 | **5** |
| Semanas 3–4 | **10** — só se você não perdeu nenhum dia |
| Depois | **15–20** — só se aceitar expandir o bloco para 30–35 min |

> A causa nº 1 de abandono do Anki é começar com 20+ e afundar na 3ª semana, quando as
> revisões acumuladas explodem. Você não sente o custo no dia 1 — sente no dia 18.

---

## 6. Os 2 tipos de card que você vai usar

**`Add`** (rodapé) → escolha o **Type** no topo da janela.

### Basic — frente e verso

Use para **vocabulário e blocos fixos**. Direção **PT → EN**, porque seu objetivo é
**produzir**, não reconhecer.

```
Front:  Obrigado pelo feedback.
Back:   Thanks for the feedback.
        ⚠️ "feedback" é incontável — nunca "feedbacks"
```

### Cloze — lacuna dentro da frase

Use para **gramática e collocations**. É o formato mais eficiente que existe.

1. Type: **Cloze**
2. Escreva a frase inteira
3. Selecione a parte que quer esconder → **`Ctrl+Shift+C`**

```
Text:   I've been working here {{c1::since}} 2020.
Extra:  since + ponto no tempo · for + duração
```

Uma frase pode ter várias lacunas (`c1`, `c2`, `c3`) — o Anki cria um card para cada.

---

## 7. Como fazer um card que funciona

| ✅ Faça | ❌ Não faça |
|---------|------------|
| Um fato por card | Card com 3 regras juntas |
| Frase completa, real, que você encontrou | Palavra solta |
| Contexto do **seu** trabalho | Exemplo genérico de livro |
| Direção PT → EN (produção) | Só EN → PT (reconhecimento) |
| Criar depois de entender | Criar para "aprender depois" |
| Deletar card ruim sem dó | Insistir num card que você erra sempre |

**O teste do card bom:** você consegue responder em **menos de 10 segundos**, e a
resposta é **uma coisa só**.

```
❌ Front: phrasal verbs com "get"
   → resposta é uma lista de 15 itens. Card impossível.

✅ Front: Eu me dou bem com meu time. → I ____ my team.
   Back:  get along with
```

### De onde vêm seus cards

| Fonte | Vira card quando |
|-------|------------------|
| [`error-log.md`](../error-log.md) | O erro apareceu **3x** → seção Reincidentes |
| [`modules/`](../modules/) | Seção "Cards pro Anki" de cada aula (já importado) |
| Leitura / listening | Você travou numa palavra e ela apareceu 2x |
| Correção recebida | Alguém corrigiu você e você não sabia a regra |

> 🎯 A fonte mais valiosa é o **error-log**. Card feito do seu próprio erro tem
> retenção muito maior que card de lista pronta — porque já tem uma memória de
> fracasso ancorada nele.

---

## 8. A rotina diária

No [STUDY-GUIDE](../STUDY-GUIDE.md#2-o-dia--45-minutos), Anki é o **primeiro bloco**,
15 min. A ordem interna importa:

```
1. Revisões pendentes   ← SEMPRE primeiro, sem exceção
2. Cards novos          ← só se sobrou tempo
3. Sync                 ← fecha a sessão
```

> **Se o tempo acabar, corte os cards novos, nunca as revisões.** Revisão atrasada
> apodrece — o card cai da curva e você perde o investimento já feito. Card novo
> não introduzido hoje simplesmente entra amanhã, sem custo nenhum.

### Os 4 botões — use com honestidade

| Botão | Quando | Frequência saudável |
|-------|--------|---------------------|
| **Again** | Errou, ou levou +10s para lembrar | ~10–15% |
| **Hard** | Acertou, mas foi sofrido | ~10% |
| **Good** | Acertou normalmente | **~70%** ← o padrão |
| **Easy** | Instantâneo, óbvio, quase irritante | ~5% |

**Os dois abusos clássicos:**

- **Abusar de `Hard`** achando que "reforça": não reforça. Ele encurta os intervalos e
  você acaba revisando o mesmo card infinitas vezes.
- **Abusar de `Easy`**: joga o card para daqui a meses. Você vai esquecer, e o Anki
  perde a calibragem.

> **Regra:** hesitou mais de ~10 segundos? Foi `Again`. Recuperação lenta não é
> recuperação — em conversa você não tem 10 segundos.

### Leeches — cards que você erra sempre

Errou 4x (pelo que configuramos) → o Anki marca com a tag `leech`.

**Isso não é falha sua, é card ruim.** Vá em **Browse** → filtre por `tag:leech` e:

1. **Reescreva** com mais contexto, ou quebre em 2 cards menores, ou
2. **Delete.** Sem cerimônia. Um card deletado custa zero; um leech custa toda semana.

---

## 9. Erros de iniciante que matam o hábito

| 🚫 Erro | Consequência |
|---------|--------------|
| Começar com 20+ cards novos/dia | Afunda na semana 3 e abandona |
| Instalar 10 add-ons na primeira semana | Quebra, trava, você culpa o Anki |
| Baixar deck pronto de 5.000 palavras | 90% é irrelevante para você. Card alheio não gruda. |
| Card com resposta longa | Você não sabe se acertou. Impossível de julgar. |
| Pular dias e "recuperar no domingo" | 400 revisões acumuladas = desistência |
| Criar card do que não entendeu | Decora a resposta, continua errando na escrita |
| Não sincronizar | Perde tudo, do nada |

> **Add-ons: zero no primeiro mês.** O Anki nativo faz tudo que você precisa agora.
> Depois de 30 dias de rotina estável, aí vale explorar.

### Backlog: o que fazer se você sumir uma semana

Não tente zerar num dia. Vá em **Deck Options → Daily Limits → Maximum reviews/day**,
coloque um teto (ex. 60) e mantenha por alguns dias até drenar. E **zere os cards novos**
até o backlog acabar.

---

## 10. Sua primeira semana

| Dia | O que fazer |
|-----|-------------|
| **1** | Instalar desktop + conta AnkiWeb + app no celular. Criar os 2 decks. |
| **1** | Importar o `.tsv` do 1A. Configurar as 6 opções da seção 5. |
| **1** | Fazer os 5 primeiros cards. Sync. |
| **2–7** | Revisões primeiro, 5 novos, sync. **Todo dia.** |
| **7** | Conferir: você perdeu algum dia? Se não, suba para 10 na semana 2. |

**Meta da semana 1: sete dias seguidos.** Não é a quantidade de cards. É a corrente.

---

## 11. Atalhos que economizam tempo

| Tecla | Ação |
|-------|------|
| `Espaço` | Mostrar resposta / `Good` |
| `1` `2` `3` `4` | Again · Hard · Good · Easy |
| `A` | Adicionar card (na tela principal) |
| `E` | Editar o card atual durante a revisão |
| `Ctrl+Shift+C` | Criar lacuna cloze |
| `*` | Marcar card (para revisar depois) |
| `@` | Suspender card |
| `Y` | Sincronizar |
| `B` | Abrir o Browse |

---

## ✅ Critério de conclusão — Módulo 0

Marque os checkboxes do [README](../README.md) quando:

- [ ] Anki desktop instalado, em inglês, logado no AnkiWeb
- [ ] App no celular sincronizando com o desktop
- [ ] Decks `English::Vocabulary` e `English::Grammar Patterns` criados
- [ ] 104 cards do 1A importados com as tags certas
- [ ] As 6 opções da seção 5 configuradas (new/day = **5**)
- [ ] **7 dias seguidos** de revisão completa, sem pular

O último item é o único que importa de verdade. Os outros levam 30 minutos.

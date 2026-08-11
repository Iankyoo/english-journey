# 09 — Formação de perguntas e question tags

> Perguntar é 50% de uma reunião em inglês. E a ordem das palavras numa pergunta é
> **rígida** — *"Where you are?"* não é sotaque, é erro que trava o entendimento.

**Módulo:** 1A · **Sessões:** 2 · **Anterior:** [08 — Preposições](../08-prepositions/) · **Próxima:** [10 — Modais básicos](../10-basic-modals/)

---

## 1. A ideia em uma frase

Pergunta em inglês tem uma fórmula fixa: **(Wh-) + auxiliar + sujeito + verbo**.

---

## 2. Forma

### A fórmula — `ASI` (Auxiliar antes do Sujeito, Inversão)

```
(Wh-)      +   AUX    +  SUJEITO  +  VERBO   +  resto?
                Do        you        know      the answer?
 What        does         it         mean?
 Where        are         you?
 Why         didn't       he         reply?
 When        will         we         deploy?
```

### Yes/No — começa pelo auxiliar

| Tempo | Exemplo |
|-------|---------|
| Present Simple | **Do** you use Docker? · **Does** it work? |
| Past Simple | **Did** you deploy it? |
| `to be` | **Are** you available? · **Was** it broken? |
| Continuous | **Is** he working on it? |
| Modal | **Can** you review this? · **Should** we roll back? |

> ⚠️ `to be` e modais **são** o auxiliar — não levam `do`.
> *~~Do you can help?~~* → **Can you help?** · *~~Do you are ready?~~* → **Are you ready?**

### Wh- questions

| Palavra | Pergunta por | Exemplo |
|---------|--------------|---------|
| **What** | coisa | What **does** this function **do**? |
| **Who** | pessoa | Who **broke** the build? |
| **Where** | lugar | Where **are** the logs? |
| **When** | tempo | When **did** you merge it? |
| **Why** | motivo | Why **is** it failing? |
| **How** | modo | How **does** caching **work** here? |
| **Which** | escolha limitada | Which branch **should** I use? |
| **Whose** | posse | Whose PR **is** this? |
| **How much / many** | quantidade | How many tests **failed**? |
| **How long** | duração | How long **will** it **take**? |

### 🔑 A exceção: perguntas de sujeito — **sem auxiliar**

Quando `who` ou `what` **é o sujeito** da frase, a ordem não muda e **não entra `do/did`**:

| Pergunta de **sujeito** (sem aux) | Pergunta de **objeto** (com aux) |
|-----------------------------------|----------------------------------|
| **Who broke** the build? | Who **did** you **ask**? |
| **What caused** the outage? | What **did** it **cause**? |
| **Who is** working on this? | Who **are** you working with? |
| **What happened**? | What **did** you **do**? |

> **Como saber:** se a resposta é o *sujeito* ("John broke it"), não use auxiliar.
> *~~Who did break the build?~~* ❌ → **Who broke the build?** ✅

### Perguntas embutidas — a ordem **volta ao normal**

Depois de `Do you know…`, `Could you tell me…`, `I wonder…`, a pergunta interna
**perde a inversão**:

| ❌ Pergunta direta dentro | ✅ Ordem normal |
|---------------------------|-----------------|
| *Do you know where **is** the file?* | Do you know where the file **is**? |
| *Could you tell me what **does** it **mean**?* | Could you tell me what it **means**? |
| *I don't know why **did** he **leave**.* | I don't know why he **left**. |

> 🎯 Este é um marcador forte de nível. Acertar embutidas soa B2; errar soa A2.

### Question tags

Confirmação no fim da frase. Regra: **frase positiva → tag negativa** e vice-versa.
O tag repete o **auxiliar** da frase.

| Frase | Tag |
|-------|-----|
| The build is broken, | **isn't it?** |
| The build isn't broken, | **is it?** |
| You deployed it, | **didn't you?** |
| You don't use Windows, | **do you?** |
| We can merge this, | **can't we?** |
| She'll review it, | **won't she?** |
| I'm late, | **aren't I?** *(irregular)* |
| Let's start, | **shall we?** *(fixo)* |

Se a frase não tem auxiliar, o tag usa `do/does/did`:
*You work here, **don't you?*** · *He left, **didn't he?***

---

## 3. Uso — perguntas que você vai usar toda semana

```
Sorry, could you repeat that?
Could you say that again, please?
Just to make sure I got it right — you mean X, right?
Does that make sense?
What's the priority on this?
Do you have any context on this ticket?
Who's the owner of this service?
When do you need this by?
Would it be possible to move the deadline?
Can I get your take on this?
What happened with the deploy?          ← pergunta de sujeito, sem "did"
```

> 💡 Decore estas como **blocos prontos**. Numa reunião você não tem 3 segundos para
> montar a estrutura — você precisa dela pronta.

---

## 4. 🇧🇷 Erros de brasileiro

| ❌ | ✅ | Por quê |
|----|----|---------|
| *Where you are?* | Where **are you**? | Falta inversão |
| *What means this?* | What **does this mean**? | Falta auxiliar |
| *You know what is it?* | Do you know what **it is**? | Embutida volta à ordem normal |
| *Do you can help me?* | **Can** you help me? | Modal já é o auxiliar |
| *Do you are ready?* | **Are** you ready? | `to be` já é o auxiliar |
| *Who did break the build?* | Who **broke** the build? | Pergunta de sujeito não leva `did` |
| *Did you went there?* | Did you **go** there? | Infinitivo após `did` |
| *How much costs?* | How much **does it cost**? | Sujeito obrigatório + auxiliar |
| *The build is broken, no?* | …, **isn't it**? | Tag precisa do auxiliar |
| *You like it, isn't it?* | You like it, **don't you**? | Tag repete o auxiliar certo |

---

## 5. ✍️ Prática

**A. Transforme em pergunta (10).**
1. Você usa Docker? *(present simple)*
2. Onde estão os logs?
3. O que essa função faz?
4. Quem quebrou o build?
5. Quem você perguntou?
6. Por que o deploy falhou?
7. Você pode revisar meu PR?
8. Quanto tempo isso vai levar?
9. Você sabe onde está o arquivo de configuração? *(embutida)*
10. Você poderia me dizer o que isso significa? *(embutida)*

**B. Adicione o question tag correto (6).**
1. The tests are passing, ___?
2. You didn't merge it yet, ___?
3. We can deploy tomorrow, ___?
4. She works on the platform team, ___?
5. It wasn't intentional, ___?
6. Let's schedule a call, ___?

**C. Escreva 8 perguntas que você faria de verdade** — 4 numa daily, 4 num code review.
Leia em voz alta cronometrando: cada uma deve sair em menos de 3 segundos.

---

## 6. ✅ Critério de conclusão

- [ ] Acertar 9+ das 10 do exercício A
- [ ] Acertar 5+ dos 6 tags do exercício B
- [ ] Distinguir pergunta de sujeito de pergunta de objeto em 5 pares, sem consultar
- [ ] Escrever 5 perguntas embutidas **sem inverter** a parte interna
- [ ] Produzir 10 perguntas faladas em 30 segundos, sem travar na ordem das palavras

**Teste final:** grave-se fazendo 10 perguntas seguidas sobre um projeto. Transcreva.
Toda inversão errada vai para o [error-log.md](../../../error-log.md) na categoria `word-order`.

---

## 7. 🔁 Cards pro Anki

```
Onde você está? → Where ____?                             | are you
O que isso significa? → What ____ this ____?              | does / mean
Quem quebrou o build? → Who ____ the build?               | broke (sem "did")
Você sabe onde está o arquivo? → Do you know where ____?  | the file is
Você pode ajudar? → ____ you help?                        | Can (sem "do")
O build está quebrado, não está? → The build is broken, ____? | isn't it
Você não usa Windows, usa? → You don't use Windows, ____? | do you
Vamos começar, vamos? → Let's start, ____?                | shall we
Quanto custa? → How much ____?                            | does it cost
```

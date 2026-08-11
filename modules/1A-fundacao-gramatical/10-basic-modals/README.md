# 10 — Modais básicos: can, must, should, have to

> Modais definem o **tom** do que você diz. A diferença entre *"You must fix this"* e
> *"You could fix this"* é a diferença entre soar ríspido e soar colaborativo — num
> code review isso pesa mais que a gramática.

**Módulo:** 1A · **Sessões:** 1 · **Anterior:** [09 — Perguntas e question tags](../09-questions-and-tags/) · **Próxima:** [11 — Adjetivos e advérbios](../11-adjectives-and-adverbs/)

---

## 1. A ideia em uma frase

Modal + **verbo no infinitivo sem `to`** — e o modal **nunca** muda de forma.

---

## 2. Forma

### As 3 regras de ouro

| Regra | ✅ | ❌ |
|-------|----|----|
| **Nunca leva `-s`** na 3ª pessoa | He **can** help. | *~~He cans~~* |
| **Nunca leva `to`** depois | I **must go**. | *~~I must to go~~* |
| **É o próprio auxiliar** | **Can** you help? · I **can't** help. | *~~Do you can~~* |

> **Exceção:** `have to` **não é modal** — é verbo normal. Conjuga (`has to`), leva
> `to`, e usa `do/does/did` em pergunta e negativa: *Does he **have to** join?*

### Tabela

| Modal | Afirmativo | Negativo | Pergunta |
|-------|-----------|----------|----------|
| **can** | I can review | can't / cannot | Can I…? |
| **could** | I could review | couldn't | Could you…? |
| **must** | I must finish | mustn't | Must I…? *(raro)* |
| **should** | I should test | shouldn't | Should we…? |
| **have to** | I have to / he **has to** | **don't** have to / **doesn't** have to | **Do** you have to…? |

---

## 3. Uso

### 3.1 `can` — habilidade, permissão, possibilidade, pedido

```
I can write SQL.                     ← habilidade
Can I merge this?                    ← permissão
This can break in production.        ← possibilidade
Can you take a look?                 ← pedido (informal)
Could you take a look?               ← pedido (mais educado) ← use este por padrão
```

### 3.2 `should` — conselho, recomendação, expectativa

```
You should add a test for this.      ← recomendação (soa colaborativo)
We shouldn't deploy on Friday.
This should take about two hours.    ← expectativa
Should we roll back?                 ← pedindo opinião
```

> 💼 **`should` é o modal do code review.** *"You should extract this into a function"*
> soa como sugestão. *"You must extract this"* soa como ordem.

### 3.3 `must` vs `have to` — obrigação interna vs externa

| | Origem da obrigação | Exemplo |
|---|---------------------|---------|
| **must** | você mesmo / regra escrita / urgência | I **must** finish this today. · All PRs **must** be reviewed. |
| **have to** | circunstância externa, outra pessoa | I **have to** join the call — the client asked. |

Na prática, em inglês falado, **`have to` é muito mais comum**. `must` aparece
principalmente em documentos, regras e RFCs (*"the client MUST send a token"*).

### 3.4 🔴 `mustn't` ≠ `don't have to` — a diferença mais cara do módulo

| | Significado | Exemplo |
|---|-------------|---------|
| **mustn't** | **proibido** | You **mustn't** commit secrets. *(é proibido)* |
| **don't have to** | **não é necessário** | You **don't have to** attend. *(é opcional)* |

```
You mustn't push to main.        ← se fizer, é violação
You don't have to push to main.  ← pode fazer, mas não precisa
```

Trocar um pelo outro inverte a mensagem. Este erro já gerou incidente real em time.

### 3.5 Escala de polidez — para pedir algo

```
Do this.                                    ← ordem (evite)
You should do this.                         ← recomendação
Can you do this?                            ← pedido direto
Could you do this?                          ← pedido educado         ← padrão
Would you mind doing this?                  ← muito educado
Do you think you could take a look at this? ← máximo cuidado
```

> 🎯 Em ambiente profissional internacional, **`could` é o default seguro**.
> Custa uma palavra e muda a percepção sobre você.

---

## 4. 🇧🇷 Erros de brasileiro

| ❌ | ✅ | Por quê |
|----|----|---------|
| *He cans help.* | He **can** help. | Modal não leva `-s` |
| *I must to go.* | I **must go**. | Modal não leva `to` |
| *I can to help.* | I **can help**. | Idem |
| *Do you can review this?* | **Can** you review this? | Modal é o próprio auxiliar |
| *He don't can do it.* | He **can't** do it. | Idem |
| *You don't must do that.* | You **mustn't** do that. | Negativa de `must` |
| *You mustn't attend* (querendo "não precisa") | You **don't have to** attend. | Inverte o sentido |
| *He have to review it.* | He **has to** review it. | `have to` conjuga |
| *Must I to ask?* | **Must I ask?** | Sem `to` |
| *You must fix this* (em code review) | You **should** fix this. | Registro — `must` soa ríspido |

---

## 5. ✍️ Prática

**A. Traduza (10).**
1. Ele pode revisar isso amanhã.
2. Você não deveria fazer deploy na sexta.
3. Eu tenho que entrar na call às 15h.
4. Você não precisa participar da retro.
5. Você não pode commitar credenciais. *(proibido)*
6. Nós deveríamos adicionar testes aqui.
7. Ela tem que aprovar antes do merge.
8. Você poderia dar uma olhada nisso? *(educado)*
9. Isso pode quebrar em produção.
10. Eu preciso terminar isso hoje. *(obrigação minha)*

**B. Reescreva estas 4 frases de code review** deixando-as colaborativas em vez de ríspidas:
1. *Fix this.*
2. *You must rename this variable.*
3. *This is wrong.*
4. *Do it again.*

**C. Escreva 5 pedidos** que você faria ao seu time — todos com `could` ou `would you mind`.

---

## 6. ✅ Critério de conclusão

- [ ] Acertar 9+ das 10 do exercício A
- [ ] Nunca escrever `to` depois de `can`, `must` ou `should`
- [ ] Explicar em voz alta a diferença entre `mustn't` e `don't have to`, com exemplo próprio
- [ ] Reescrever qualquer ordem direta em pedido educado em menos de 5 segundos
- [ ] Fazer perguntas com modal **sem** usar `do` como auxiliar

**Teste final:** escreva um code review completo de 6 comentários. Todos devem usar modal.
Peça a alguém para ler e dizer se soou colaborativo ou ríspido — este é o único item
do módulo cujo critério é a **percepção do leitor**, não a gramática.

---

## 7. 🔁 Cards pro Anki

```
Ele pode ajudar. → He ____ help.                          | can (sem -s)
Eu tenho que ir. → I must ____ go.                         | ∅ (sem "to")
Você pode revisar? → ____ you review this?                 | Can/Could (sem "do")
Você não precisa vir. → You ____ come.                     | don't have to
Você não pode commitar segredos. → You ____ commit secrets.| mustn't
Ela tem que aprovar. → She ____ approve.                   | has to
Deveríamos testar isso. → We ____ test this.               | should
Pedido educado padrão no trabalho →                        | Could you...?
```

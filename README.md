# 🛠️ Tradutor Tech Simplificado

Hello Hello! Este é um projeto pessoal criado com o objetivo de **quebrar a barreira entre o jargão técnico e o entendimento humano**.

Muitas pessoas enfrentam dificuldades ao ler documentação técnica — tanto pelo idioma quanto pelo uso intenso de termos complexos e abstratos. Este projeto surgiu para resolver esse problema de forma simples, acessível e com potencial de crescimento.

---

## ✨ O que este projeto faz

🔁 **1. Tradução literal:**  
Utiliza a API gratuita do **DeepL** para traduzir trechos técnicos de forma confiável e automática.

✅ **2. Versão explicada: NÃO ESTA FUNCIONANDO REPLICA A TRADUÇÃO LITERAL**  
Gera uma **versão humanizada e simplificada**, com substituições diretas de termos técnicos por definições curtas e acessíveis. 

💡 **3. Pensando adiante:**  
A ideia é evoluir esta simplificação para algo mais **inteligente e contextual**, baseado em um **modelo de linguagem treinado com um banco de conhecimento técnico**.

---

## 💡 Visão de futuro: um modelo de linguagem especializado

O projeto pode evoluir para um **modelo de linguagem de máquina (Machine Learning / NLP)** focado em:

- 🔬 **Compreender o contexto técnico** de trechos traduzidos
- 🗣️ **Gerar explicações mais naturais, amigáveis e adaptadas ao nível do usuário**
- 🧠 **Aprender continuamente**, alimentado por um banco de dados com termos técnicos e exemplos reais de uso

### Exemplo de evolução:

Hoje:
> `"A class is a blueprint for creating objects."`  
> ➤ Tradução: `"Uma classe é um modelo para criar objetos."`  
> ➤ Explicação: `"classe" = modelo de objeto`

Futuro desejado:
> ➤ Explicação inteligente: `"Uma classe é como um molde que define como os objetos devem ser construídos. Imagine um molde de biscoito: ele define o formato, mas cada biscoito é único."`

Essa abordagem permitiria que **pessoas sem background técnico** compreendessem conceitos complexos com analogias, linguagem natural e empatia.

---

## 📁 Estrutura do Projeto

```

.
├── main.py            # Backend FastAPI (integração com DeepL e simplificação)
├── index.html         # Interface simples e direta
├── script.js          # Comunicação frontend ↔ backend
├── style.css          # Estilo básico


````

---

## 🚀 Como rodar localmente

1. **Clone o repositório:**

```bash
git clone https://github.com/seu-usuario/tradutor-tech-simplificado.git
cd tradutor-tech-simplificado
````

2. **Crie um ambiente virtual (opcional):**

```bash
python -m venv venv
venv\Scripts\activate  # no Windows
```

3. **Instale as dependências:**

```bash
pip install fastapi uvicorn requests
```

4. **Insira sua chave da API DeepL no `main.py`**

5. **Execute o backend:**

```bash
uvicorn main:app --reload
```

6. **Abra o `index.html` no navegador.**

---

## 📘 termos.json: O Banco de Conhecimento

O arquivo `termos.json` funciona como um mini banco de conhecimento técnico.
Cada entrada contém um termo e uma explicação amigável, que pode futuramente ser expandida com:

* Exemplos de uso
* Analogias visuais
* Traduções alternativas
* Nível de dificuldade

Esse conhecimento pode ser usado como **fonte de treino para modelos de linguagem personalizados**, no futuro.

---

## 🌍 Sobre os limites da API

Este projeto usa o plano **gratuito da API DeepL**, com limite de **500.000 caracteres por mês**.
⚠️ O upgrade para plano pago **não é automático**, então você não será cobrado sem querer.

---

## 🧠 Próximos passos

* [ ] Expandir o banco de conhecimento (`termos.json`) com mais termos e exemplos
* [ ] Implementar uma interface interativa para explorar os termos explicados
* [ ] Usar **transformers leves (como DistilBERT)** para gerar explicações contextuais
* [ ] Incluir **níveis de explicação** (iniciante, intermediário, avançado)
* [ ] Adicionar **tradução reversa** (PT → EN) com explicação técnica

---

## ✍️ Autoria

Desenvolvido com carinho por \[labarbozadev].
Este projeto nasceu da vontade de **tornar a tecnologia mais acessível** e amigável para todos — mesmo os que nunca escreveram uma linha de código.

---

```


Deseja isso também?
```

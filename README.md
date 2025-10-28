# 💾 Gerador de Dados 📊

Aplicação interativa desenvolvida em **Python + Streamlit** para **gerar dados sintéticos** de diferentes áreas (como Vendas, RH, Logística, Financeiro, etc.).  
Ideal para **testes, prototipagem de dashboards, aprendizado e validação de modelos de dados**.

---

## 🚀 Visão Geral

O **Gerador de Dados** permite criar datasets totalmente fictícios com poucos cliques, de forma simples e rápida.  
Ele utiliza a biblioteca [Faker](https://faker.readthedocs.io/en/master/) para gerar nomes, datas, empresas, cidades e outros dados realistas — tudo dentro de um ambiente Streamlit interativo.

A aplicação foi pensada especialmente para **Analistas de Dados, Cientistas de Dados e Desenvolvedores de BI** que precisam de bases para:
- Testar transformações no Power BI, SQL ou Python;
- Criar dashboards protótipo;
- Simular cenários empresariais sem expor dados reais.

---

## 🧩 Funcionalidades

- Interface web interativa com **Streamlit**;
- Geração de dados fictícios com **Faker (pt_BR)**;
- Seleção de **Área** e **Subárea** específicas;
- Controle da **quantidade de linhas** (10 a 1000);
- Visualização dos dados diretamente na tela;
- **Download em CSV** com apenas um clique.

---

## 🗂️ Estrutura de Áreas e Subáreas

| Área | Subáreas Disponíveis | Descrição |
|------|----------------------|------------|
| **Vendas** | — | Gera vendas com cliente, produto, valor e forma de pagamento |
| **Saúde** | — | Consultas médicas com médico, paciente e convênio |
| **RH** | — | Funcionários com cargo, departamento e salário |
| **Logística** | Transporte / Estoque / Distribuição | Movimentações, controle de estoque e centros de distribuição |
| **Financeiro** | Contas a Pagar / Contas a Receber / Fluxo de Caixa | Entradas e saídas financeiras simuladas |
| **SLA de Atendimento** | Suporte Técnico / Helpdesk / Manutenção | Chamados, tickets e manutenções preventivas/corretivas |

---

## 🖥️ Como Executar Localmente

### 1️⃣ Pré-requisitos
Certifique-se de ter o **Python 3.9+** instalado.  
Em seguida, instale as dependências necessárias:

```bash
pip install streamlit pandas faker

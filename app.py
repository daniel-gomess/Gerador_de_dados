import streamlit as st
import pandas as pd
from faker import Faker
import random
from datetime import datetime, timedelta

# CONFIGURAÇÃO INICIAL
fake = Faker('pt_BR')
st.set_page_config(page_title="Gerador de Dados", page_icon="💾", layout="wide")
# Cabeçalho centralizado
col_l, col_c, col_r = st.columns([1, 2, 1])
with col_c:
    st.title('💾 Gerador de Dados 📊')
    st.markdown("Gerar dados sintéticos por área/subárea para testes e protótipos.")
st.write("")  # espaçamento opcional


# ÁREA E SUBÁREA
areas = {
    'Vendas': [],
    'Saúde': [],
    'RH': [],
    'Logística': ['Transporte', 'Estoque', 'Distribuição'],
    'Financeiro': ['Contas a Pagar', 'Contas a Receber', 'Fluxo de Caixa'],
    'SLA de Atendimento': ['Suporte Técnico', 'Helpdesk', 'Manutenção']
}

# Layout centralizado para seleção de parâmetros
col1, col2, col3 = st.columns([1, 2, 1])  # colunas laterais menores

with col2:
    st.markdown("### ⚙️ Configurações de Geração de Dados")
    area = st.selectbox('📂 Selecione a área:', list(areas.keys()), key='area_select')

    subarea = None
    if areas[area]:
        subarea = st.selectbox('📁 Selecione a subárea:', areas[area], key='subarea_select')

    qtd = st.slider(
        '📊 Quantas linhas deseja gerar?',
        min_value=10, max_value=1000, step=10, value=20,
        key='slider_qtd'
    )


# FUNÇÃO PRINCIPAL
def gerar_dados(area, qtd, subarea=None):
    dados = []


    # ÁREA: VENDAS
    if area == 'Vendas':
        produtos = ['Camisa', 'Calça', 'Tênis', 'Boné', 'Relógio']
        pagamentos = ['Cartão', 'Dinheiro', 'Pix', 'Boleto']
        for _ in range(qtd):
            dados.append({
                'Data': fake.date_between(start_date='-1y', end_date='today'),
                'Cliente': fake.name(),
                'Produto': random.choice(produtos),
                'Valor': round(random.uniform(50, 2000), 2),
                'Forma de Pagamento': random.choice(pagamentos),
                'Vendedor': fake.first_name()
            })


    # ÁREA: SAÚDE
    elif area == 'Saúde':
        especialidades = ['Clínico Geral', 'Cardiologia', 'Ortopedia', 'Dermatologia', 'Pediatria']
        convenios = ['Particular', 'Plano A', 'Plano B', 'SUS']
        for _ in range(qtd):
            dados.append({
                'Data da Consulta': fake.date_between(start_date='-6M', end_date='today'),
                'Paciente': fake.name(),
                'Especialidade': random.choice(especialidades),
                'Convênio': random.choice(convenios),
                'Valor (R$)': round(random.uniform(100, 500), 2),
                'Médico': f"Dr(a). {fake.last_name()}"
            })


    # ÁREA: RH
    elif area == 'RH':
        cargos = ['Coordenador', 'Gerente', 'Técnico', 'Pleno', 'Júnior', 'Sênior']
        departamentos = ['TI', 'Financeiro', 'Vendas', 'Marketing', 'Operações']
        for _ in range(qtd):
            dados.append({
                'Nome': fake.name(),
                'Cargo': random.choice(cargos),
                'Departamento': random.choice(departamentos),
                'Data de Admissão': fake.date_between(start_date='-5y', end_date='today'),
                'Salário (R$)': round(random.uniform(2000, 15000), 2)
            })


    # ÁREA: LOGÍSTICA
    elif area == 'Logística':
        if subarea == 'Transporte':
            tipos_transporte = ['Rodoviário', 'Aéreo', 'Marítimo']
            status = ['Em Trânsito', 'Entregue', 'Atrasado']
            for _ in range(qtd):
                data_inicio = fake.date_between(start_date='-1M', end_date='today')
                # Garante que o término seja entre 1 e 10 dias após o início
                dias_duracao = random.randint(1, 10)
                data_termino = data_inicio + timedelta(days=dias_duracao)

                dados.append({
                    'Data Início': data_inicio,
                    'Data Término': data_termino,
                    'Motorista': fake.name(),
                    'Tipo Transporte': random.choice(tipos_transporte),
                    'Placa Veículo': fake.license_plate(),
                    'Cidade Origem': fake.city(),
                    'Cidade Destino': fake.city(),
                    'Status': random.choice(status)
                })

        elif subarea == 'Estoque':
            produtos = ['Teclado', 'Mouse', 'Monitor', 'Cabo HDMI', 'Notebook']
            for _ in range(qtd):
                dados.append({
                    'Produto': random.choice(produtos),
                    'Quantidade': random.randint(10, 500),
                    'Localização': fake.city(),
                    'Data Atualização': fake.date_between(start_date='-3M', end_date='today')
                })

        elif subarea == 'Distribuição':
            centros = ['SP', 'RJ', 'MG', 'PR', 'RS']
            for _ in range(qtd):
                dados.append({
                    'Centro Distribuição': random.choice(centros),
                    'Pedidos Enviados': random.randint(50, 500),
                    'Pedidos Pendentes': random.randint(0, 50),
                    'Data': fake.date_between(start_date='-2M', end_date='today')
                })


    # ÁREA: FINANCEIRO
    elif area == 'Financeiro':
        if subarea == 'Contas a Pagar':
            categorias = ['Fornecedores', 'Serviços', 'Impostos']
            for _ in range(qtd):
                dados.append({
                    'Data Vencimento': fake.date_between(start_date='-1M', end_date='+1M'),
                    'Fornecedor': fake.company(),
                    'Categoria': random.choice(categorias),
                    'Valor (R$)': round(random.uniform(500, 10000), 2),
                    'Pago': random.choice(['Sim', 'Não'])
                })

        elif subarea == 'Contas a Receber':
            clientes = [fake.company() for _ in range(20)]
            for _ in range(qtd):
                dados.append({
                    'Data Recebimento': fake.date_between(start_date='-1M', end_date='today'),
                    'Cliente': random.choice(clientes),
                    'Nota Fiscal': fake.random_int(1000, 9999),
                    'Valor (R$)': round(random.uniform(1000, 20000), 2),
                    'Status': random.choice(['Pago', 'Em Aberto', 'Atrasado'])
                })

        elif subarea == 'Fluxo de Caixa':
            tipos = ['Entrada', 'Saída']
            for _ in range(qtd):
                tipo = random.choice(tipos)
                valor = random.uniform(500, 10000)
                dados.append({
                    'Data': fake.date_between(start_date='-2M', end_date='today'),
                    'Tipo': tipo,
                    'Descrição': fake.sentence(nb_words=4),
                    'Valor (R$)': round(valor if tipo == 'Entrada' else -valor, 2)
                })


    # ÁREA: SLA DE ATENDIMENTO
    elif area == 'SLA de Atendimento':
        if subarea == 'Suporte Técnico':
            for _ in range(qtd):
                inicio = fake.date_time_between(start_date='-30d', end_date='-1d')
                fim = inicio + timedelta(minutes=random.randint(15, 240))
                dados.append({
                    'ID Chamado': fake.uuid4()[:8],
                    'Cliente': fake.company(),
                    'Data Abertura': inicio.strftime('%Y-%m-%d %H:%M'),
                    'Data Fechamento': fim.strftime('%Y-%m-%d %H:%M'),
                    'Tempo (min)': (fim - inicio).seconds // 60,
                    'Atendente': fake.first_name(),
                    'Status': random.choice(['Resolvido', 'Em Andamento', 'Cancelado'])
                })

        elif subarea == 'Helpdesk':
            categorias = ['Hardware', 'Software', 'Rede', 'E-mail']
            for _ in range(qtd):
                dados.append({
                    'Ticket': fake.uuid4()[:8],
                    'Usuário': fake.name(),
                    'Categoria': random.choice(categorias),
                    'Prioridade': random.choice(['Baixa', 'Média', 'Alta']),
                    'Status': random.choice(['Fechado', 'Aberto', 'Em Análise'])
                })

        elif subarea == 'Manutenção':
            tipos = ['Preventiva', 'Corretiva']
            for _ in range(qtd):
                dados.append({
                    'Equipamento': fake.word(),
                    'Tipo': random.choice(tipos),
                    'Responsável': fake.name(),
                    'Data Execução': fake.date_between(start_date='-3M', end_date='today'),
                    'Custo (R$)': round(random.uniform(300, 8000), 2)
                })

    return pd.DataFrame(dados)

# EXECUÇÃO E EXIBIÇÃO
df = gerar_dados(area, qtd, subarea)
st.dataframe(df, use_container_width=True)

# DOWNLOAD
csv = df.to_csv(index=False, encoding='utf-8-sig')
st.download_button(
    label="📥 Baixar CSV Gerado",
    data=csv,
    file_name=f'dados_{area}_{subarea or "geral"}.csv',
    mime='text/csv'
)

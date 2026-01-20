import streamlit as st
import pandas as pd
from faker import Faker
import random
from datetime import datetime, timedelta, date
from geopy.distance import geodesic

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
    'Fornecedores': [],
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
        min_value=10,
        max_value=1000,
        step=10,
        value=20,
        key='slider_qtd'
    )

# DICIONÁRIO DE COORDENADAS DAS PRINCIPAIS CIDADES BRASILEIRAS
CIDADES_COORDS = {
    'São Paulo': (-23.5505, -46.6333),
    'Rio de Janeiro': (-22.9068, -43.1729),
    'Belo Horizonte': (-19.9167, -43.9345),
    'Brasília': (-15.7939, -47.8828),
    'Curitiba': (-25.4284, -49.2733),
    'Porto Alegre': (-30.0346, -51.2177),
    'Salvador': (-12.9714, -38.5014),
    'Fortaleza': (-3.7319, -38.5267),
    'Recife': (-8.0476, -34.8770),
    'Manaus': (-3.1190, -60.0217),
    'Goiânia': (-16.6869, -49.2648),
    'Campinas': (-22.9099, -47.0626),
    'Florianópolis': (-27.5954, -48.5480),
    'Vitória': (-20.3155, -40.3128),
    'Santos': (-23.9618, -46.3322),
    'Joinville': (-26.3045, -48.8487),
    'Blumenau': (-26.9194, -49.0661),
    'Caxias do Sul': (-29.1678, -51.1794),
    'Ribeirão Preto': (-21.1704, -47.8103),
    'Uberlândia': (-18.9186, -48.2772),
    'Sorocaba': (-23.5015, -47.4526),
    'Cuiabá': (-15.6014, -56.0979),
    'Belém': (-1.4558, -48.5039),
    'João Pessoa': (-7.1195, -34.8450),
    'Natal': (-5.7945, -35.2110)
}

def calcular_distancia(cidade_origem, cidade_destino):
    """Calcula a distância real entre duas cidades brasileiras"""
    if cidade_origem in CIDADES_COORDS and cidade_destino in CIDADES_COORDS:
        coords_origem = CIDADES_COORDS[cidade_origem]
        coords_destino = CIDADES_COORDS[cidade_destino]
        distancia_km = geodesic(coords_origem, coords_destino).kilometers
        return round(distancia_km)
    return random.randint(100, 2000)  # fallback caso cidade não esteja no dicionário

# FUNÇÃO PRINCIPAL
def gerar_dados(area, qtd, subarea=None):
    dados = []

    # ÁREA: VENDAS
    if area == 'Vendas':
        # Lista fixa de 10 vendedores
        vendedores = [
            "Ana", "Bruno", "Carla", "Diego", "Eduardo",
            "Fernanda", "Gabriel", "Helena", "João", "Mariana"
        ]

        # Produtos de informática com faixas de preço coerentes
        produtos_precos = {
            'Mouse': (30, 150),
            'Teclado': (50, 300),
            'Headset': (80, 400),
            'Webcam': (100, 500),
            'Memória RAM 8GB': (150, 300),
            'Memória RAM 16GB': (250, 500),
            'SSD 256GB': (180, 350),
            'SSD 512GB': (300, 600),
            'SSD 1TB': (450, 900),
            'HD Externo 1TB': (250, 450),
            'Placa de Vídeo GTX': (1200, 2500),
            'Placa de Vídeo RTX': (2500, 5000),
            'Processador Intel i5': (800, 1500),
            'Processador Intel i7': (1500, 2500),
            'Processador AMD Ryzen 5': (700, 1300),
            'Processador AMD Ryzen 7': (1300, 2200),
            'Fonte 500W': (200, 400),
            'Fonte 700W': (350, 600),
            'Placa-Mãe': (400, 1200),
            'Gabinete': (150, 600),
            'Monitor 24"': (600, 1200),
            'Monitor 27"': (900, 2000),
            'Notebook': (2000, 5000),
            'Computador Desktop': (2500, 6000),
            'Impressora': (400, 1500),
            'Roteador Wi-Fi': (100, 400),
            'Switch de Rede': (150, 500),
            'Cabo HDMI': (20, 80),
            'Cabo de Rede': (15, 50),
            'Pendrive 32GB': (25, 60),
            'Pendrive 64GB': (40, 90),
            'Cooler para CPU': (50, 200),
            'Cadeira Gamer': (600, 2000),
            'Mesa para Computador': (300, 1200)
        }

        pagamentos = ['Cartão', 'Dinheiro', 'Pix', 'Boleto']

        # Data mínima: 1º de janeiro de 2025
        data_inicio_minima = date(2025, 1, 1)
        # Data atual
        data_atual = datetime.now().date()

        for _ in range(qtd):
            # Gera data a partir de janeiro de 2025
            data_venda = fake.date_between(start_date=data_inicio_minima, end_date='today')

            # Gera nome sem títulos (apenas primeiro e último nome)
            nome_cliente = f"{fake.first_name()} {fake.last_name()}"

            # Seleciona produto e sua faixa de preço
            produto = random.choice(list(produtos_precos.keys()))
            preco_min, preco_max = produtos_precos[produto]

            # Define forma de pagamento
            forma_pagamento = random.choice(pagamentos)

            # Define STATUS e Nº VEZES baseado na forma de pagamento
            if forma_pagamento in ['Pix', 'Dinheiro']:
                status = 'PAGO'
                num_vezes = 1
            else:
                # Para outras formas, escolhe entre PAGO, NÃO PAGO ou PENDENTE
                status = random.choice(['PAGO', 'NÃO PAGO', 'PENDENTE'])
                # Número de parcelas entre 1 e 12
                num_vezes = random.randint(1, 12)

            # Define quantidade do produto
            quantidade = random.randint(1, 5)

            # Define valor unitário dentro da faixa do produto
            valor_unitario = round(random.uniform(preco_min, preco_max), 2)
            valor_total = valor_unitario * quantidade

            # Define desconto em PERCENTUAL (0% a 20%)
            desconto_percentual = random.choice([0, 0, 0, 5, 10, 15, 20])
            desconto_valor = round(valor_total * (desconto_percentual / 100), 2)

            # Valor final
            valor_final = round(valor_total - desconto_valor, 2)

            # Calcula DATA VENCIMENTO
            if forma_pagamento in ['Pix', 'Dinheiro'] or num_vezes == 1:
                # Pagamento à vista - vencimento é a data da compra
                data_vencimento = data_venda
            else:
                # Pagamento parcelado - calcula próximo vencimento
                # Primeira parcela vence 30 dias após a compra
                dias_por_parcela = 30

                # Calcula quantas parcelas já venceram até hoje
                dias_desde_compra = (data_atual - data_venda).days
                parcelas_vencidas = dias_desde_compra // dias_por_parcela

                # Próxima parcela a vencer (se todas já venceram, mostra a última)
                if parcelas_vencidas >= num_vezes:
                    # Todas as parcelas já venceram - mostra a última parcela
                    proxima_parcela = num_vezes
                else:
                    # Ainda há parcelas a vencer - mostra a próxima
                    proxima_parcela = parcelas_vencidas + 1

                # Data de vencimento da próxima parcela
                data_vencimento = data_venda + timedelta(days=proxima_parcela * dias_por_parcela)

            dados.append({
                'Data': data_venda,
                'Cliente': nome_cliente,
                'Produto': produto,
                'Quantidade': quantidade,
                'Valor': valor_final,
                'Desconto': f"{desconto_percentual}%",
                'Forma de Pagamento': forma_pagamento,
                'Nº Vezes': num_vezes,
                'Data Vencimento': data_vencimento,
                'Status': status,
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

    # ÁREA: FORNECEDORES
    elif area == 'Fornecedores':
        categorias = ['Eletrônicos', 'Móveis', 'Material de Escritório', 'Alimentos', 'Limpeza']

        for _ in range(qtd):
            dados.append({
                'Razão Social': fake.company(),
                'Nome Fantasia': fake.company_suffix(),
                'Endereço': fake.street_address(),
                'Cidade': fake.city(),
                'Bairro': fake.street_name(),
                'Estado': fake.state_abbr(),
                'CEP': fake.postcode(),
                'CNPJ': fake.cnpj(),
                'Numero de Contato': fake.phone_number(),
                'Email de contato': fake.company_email()
            })

    # ÁREA: LOGÍSTICA
    elif area == 'Logística':
        if subarea == 'Transporte':
            tipos_transporte = ['Rodoviário', 'Aéreo', 'Marítimo']
            tipos_combustivel = ['Óleo Diesel S10', 'Óleo Diesel S500']

            # Modelos de veículos disponíveis
            veiculos_scania = ['R 410', 'R 450', 'G 540', 'G 450', 'S 540', '770 S', 'P 320', 'P 410']
            veiculos_mercedes = ['Accelo', 'Atego', 'Axor', 'Actros']

            # Preços médios do diesel em janeiro de 2026 (R$ por litro)
            # S10 é ligeiramente mais caro que S500
            preco_diesel = {
                'Óleo Diesel S10': (6.20, 6.80),
                'Óleo Diesel S500': (6.00, 6.60)
            }

            # Frota fixa de 15 veículos com seus respectivos motoristas
            frota = []
            for i in range(15):
                # Gera nome completo sem títulos
                nome_completo = f"{fake.first_name()} {fake.last_name()}"
                placa = fake.license_plate()

                # Alterna entre Scania e Mercedes (60% Scania, 40% Mercedes)
                if random.random() < 0.6:
                    marca = 'Scania'
                    modelo = random.choice(veiculos_scania)
                else:
                    marca = 'Mercedes'
                    modelo = random.choice(veiculos_mercedes)

                veiculo_nome = f"{marca} {modelo}"

                frota.append({
                    'motorista': nome_completo,
                    'placa': placa,
                    'veiculo': veiculo_nome
                })

            # Data atual para comparação
            data_atual = datetime.now().date()

            # Data inicial: 1º de março de 2025
            data_inicio_minima = date(2025, 3, 1)

            # Lista de cidades disponíveis
            cidades_disponiveis = list(CIDADES_COORDS.keys())

            for _ in range(qtd):
                # Data início a partir de março/2025
                data_inicio = fake.date_between(start_date=data_inicio_minima, end_date='today')

                # Define a previsão de término (entre 1 e 10 dias após o início)
                dias_previsao = random.randint(1, 10)
                data_previsao_termino = data_inicio + timedelta(days=dias_previsao)

                # Define o término real, que pode ser antes ou depois da previsão
                # 70% de chance de entregar no prazo ou antes, 30% de atrasar
                if random.random() < 0.7:
                    # Entrega no prazo ou antes
                    dias_duracao = random.randint(1, dias_previsao)
                else:
                    # Entrega atrasada
                    dias_duracao = random.randint(dias_previsao + 1, dias_previsao + 5)

                data_termino = data_inicio + timedelta(days=dias_duracao)

                # Se a data de término for no futuro, deixa em branco
                if data_termino > data_atual:
                    data_termino_display = None
                else:
                    data_termino_display = data_termino

                # Seleciona um veículo da frota (motorista e placa juntos)
                veiculo = random.choice(frota)

                # Seleciona cidades origem e destino (diferentes)
                cidade_origem = random.choice(cidades_disponiveis)
                cidade_destino = random.choice([c for c in cidades_disponiveis if c != cidade_origem])

                # Coordenadas de origem e destino
                lat_origem, lon_origem = CIDADES_COORDS[cidade_origem]
                lat_destino, lon_destino = CIDADES_COORDS[cidade_destino]

                # Calcula distância real entre as cidades
                distancia_km = calcular_distancia(cidade_origem, cidade_destino)

                # Consumo médio de caminhão: 2.5 a 4 km/litro
                # Quanto maior a distância, melhor a média (viagens longas em rodovia)
                if distancia_km > 1000:
                    consumo_medio = random.uniform(3.2, 4.0)
                elif distancia_km > 500:
                    consumo_medio = random.uniform(2.8, 3.5)
                else:
                    consumo_medio = random.uniform(2.5, 3.2)

                # Calcula litros necessários (com pequena margem de 5-15% para abastecimentos extras)
                litros_base = distancia_km / consumo_medio
                margem = random.uniform(1.05, 1.15)
                litros_total = round(litros_base * margem, 2)

                # Tipo de combustível (95% S10, 5% S500 para caminhões modernos)
                combustivel = random.choices(tipos_combustivel, weights=[95, 5])[0]

                # Valor do litro baseado no tipo de combustível
                preco_min, preco_max = preco_diesel[combustivel]
                valor_litro = round(random.uniform(preco_min, preco_max), 2)

                dados.append({
                    'Data Início': data_inicio,
                    'Previsão Término': data_previsao_termino,
                    'Data Término': data_termino_display,
                    'Motorista': veiculo['motorista'],
                    'Veículo': veiculo['veiculo'],
                    'Tipo Transporte': random.choice(tipos_transporte),
                    'Placa Veículo': veiculo['placa'],
                    'Cidade Origem': cidade_origem,
                    'Latitude Origem': lat_origem,
                    'Longitude Origem': lon_origem,
                    'Cidade Destino': cidade_destino,
                    'Latitude Destino': lat_destino,
                    'Longitude Destino': lon_destino,
                    'Distância (KM)': distancia_km,
                    'Litros': litros_total,
                    'Combustível': combustivel,
                    'Valor do Litro (R$)': valor_litro,
                    'Valor Mercadoria (R$)': round(random.uniform(1000, 50000), 2)
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

# PAGINAÇÃO
st.markdown("---")
col_pag1, col_pag2, col_pag3 = st.columns([2, 1, 2])

with col_pag2:
    linhas_por_pagina = st.selectbox(
        '📄 Linhas por página:',
        options=[10, 20, 50, 100],
        index=1,
        key='linhas_pagina'
    )

# Calcula total de páginas
total_paginas = (len(df) - 1) // linhas_por_pagina + 1

# Controle de página
if 'pagina_atual' not in st.session_state:
    st.session_state.pagina_atual = 1

col_nav1, col_nav2, col_nav3, col_nav4, col_nav5 = st.columns([1, 1, 2, 1, 1])

with col_nav1:
    if st.button('⏮️ Primeira', use_container_width=True):
        st.session_state.pagina_atual = 1

with col_nav2:
    if st.button('⬅️ Anterior', use_container_width=True):
        if st.session_state.pagina_atual > 1:
            st.session_state.pagina_atual -= 1

with col_nav3:
    st.markdown(f"**Página {st.session_state.pagina_atual} de {total_paginas}**")

with col_nav4:
    if st.button('Próxima ➡️', use_container_width=True):
        if st.session_state.pagina_atual < total_paginas:
            st.session_state.pagina_atual += 1

with col_nav5:
    if st.button('Última ⏭️', use_container_width=True):
        st.session_state.pagina_atual = total_paginas

# Determina o intervalo de linhas para exibição
inicio = (st.session_state.pagina_atual - 1) * linhas_por_pagina
fim = inicio + linhas_por_pagina

st.dataframe(df.iloc[inicio:fim])

# Download do CSV
csv = df.to_csv(index=False).encode('utf-8')
st.download_button(
    label="⬇️ Baixar CSV",
    data=csv,
    file_name="dados_sinteticos.csv",
    mime="text/csv"
)

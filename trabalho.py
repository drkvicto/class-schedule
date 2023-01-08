import streamlit as st

st.sidebar.title('Menu')
PaginaSelecionada = st.sidebar.selectbox('Selecione o Período', ['Selecione o Período', 'Primeiro Período', 'Segundo Período', 'Terceiro Período' ])


if PaginaSelecionada == 'Selecione o Período':
    st.title('Class Schedule')
    st.header('Quadro de avisos')
    st.write('O ônibus da UERJ não funcionará no dia 02/01')
elif PaginaSelecionada == 'Primeiro Período':
    st.title('Primeiro Período')
    MateriaSelecionada1 = st.sidebar.selectbox('Selecione a sua matéria', ['Selecione a sua matéria', 'Cálculo 1', 'Expressão Gráfica', 'Geometria Analítica', 'Introdução à Computação', 'Comunicação e Expressão', 'Introdução à Engenharia de Produção', 'Química Teórica 1', 'Química Experimental 1'])
    if MateriaSelecionada1 == 'Selecione a sua matéria':
        st.subheader('Selecione a sua matéria')
    elif MateriaSelecionada1 == 'Cálculo 1':
        st.subheader('Cálculo 1')
        st.selectbox('Selecione a sua turma', ['Turma 1', 'Turma 2', 'Turma 3'])
    elif MateriaSelecionada1 == 'Expressão Gráfica':
        st.subheader('Expressão Gráfica')
        st.selectbox('Selecione a sua turma', ['Turma 1', 'Turma 2'])
    elif MateriaSelecionada1 == 'Geometria Analítica':
        st.subheader('Geometria Analítica')
        st.selectbox('Selecione a sua turma', ['Turma 1', 'Turma 2', 'Turma 3'])
    elif MateriaSelecionada1 == 'Introdução à Computação':
        st.subheader('Introdução à Computação')
        st.selectbox('Selecione a sua turma', ['Turma 1', 'Turma 2'])
    elif MateriaSelecionada1 == 'Comunicação e Expressão':
        st.subheader('Comunicação e Expressão')
        st.selectbox('Selecione a sua turma', ['Turma 1'])
    elif MateriaSelecionada1 == 'Introdução à Engenharia de Produção':
        st.subheader('Introdução à Engenharia de Produção')
        st.selectbox('Selecione a sua turma', ['Turma 1'])
elif PaginaSelecionada == 'Segundo Período':
    st.title('Segundo Período')
    st.sidebar.selectbox('Selecione a sua matéria', ['Selecione a sua matéria', 'Álgebra Linear', 'Cálculo 2', 'Cálculo Numérico 1', 'Desenho Técnico', 'Física Teórica 1', 'Física Experimental 1', 'Metodologia Científica', 'Química Teórica 2'])
elif PaginaSelecionada == 'Terceiro Período':
    st.title('Terceiro Período')
    st.sidebar.selectbox('Selecione a sua matéria', ['Selecione a sua matéria', 'Análise Vetorial', 'Equações Diferenciadas Ordinárias', 'Física Teórica 2', 'Física Experimental 2', 'Probabilidade e Estatística', 'Programação Linear', 'Mecânica Geral', 'Introdução à Engenharia Ambiental '])

    






    























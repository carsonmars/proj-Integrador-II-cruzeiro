Olá, estudante.

A seguir, você dará continuidade ao desenvolvimento da sua solução através dos campos específicos para a resolução dos 3 desafios propostos, lembrando que eles se complementam.

**Nome:** Carson Marques Andrade Rodrigues de Souza
**RGM:** 32846916

**Documentação:**

Revisite a documentação do projeto desenvolvido na PIT I, peça *feedback* aos seus colegas e veja possíveis melhorias. Insira, a seguir, toda a documentação atualizada e melhorada:

---

### **MELHORIAS DE PROJETO**

**DESENVOLVIMENTO DE CARDÁPIO**

- **Variedade e Inovação**: Adicione opções sazonais e temáticas para atrair clientes em diferentes épocas do ano. Por exemplo, bebidas especiais de inverno como chocolate quente com especiarias ou refrescos de verão com frutas tropicais.
- **Dietas Especiais**: Inclua opções para dietas específicas, como veganas, sem glúten e sem lactose. Isso pode incluir leites vegetais, sobremesas sem glúten e lanches saudáveis.
- **Ingredientes Locais e Orgânicos**: Utilize ingredientes locais e orgânicos para destacar a qualidade e frescor dos produtos, além de apoiar produtores locais.
- **Menu Infantil**: Crie um menu infantil com opções saudáveis e atrativas para as crianças, como mini sanduíches e sucos naturais.
- **Parcerias com Fornecedores**: Estabeleça parcerias com fornecedores de produtos gourmet, como chocolates artesanais e queijos especiais, para diversificar ainda mais o cardápio.
- **Degustações e Eventos**: Organize eventos de degustação de novos itens do cardápio para receber feedback dos clientes e criar um senso de comunidade.

---

### **Cardápio Sabor & Aroma**

**Bebidas Quentes**

- **Café Expresso**: R\$ 5,00
- **Cappuccino**: R\$ 8,00
- **Latte**: R\$ 7,50
- **Chocolate Quente com Especiarias** (sazonal): R\$ 9,00
- **Chá de Ervas Orgânicas**: R\$ 6,00

**Bebidas Frias**

- **Frappuccino de Caramelo**: R\$ 10,00
- **Smoothie de Frutas Tropicais**: R\$ 12,00
- **Chá Gelado com Limão e Hortelã**: R\$ 7,00
- **Refresco de Verão com Frutas Tropicais** (sazonal): R\$ 8,50

**Opções para Dietas Especiais**

- **Latte com Leite de Amêndoas**: R\$ 8,00
- **Bolo de Cenoura Sem Glúten**: R\$ 6,50
- **Cookie Vegano de Chocolate**: R\$ 5,00
- **Sanduíche de Grão-de-Bico e Abacate**: R\$ 12,00

**Lanches e Sobremesas**

- **Croissant de Queijo e Presunto**: R\$ 7,50
- **Torta de Maçã com Canela**: R\$ 8,00
- **Brownie de Chocolate Artesanal**: R\$ 6,00
- **Mini Sanduíches Infantis**: R\$ 5,00

**Ingredientes Locais e Orgânicos**

- **Salada de Frutas Orgânicas**: R\$ 10,00
- **Tábua de Queijos Artesanais**: R\$ 15,00
- **Chocolate Artesanal com Café**: R\$ 7,00

**Menu Infantil**

- **Mini Sanduíche de Queijo e Presunto**: R\$ 5,00
- **Suco Natural de Laranja**: R\$ 4,50
- **Biscoitos Decorados**: R\$ 3,50

---

### **MARKETING E PROMOÇÃO**

**Redes Sociais**

- **Postagens Regulares**: Crie um calendário de postagens com conteúdo variado, incluindo fotos dos produtos, histórias dos clientes e bastidores da cafeteria.
- **Promoções Exclusivas**: Ofereça descontos e promoções exclusivas para seguidores das redes sociais, como "Desconto de 10% para quem mostrar este post".
- **Parcerias com Influenciadores**: Colabore com influenciadores locais para promover a cafeteria. Eles podem compartilhar suas experiências e atrair novos clientes.
- **Conteúdo Interativo**: Utilize enquetes, quizzes e desafios para aumentar o engajamento dos seguidores.
- **Stories e Reels**: Use stories e reels para mostrar novidades, eventos ao vivo e momentos do dia a dia na cafeteria.

**Eventos e Degustações**

- **Degustação de Café**: Organize sessões de degustação de diferentes tipos de café, explicando as características de cada um e a origem dos grãos.
- **Workshops de Preparo**: Realize workshops sobre métodos de preparo de café, como prensa francesa, aeropress e métodos de filtragem.
- **Eventos Temáticos**: Crie eventos temáticos, como "Noite do Café com Chocolate" ou "Festival de Cafés Gelados", para atrair diferentes públicos.
- **Parcerias com Produtores**: Convide produtores de café para falar sobre o processo de cultivo e colheita, criando uma conexão mais profunda com os clientes.
- **Feedback dos Participantes**: Após cada evento, colete feedback dos participantes para melhorar futuras edições e entender melhor as preferências do público.

---

### **Configuração Inicial**

1. **Ambiente de Desenvolvimento**:

   - Configure um ambiente de desenvolvimento local utilizando Python e Streamlit.
   - Instale as dependências necessárias listadas no arquivo `requirements.txt`:
     ```bash
     pip install -r requirements.txt
     ```
2. **Estrutura do Projeto**:

   - Organize o projeto de forma clara e lógica. Utilize a seguinte estrutura de diretórios:
     ```
     cafeteria_project/
     ├── app/
     │   ├── __init__.py
     │   ├── menu.py
     │   ├── order.py
     ├── tests/
     │   ├── test_menu.py
     │   ├── test_order.py
     ├── requirements.txt
     ├── README.md
     ├── setup.py
     └── main.py
     ```

---

### **Funcionalidades Específicas**

1. **Tela Inicial**:

   - Crie uma tela inicial com botões de navegação para as principais funcionalidades: “Fazer Pedido” e “Cardápio”.
   - Utilize o Streamlit para criar a interface:
     ```python
     import streamlit as st

     st.title("Bem-vindo à Cafeteria Sabor & Aroma")
     st.button("Fazer Pedido")
     st.button("Cardápio")
     ```
2. **Tela de Cardápio**:

   - Implemente uma galeria para exibir os itens do cardápio.
   - Conecte a galeria a uma fonte de dados (arquivo CSV) contendo os itens do cardápio, com colunas para nome, descrição, preço e imagem.
   - Exemplo de código:
     ```python
     import pandas as pd
     import streamlit as st

     df = pd.read_csv("cardapio.csv")
     st.dataframe(df)
     ```
3. **Tela de Pedido**:

   - Adicione campos para o cliente selecionar itens do cardápio e quantidade.
   - Inclua um botão para confirmar o pedido, que salva os dados em um arquivo CSV.
   - Exemplo de código:
     ```python
     import streamlit as st
     import pandas as pd

     item = st.selectbox("Selecione um item", ["Café Expresso", "Cappuccino", "Latte"])
     quantidade = st.number_input("Quantidade", min_value=1, max_value=10)
     if st.button("Adicionar ao Carrinho"):
         pedidos = pd.DataFrame({"item": [item], "quantidade": [quantidade]})
         pedidos.to_csv("pedidos.csv", mode='a', header=False, index=False)
         st.write(f"{quantidade}x {item} adicionado ao carrinho.")
     ```

---

### **Integração e Testes**

4. **Integração com Fontes de Dados**:

   - Conecte seu aplicativo a um arquivo CSV para armazenar informações de pedidos e cardápio.
   - Exemplo de código:
     ```python
     import pandas as pd

     df = pd.read_csv("pedidos.csv")
     ```
5. **Testes Automatizados**:

   - Implemente testes automatizados para garantir a qualidade do código.
   - Utilize frameworks como `unittest` para escrever testes unitários.
   - Exemplo de teste com `unittest`:
     ```python
     import unittest

     class TestMenu(unittest.TestCase):
         def test_item_adicionado(self):
             self.assertEqual(adicionar_item("Café Expresso", 2), "2x Café Expresso adicionado ao carrinho.")

     if __name__ == '__main__':
         unittest.main()
     ```

---

### **Publicação**

6. **Hospedagem**:

   - Utilize uma plataforma gratuita como Streamlit Community Cloud para hospedar sua aplicação.
   - Conecte seu repositório GitHub e configure o pipeline de CI/CD para implantar automaticamente sua aplicação.
7. **Compartilhamento**:

   - Compartilhe o link da aplicação com os usuários relevantes e configure as permissões de acesso.

---

### **Boas Práticas de Desenvolvimento de Software**

8. **Código Limpo e Simples**: Mantenha o código fácil de ler e entender. Utilize nomes de variáveis e funções descritivos e evite complexidade desnecessária.
9. **Testes Contínuos**: Implemente testes automatizados para garantir a qualidade do código.
10. **Consistência no Código**: Adote um guia de estilo consistente, como o PEP 8, para manter a uniformidade no código.
11. **Revisão de Código**: Realize revisões de código regularmente para identificar problemas e compartilhar conhecimento entre a equipe.
12. **Documentação**: Mantenha a documentação atualizada e detalhada. Inclua comentários no código e crie documentação externa para explicar a arquitetura e o funcionamento do sistema.

---

### **Testes da Solução**

Escolha 5 colegas para testar sua aplicação, disponibilize o *link* de acesso ou os recursos necessários para que testem como usuários. Preencha a Tabela a seguir com as informações obtidas:

| **Nome:** | **Data do teste:** | **O que testou e funcionou:** | **O que testou e não funcionou -- O que deve ser corrigido:** | **Funcionalidade não testada (faltou ou não foi implementada):** |
| --------------- | ------------------------ | ----------------------------------- | -------------------------------------------------------------------- | ------------------------------------------------------------------------ |
|                 |                          |                                     |                                                                      |                                                                          |
|                 |                          |                                     |                                                                      |                                                                          |
|                 |                          |                                     |                                                                      |                                                                          |
|                 |                          |                                     |                                                                      |                                                                          |
|                 |                          |                                     |                                                                      |                                                                          |

---

### **Vídeo da Solução Atualizada**

Após levantar os *feedbacks* e executar as correções necessárias e pertinentes, grave um vídeo de **até 5 minutos** apresentando as modificações realizadas no sistema.

| ***Link* para o vídeo** |
| -------------------------------- |
|                                  |

---

**Codificação:**

Na Tabela a seguir insira as informações referentes ao desenvolvimento do código do processo.

| **Linguagem**                                                                           | **Python**                    |
| --------------------------------------------------------------------------------------------- | ----------------------------------- |
| **Banco de Dados**                                                                      | **CSV**                       |
| **Hospedagem**                                                                          | **Streamlit Community Cloud** |
| **Plataforma**                                                                          | **Streamlit**                 |
| **Modo de Codificação**                                                               | \(x\) *Tradicional*               |
| ***Link* do repositório no [GitHub](https://github.com/login) com os códigos abertos** | Desenvolvido na plataforma GitHub.  |
| ***Link* da solução em funcionamento**                                              |                                     |
| ***Link* do vídeo narrado (no mínimo 5 min)**                                       |                                     |

---

Espero que essa versão do documento atenda às suas necessidades!

import requests

# URL configurada com o limite máximo de 10 campos úteis
URL = "https://restcountries.com/v3.1/all?fields=name,translations,capital,currencies,region,subregion,languages,population,area,timezones"


def carregar_banco_de_dados():
    """Baixa os dados de todos os países uma única vez ao iniciar o programa."""
    print("Carregando banco de dados de países. Aguarde...")
    try:
        response = requests.get(URL, timeout=8)
        response.raise_for_status()
        print("Dados carregados com sucesso!\n")
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Falha ao carregar os dados: {e}")
        return None


def formatar_numero(numero):
    """Formata números com pontos de milhar de forma segura."""
    if isinstance(numero, (int, float)):
        return f"{numero:,.0f}".replace(",", ".")
    return "Dado indisponível"


def exibir_menu_informacoes(pais):
    """Submenu interativo para escolher qual dado do país exibir."""
    nome_pt = pais.get('translations', {}).get('por', {}).get('common', 'Nome Desconhecido')

    while True:
        print(f"\n--- PAÍS SELECIONADO: {nome_pt.upper()} ---")
        print("Escolha qual informacao voce deseja ver:")
        print("1. Capital")
        print("2. Populacao")
        print("3. Area Territorial")
        print("4. Regiao e Sub-regiao")
        print("5. Idiomas Oficiais")
        print("6. Moedas")
        print("7. Fusos Horarios")
        print("8. Ver Tudo")
        print("0. Voltar para a pesquisa")

        escolha = input("Digite o numero da opcao: ").strip()
        print("-" * 30)

        if escolha == '0':
            break

        elif escolha == '1':
            capitais = pais.get('capital', [])
            texto_capital = ", ".join(capitais) if capitais else "Nenhuma capital registrada"
            print(f"Capital: {texto_capital}")

        elif escolha == '2':
            pop = pais.get('population', 0)
            print(f"Populacao: {formatar_numero(pop)} habitantes")

        elif escolha == '3':
            area = pais.get('area', 0)
            print(f"Area: {formatar_numero(area)} km2")

        elif escolha == '4':
            regiao = pais.get('region', 'Desconhecida')
            subregiao = pais.get('subregion', 'Desconhecida')
            print(f"Regiao: {regiao}")
            print(f"Sub-regiao: {subregiao}")

        elif escolha == '5':
            idiomas = pais.get('languages', {})
            texto_idiomas = ", ".join(idiomas.values()) if idiomas else "Nenhum idioma registrado"
            print(f"Idiomas: {texto_idiomas}")

        elif escolha == '6':
            moedas = pais.get('currencies', {})
            if moedas:
                nomes_moedas = [dados.get('name', 'Desconhecida') for dados in moedas.values()]
                print(f"Moeda(s): {', '.join(nomes_moedas)}")
            else:
                print("Moeda(s): Nenhuma moeda oficial")

        elif escolha == '7':
            fusos = pais.get('timezones', [])
            texto_fusos = ", ".join(fusos) if fusos else "Desconhecido"
            print(f"Fusos Horarios: {texto_fusos}")

        elif escolha == '8':
            capitais = ", ".join(pais.get('capital', []))
            print(f"Capital: {capitais or 'Nenhuma'}")
            print(f"Populacao: {formatar_numero(pais.get('population', 0))}")
            print(f"Area: {formatar_numero(pais.get('area', 0))} km2")
            print(f"Regiao: {pais.get('region', '')} ({pais.get('subregion', '')})")

            idiomas = ", ".join(pais.get('languages', {}).values())
            print(f"Idiomas: {idiomas or 'Nenhum'}")

            moedas = [d.get('name', '') for d in pais.get('currencies', {}).values()]
            print(f"Moedas: {', '.join(moedas) or 'Nenhuma'}")
            print(f"Fusos: {', '.join(pais.get('timezones', []))}")

        else:
            print("Opcao invalida. Tente novamente.")

        input("\nPressione ENTER para continuar...")

def menu_principal():
    paises = carregar_banco_de_dados()

    if not paises or not isinstance(paises, list):
        print("Encerrando o programa por falha nos dados.")
        return

    while True:
        print("\n" + "=" * 40)
        print("   SISTEMA DE CONSULTA DE PAISES")
        print("=" * 40)
        print("Digite o nome do pais (ex: Brasil)")
        print("Ou digite '0' para sair.")

        busca = input("\nPesquisa: ").strip().lower()

        if busca == '0':
            print("Encerrando o programa. Ate logo!")
            break

        if not busca:
            print("Por favor, digite um nome valido.")
            continue

        # Filtra a lista de países localmente
        resultados = []
        for pais in paises:
            nome_eng = pais.get('name', {}).get('common', '').lower()
            nome_pt = pais.get('translations', {}).get('por', {}).get('common', '').lower()

            if busca in nome_eng or busca in nome_pt:
                resultados.append(pais)

        if len(resultados) == 0:
            print("Nenhum pais encontrado com esse nome. Tente novamente.")

        elif len(resultados) == 1:
            exibir_menu_informacoes(resultados[0])

        else:
            print(f"\nForam encontrados {len(resultados)} paises:")
            for indice, pais in enumerate(resultados):
                nome = pais.get('translations', {}).get('por', {}).get('common', 'Desconhecido')
                print(f"[{indice + 1}] {nome}")

            print("[0] Cancelar")

            escolha_desempate = input("\nQual deles voce deseja? Digite o numero: ").strip()

            if escolha_desempate.isdigit():
                indice_escolhido = int(escolha_desempate)
                if 1 <= indice_escolhido <= len(resultados):
                    pais_selecionado = resultados[indice_escolhido - 1]
                    exibir_menu_informacoes(pais_selecionado)
                elif indice_escolhido != 0:
                    print("Numero invalido.")
            else:
                print("Entrada invalida.")


if __name__ == "__main__":
    menu_principal()
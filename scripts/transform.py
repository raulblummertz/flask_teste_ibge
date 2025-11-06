import pandas as pd
from scripts.database import db
from flask import jsonify

def tl_dados(dados):

    try:
        for item in dados:
            dadosTransformados = []
            identificador = item.get("id")
            indicador = item.get("indicador")
            match str(identificador):
                    case '77818':
                        tablename = 'turismo'
                    case '77819':
                        tablename = 'educacao'
                    case '77820':
                        tablename = 'saude'
            series_list = item.get("series", [])
            for serie in series_list:
                pais = serie['pais']['nome']
                serie_data = serie.get("serie", [])
                if not serie_data:
                    continue
                for dictAno in serie_data:
                    for chave, valor in dictAno.items():
                        if not chave.isdigit():
                            continue

                        if valor in (None, "", "-"):
                            continue
                        dadosTransformados.append({
                            "pais": pais,
                            "indicador": indicador,
                            "ano": chave,
                            "valor": valor})
            if dadosTransformados:
                dataframe = pd.DataFrame(dadosTransformados)
                dataframe_inserido = dataframe[['pais', 'ano', 'valor']]
                dataframe_inserido.rename(columns={'valor': 'indicador'}, inplace=True)
                dataframe_inserido.to_sql(tablename, db.engine, if_exists='append', index=False)

        return jsonify({'message':'Dados inseridos com sucesso!'}), 200
    except Exception as e:
        import traceback
        traceback.print_exc()
        return jsonify({'message': str(e)}), 500
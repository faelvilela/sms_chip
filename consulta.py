import pandas as pd
import pyodbc

#se for score 1 e 2 usar complemento abaixo na frente de TPTEL_TEL = 2 
# AND SCORE_TEL IN (1,2)

def conectar(numero_lote):
    conn_str = 'DRIVER={SQL Server};SERVER=192.168.0.38;DATABASE=Nectar;UID=imaps;PWD=imaps'
    query = f"""
        SELECT  CONCAT('+55',RTRIM(DDD_TEL),RTRIM(TELEF_TEL)) AS TELEFONE, RTRIM(NOME_DEV) AS NOME
        FROM iMapsNectar_Contratos
        JOIN iMapsNectar_Devedores ON IDDEV_CON = IDDEV_DEV
        JOIN iMapsNectar_OcorrenciasEnvios ON IDCON_AND = IDCON_CON
        JOIN iMapsNectar_Telefones ON IDTEL_TEL = IDTEL_AND
        JOIN iMapsNectar_Ocorrencias ON IDOCO_OCO = IDOCO_AND
        WHERE IDLOTE_AND = '{numero_lote}' AND STATU_TEL = 0 AND TPTEL_TEL = 2
        ORDER BY TELEF_TEL, DDD_TEL
    """

    conn = pyodbc.connect(conn_str)
    df = pd.read_sql_query(query, conn)

    conn.close()

    num_linhas = df.shape[0]

    print(df)

    return df["TELEFONE"].tolist(), df["NOME"].tolist(), num_linhas

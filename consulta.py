import pandas as pd
import pyodbc  

def conectar():
    conn_str = 'DRIVER={SQL Server};SERVER=192.168.0.38;DATABASE=Nectar;UID=imaps;PWD=imaps'
    query = """
        SELECT  CONCAT('+55',RTRIM(DDD_TEL),RTRIM(TELEF_TEL)) AS TELEFONE, RTRIM(NOME_DEV) AS NOME
        FROM iMapsNectar_Contratos
        JOIN iMapsNectar_Devedores ON IDDEV_CON = IDDEV_DEV
        JOIN iMapsNectar_OcorrenciasEnvios ON IDCON_AND = IDCON_CON
        JOIN iMapsNectar_Telefones ON IDORI_TEL = IDCON_CON
        JOIN iMapsNectar_Ocorrencias ON IDOCO_OCO = IDOCO_AND
        WHERE IDLOTE_AND = '175966' AND STATU_TEL = 0 AND TPTEL_TEL = 2
        ORDER BY TELEF_TEL, DDD_TEL
    """

    conn = pyodbc.connect(conn_str)
    df = pd.read_sql_query(query, conn)

    conn.close()

    num_linhas = df.shape[0]

    print(df)
    # print(f"Quantidade de linhas: {num_linhas}")

    return df["TELEFONE"].tolist(), df["NOME"].tolist(), num_linhas


conectar()
from app.dao.dao import DAO
from app.models.fornecedor import Cliente
class Fornecedor_DAO(DAO):
    def __init__(self, database):
        super().__init__(database)

    def save(self, fornecedor):
        conexao, cursor = self.conectar()
        try:
            sql =   """
                        INSERT INTO FORNECEDOR
                        (RAZAO_SOCIAL, NOME_FANTASIA, CNPJ, SLA_ATENDIMENTO)
                        VALUES (%s, %s, %s,%s)
                    """
            cursor.execute(sql, (
                fornecedor.razao_social,
                fornecedor.nome_fantasia,
                fornecedor.cnpj,
                fornecedor.sla_atendimento
            ))
            conexao.commit()
            fornecedor.id = cursor.lastrowid
            return fornecedor
        except Exception as e:
            conexao.rollback()
            raise e
        finally:
            self.desconectar(cursor, conexao)
        
    
    def get_all(self):
        conexao, cursor = self.conectar()
        try:
            sql =   """
                        SELECT
                            ID,
                            RAZAO_SOCIAL,
                            NOME_FANTASIA,
                            CNPJ,
                            SLA_ATENDIMENTO
                        FROM
                            FORNECEDOR
                    """
            cursor.execute(sql)
            registros = cursor.fetchall()
            fornecedores = []
            for registro in registros:
                fornecedores.append(
                    Cliente(
                        registro[0],
                        registro[1],
                        registro[2],
                        registro[3],
                        registro[4]
                    )
                )
            return fornecedores
        except Exception as e:
            raise e
        finally:
            self.desconectar(cursor, conexao)
        
    
    def get_by_id(self, id):
        conexao, cursor = self.conectar()
        try:
            sql =   """
                        SELECT
                            ID,
                            RAZAO_SOCIAL,
                            NOME_FANTASIA,
                            CNPJ,
                            SLA_ATENDIMENTO
                        FROM
                            FORNECEDORES
                        WHERE
                            ID = %s
                    """        
            cursor.execute(sql,(id,))
            registro = cursor.fetchone()
            self._database.desconectar(cursor, conexao)
            if registro is None:
                return None
            return Cliente(
                registro[0],
                registro[1],
                registro[2],
                registro[3],
                registro[4]
            )
        except Exception as e:
            raise e
        finally:
            self.desconectar(cursor, conexao)


    def update(self, fornecedor):
        conexao, cursor = self.conectar()
        try:
            sql =   """
                        UPDATE FORNECEDOR SET
                            RAZAO_SOCIAL             = %s,
                            NOME_FANTASIA            = %s,
                            CNPJ                     = %s,
                            SLA_ATENDIMENTO          = %s
                        WHERE
                            ID = %s
                    """
            cursor.execute(sql,(
                                    fornecedor.razao_social,
                                    fornecedor.nome_fantasia,
                                    fornecedor.cnpj,
                                    fornecedor.sla_atendimento
            ))
            conexao.commit()
            sucesso = cursor.rowcount > 0
            self._database.desconectar(cursor, conexao)
            return sucesso
        except Exception as e:
            conexao.rollback()
            raise e
        finally:
            self.desconectar(cursor, conexao)
    
    def delete(self, id):
        conexao, cursor = self.conectar()
        try:
            sql =   """
                        DELETE FROM FORNECEDOR
                        WHERE ID = %s
                    """
            cursor.execute(sql,(id,))
            conexao.commit()
            sucesso = cursor.rowcount > 0
            self._database.desconectar(cursor, conexao)
            return sucesso
        except Exception as e:
            conexao.rollback()
            raise e
        finally:
            self.desconectar(cursor, conexao)
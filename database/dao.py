from database.DB_connect import DBConnect
from model.artista import Artista
class DAO:

    #lista di ruoli
    @staticmethod
    def dropdown():
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor()
        query = """select distinct role from authorship"""
        cursor.execute(query)
        for row in cursor:
            result.append(row[0])
        cursor.close()
        conn.close()
        return result

    #lista di ruoli
    @staticmethod
    def artisti(ruolo):
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)
        query = """select a.name as nome, a.artist_id as id
                    from artists a,authorship au
                    where a.artist_id =au.artist_id and au.role=%s"""
        cursor.execute(query,(ruolo,))
        for row in cursor:
            result.append(Artista(row["nome"],row["id"], 0))
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def pesi():  #quesri che restituisce id->peso    dizionario
        conn = DBConnect.get_connection()
        result = {}
        cursor = conn.cursor(dictionary=True)
        query = """select artist_id as id, count(object_id) as numero
                    from authorship a2
                    group by(artist_id)"""
        cursor.execute(query)
        for row in cursor:
            result[row["id"]]=row["numero"]
        cursor.close()
        conn.close()
        return result


    #restituisce una lista con gli artisti collegati id1->id2
    def collegamenti(ruolo):
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)
        query = """ select distinct a1.artist_id as id1, a2.artist_id as id2
                    from authorship a1, authorship a2 where
                    a1.object_id in (select object_id from objects where curator_approved =1)
                    and a2.object_id in (select object_id from objects where curator_approved =1)
                    and a1.role = %s and a2.role = %s"""
        cursor.execute(query, (ruolo,ruolo))
        for row in cursor:
            result.append((row["id1"],row["id2"]))
        cursor.close()
        conn.close()
        return result

'''

select distinct a1.artist_id as id1, a2.artist_id as id2
from authorship a1, authorship a2 
where a1.object_id in (select object_id from objects where curator_approved =1)
and a2.object_id in (select object_id from objects where curator_approved =1)
and a1.role = "Maker" and a2.role = "Maker" and a1.artist_id != a2.artist_id'''
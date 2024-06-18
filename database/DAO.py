from database.DB_connect import DBConnect


class DAO():
    def __init__(self):
        pass

    @staticmethod
    def getBorghi():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select distinct nwhl.Borough as borghi 
from nyc_wifi_hotspot_locations nwhl """

        cursor.execute(query)

        for row in cursor:
            result.append(row["borghi"])

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getNodi(borgo):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select distinct nwhl.NTACode as nta
from nyc_wifi_hotspot_locations nwhl 
where nwhl.Borough =%s"""

        cursor.execute(query,(borgo,))

        for row in cursor:
            result.append(row["nta"])

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getPeso(nta1,nta2):
        conn = DBConnect.get_connection()

        result = 0

        cursor = conn.cursor(dictionary=True)
        query = """select count(distinct nwhl.SSID) as peso
from nyc_wifi_hotspot_locations nwhl 
where nwhl.NTACode=%s or nwhl.NTACode=%s"""

        cursor.execute(query, (nta1,nta2,))

        for row in cursor:
            result= row["peso"]

        cursor.close()
        conn.close()
        return result


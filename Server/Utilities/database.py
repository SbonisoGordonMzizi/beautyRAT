import sqlite3 as lite


def create_datebase(database_path: str):
    conn = lite.connect(database_path)
    with conn:
        cur = conn.execute("drop table if exists connected_client")
        ddl1 = """create table connected_client ( request_time text not null constraint connected_client_pk primary key,
	             client_address text not null,
	             http_version text not null,
	             request_type text not null,
	             client_agent text not null);"""

        ddl2  = """create unique index connected_client_client_address_uindex
	             on connected_client (client_address);"""

        ddl3 = """create unique index connected_client_request_time_uindex
	             on connected_client (request_time);
                 """
        cur.execute(ddl1)
        cur.execute(ddl2)
        cur.execute(ddl3)

    conn.close()


def save_to_database(database_path:str,req_time:str,c_address:str,http_ver:str,req_type:str,c_agent:str):
    conn = lite.connect(database_path)

    with conn:
        cur = conn.cursor()
        hold = f"INSERT INTO connected_client ( request_time, client_address ,http_version, request_type , client_agent )VALUES(\"{req_time}\",\"{c_address}\",\"{http_ver}\",\"{req_type}\",\"{c_agent}\");"
        r = cur.execute(hold)

    conn.close()

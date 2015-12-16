from app.config import SQL_HOURLY_AGG_PROC, SQL_DAILY_AGG_PROC, SQL_DATA_CLEANUP_PROC
from app.utils.database import database_connection


PROCS = (SQL_HOURLY_AGG_PROC, SQL_DAILY_AGG_PROC, SQL_DATA_CLEANUP_PROC, )


def main():
    db = database_connection()
    cursor = db.cursor()
    for proc in PROCS:
        cursor.callproc(proc)


if __name__ == "__main__":
    main()

import os


DATABASE_URL = os.getenv('THPL_DATABASE_URL', None)
DB_PORT_5432_TCP_ADDR = os.getenv('DB_PORT_5432_TCP_ADDR', None)

if DATABASE_URL is None:
    assert DB_PORT_5432_TCP_ADDR
    DATABASE_URL = 'postgres://postgres@{0}:5432/postgres'.format(DB_PORT_5432_TCP_ADDR)

SQL_HOURLY_AGG_PROC = 'sp_thpl_hourly_agg'
SQL_DAILY_AGG_PROC = 'sp_thpl_daily_agg'
SQL_DATA_CLEANUP_PROC = 'sp_thpl_data_cleanup'

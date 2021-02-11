import snowflake.connector


def handler(event, context):
    SNOW_ACCOUNT = ''
    SNOW_USER = ''
    SNOW_PASS = ''
    WAREHOUSE = ''
    SNOW_DB = ''
    SNOW_SCHEMA = ''
    # connect to snowflake - set ocsp response cache to /tmp, the only place we can write on lambda
    ctx = snowflake.connector.connect(
        user=SNOW_USER,
        password=SNOW_PASS,
        account=SNOW_ACCOUNT,
        warehouse=WAREHOUSE,
        database=SNOW_DB,
        schema=SNOW_SCHEMA,
        ocsp_response_cache_filename="/tmp/ocsp_response_cache"
        )
    cur = ctx.cursor()
    try:
        cur.execute('SELECT "都道府県", "売上" FROM "売上" LIMIT 100;')
        df = cur.fetch_pandas_all()
        print(df.groupby('都道府県').mean())
    finally:
        cur.close()

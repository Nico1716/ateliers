import duckdb
con = duckdb.connect('traffic_data.duckdb')


con.execute("""
CREATE OR REPLACE TABLE traffic_data AS
SELECT * FROM read_csv_auto('traffic_data.csv',
    normalize_names=True
)
""")
result = con.execute("SELECT * FROM traffic_data LIMIT 10").fetchall()
print(result)

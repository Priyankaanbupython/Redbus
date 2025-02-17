engine_string = f"mysql+pymysql://{username}:{password}@{host}:{port}/{database}"
engine = create_engine(engine_string)
 
table_name = "bus_details"
df = pd.read_csv('tenstate.csv')
df.to_sql(table_name, engine,if_exists="replace", index=False)
print("success")

#!python3

import os
import json

import pandas
from sqlalchemy import create_engine

if __name__ == "__main__":
    path = os.getcwd() + "\\" + "dataset" + "\\"

    for dic in [("distribution_centers.csv","dim_distribution"),
                ("employees.csv","dim_employee"),
                ("events.csv","dim_event"),
                ("inventory_items.csv","dim_inventory"),
                ("order_items.csv","fact_orderdetails"),
                ("orders.csv","dim_order"),
                ("products.csv","fact_product"),
                ("users.csv","dim_users")]:
        
        df = pandas.read_csv(path + dic[0])
        engine = create_engine('postgresql://postgres:12345678@localhost:5432/final_project')
        df.to_sql(dic[1], engine, if_exists='replace', index=False)
#!python3

def get_distribtion():
    sql = """
            select * from public.dim_distribution
    """
    return sql

def get_employee():
    sql = """
            select * from public.dim_employee
    """
    return sql

def get_event():
    sql = """
            select * from public.dim_event
    """
    return sql

def get_inventory():
    sql = """
            select * from public.dim_inventory
    """
    return sql

def get_order():
    sql = """
            select * from public.dim_order
    """
    return sql
def get_product():
    sql = """
            select * from public.dim_product
    """
    return sql

def get_users():
    sql = """
            select * from public.dim_users
    """
    return sql

def get_ordersdetails():
    sql = """
            select * from public.fact_orderdetails
    """
    return sql

def list_tables():
    tables = [("distribution",get_distribtion()),
              ("employee",get_employee()),
              ("event",get_event()),
              ("inventory",get_inventory()),
              ("order",get_order()),
              ("product",get_product()),
              ("users",get_users()),
              ("orders",get_ordersdetails())]

    return tables

    # def dwh_fact_orders():
    #     sql = """
    #             select 	
    #             from fact_orderdetails a 

    #     """

    #     return sql
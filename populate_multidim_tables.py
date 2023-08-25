# Data Science
# Vinicius Gutteres
# 2023-08-17 

import mysql.connector;
import pandas;

connection = mysql.connector.connect(
    user = 'root',
    password = 'positivo',
    host = 'localhost',    
    database = 'northwind'
);

connection_multidim1 = mysql.connector.connect(
    user = 'root',
    password = 'positivo',
    host = 'localhost',    
    database = 'multidim1'
);

def populate_multidim_tables(table_name, table_columns, multidim_table) :
    cursor = connection.cursor();
    cursor_multidim1 = connection_multidim1.cursor();

    select_joins = ','.join(table_columns);

    select_query = f"SELECT {select_joins} FROM {table_name};";

    cursor.execute(select_query);

    result = cursor.fetchall();

    prod_df = pandas.DataFrame(result, columns=[table_columns]);

    for i, r in prod_df.iterrows():
        index = i + 1;
  
        columnValue = '';

        for key, value in r.items():
            columnValue += f"{value} ";
        
        columnValue = columnValue.strip();

        insert_query = f"INSERT INTO {multidim_table} value({index}, '{columnValue}')";

        cursor_multidim1.execute(insert_query);
        connection_multidim1.commit();

    print('Success:::::::: ')


# populate_multidim_tables('customers', ['first_name', 'last_name'], 'dim_cliente'); --- dim_cliente
# populate_multidim_tables('products', ['product_name'], 'dim_produto'); --- dim_produto
# populate_multidim_tables('employees', ['first_name', 'last_name'], 'dim_vendedor'); --- dim_vendedor
# populate_multidim_tables('products', ['category'], 'dim_catproduto'); --- dim_catproduto
# populate_multidim_tables('customers', ['city'], 'dim_municipio'); # dim_municipio
# populate_multidim_tables('customers', ['state_province'], 'dim_uf'); # dim_uf
# populate_multidim_tables('customers', ['country_region'], 'dim_regiao'); # dim_regiao

# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "lakehouse": {
# META       "default_lakehouse": "15642f53-3ae0-4eb7-9c62-456b19d76241",
# META       "default_lakehouse_name": "Bronze_WWI",
# META       "default_lakehouse_workspace_id": "b6d7b31c-9af0-427d-b250-c74c5333fabe",
# META       "known_lakehouses": [
# META         {
# META           "id": "15642f53-3ae0-4eb7-9c62-456b19d76241"
# META         }
# META       ]
# META     }
# META   }
# META }

# CELL ********************

# MAGIC %%sql
# MAGIC 
# MAGIC CREATE TABLE IF NOT EXISTS demo_table ( id int ) USING DELTA;
# MAGIC 


# METADATA ********************

# META {
# META   "language": "sparksql",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# MAGIC %%sql
# MAGIC 
# MAGIC SHOW TABLES;

# METADATA ********************

# META {
# META   "language": "sparksql",
# META   "language_group": "synapse_pyspark"
# META }

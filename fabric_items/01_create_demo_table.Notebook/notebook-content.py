# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "lakehouse": {
# META       "default_lakehouse": "d9dc40ac-75ae-4620-8987-f0f523d31e69",
# META       "default_lakehouse_name": "Bronze_WWI",
# META       "default_lakehouse_workspace_id": "28db5efc-14fd-4c15-a74e-994ae1f48847",
# META       "known_lakehouses": [
# META         {
# META           "id": "d9dc40ac-75ae-4620-8987-f0f523d31e69"
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

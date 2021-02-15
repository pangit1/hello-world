# Databricks notebook source
print('Hello world')

# COMMAND ----------

import pandas as pd
d = {'col1': [1, 2], 'col2': [3, 4]}
df = pd.DataFrame(data=d)
df.describe()

# COMMAND ----------


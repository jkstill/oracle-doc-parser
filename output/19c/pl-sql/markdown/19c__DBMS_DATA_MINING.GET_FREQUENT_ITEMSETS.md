---
id: 19c__DBMS_DATA_MINING.GET_FREQUENT_ITEMSETS
name: DBMS_DATA_MINING.GET_FREQUENT_ITEMSETS
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_DATA_MINING
tags: [dbms_data_mining]
source_file: DBMS_DATA_MINING.html
---

# DBMS_DATA_MINING.GET_FREQUENT_ITEMSETS

The GET_FREQUENT_ITEMSETS function returns a set of rows that represent the frequent itemsets from an Association model. Starting from Oracle Database 12 c Release 2, this function is deprecated. See "Model Detail Views" in Oracle Data Mining User’s Guide .

## Syntax

```sql
DBMS_DATA_MINING.get_frequent_itemsets(
      model_name IN VARCHAR2,
      topn IN NUMBER DEFAULT NULL,
      max_itemset_length IN NUMBER DEFAULT NULL,
      partition_name     IN VARCHAR2 DEFAULT NULL)
  RETURN DM_ItemSets PIPELINED;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| model_name | VARCHAR2 | IN | Name of the model in the form [ schema_name .] model_name . If you do not specify a schema, then your own schema is used. |
| topn | NUMBER | IN | When not NULL , return the top n rows ordered by support in descending order |
| max_itemset_length | NUMBER | IN | Maximum length of an item set. |
| partition_name | VARCHAR2 | IN | Specifies a partition in a partitioned model. Note: The partition_name columns applies only when the model is partitioned. |

**Returns:** `DM_ItemSets`

## Usage Notes

For a detailed description of frequent itemsets, consult Oracle Data Mining Concepts . Syntax DBMS_DATA_MINING.get_frequent_itemsets( model_name IN VARCHAR2, topn IN NUMBER DEFAULT NULL, max_itemset_length IN NUMBER DEFAULT NULL, partition_name IN VARCHAR2 DEFAULT NULL) RETURN DM_ItemSets PIPELINED; Parameters Table 47-73 GET_FREQUENT_ITEMSETS Function Parameters Parameter Description model_name Name of the model in the form [ schema_name .] model_name . If you do not specify a schema, then your own schema is used. topn When not NULL , return the top n rows ordered by support in descending order max_itemset_length Maximum length of an item set. partition_name Specifies a partition in a partitioned model. Note: The partition_name columns applies only when the model is partitioned. Note: The partition_name columns applies only when the model is partitioned. Return Values Table 47-74 GET_FREQUENT_ITEMSETS Function Return Values Return Value Description DM_ITEMSETS A set of rows of type DM_ITEMSET . The rows have the following columns: (partition_name VARCHAR2(128) itemsets_id NUMBER, items DM_ITEMS, support NUMBER, number_of_items NUMBER) Note: The partition_name columns applies only when the model is partitioned. The items column returns a nested table of type DM_ITEMS . The rows have type DM_ITEM : (attribute_name VARCHAR2(4000), attribute_subname VARCHAR2(4000), attribute_num_value NUMBER, attribute_str_value VARCHAR2(4000))
---
id: 19c__DBMS_FREQUENT_ITEMSET.FI_TRANSACTIONAL
name: DBMS_FREQUENT_ITEMSET.FI_TRANSACTIONAL
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_FREQUENT_ITEMSET
tags: [dbms_frequent_itemset]
source_file: DBMS_FREQUENT_ITEMSET.html
---

# DBMS_FREQUENT_ITEMSET.FI_TRANSACTIONAL

This procedure counts all frequent itemsets given a cursor for input data which is in ' TRANSACTIONAL ' row format, support threshold, minimum itemset length, maximum itemset length, items to be included, items to be excluded. The result will be a table of rows in form of itemset, support, length, total number of transactions.

## Syntax

```sql
DBMS_FREQUENT_ITEMSET.FI_TRANSACTIONAL (
   tranx_cursor         IN    SYSREFCURSOR,
   support_threshold    IN    NUMBER,
   itemset_length_min   IN    NUMBER,
   itemset_length_max   IN    NUMBER,
   including_items      IN    SYS_REFCURSOR DEFAULT NULL,
   excluding_items      IN    SYS_REFCURSOR DEFAULT NULL)
  RETURN TABLE OF ROW (
     itemset [Nested Table of Item Type DERIVED FROM tranx_cursor],
     support        NUMBER,
     length         NUMBER,
     total_tranx    NUMBER);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| tranx_cursor | SYSREFCURSOR | IN | The cursor parameter that the user will supply when calling the function. It should return two columns in its returning row, the first column being the transaction id, the second column being the item id. The item id must be number or character type (for example, VARCHAR2 (n)). |
| support_threshold | NUMBER | IN | A fraction number of total transaction count. An itemset is termed "frequent" if [the number of transactions it occurs in] divided by [the total number of transactions] exceed the fraction. The parameter must be a NUMBER . |
| itemset_length_min | NUMBER | IN | The minimum length for interested frequent itemset. The parameter must be a NUMBER between 1 and 20, inclusive. |
| itemset_length_max | NUMBER | IN | The maximum length for interested frequent itemset. This parameter must be a NUMBER between 1 and 20, inclusive, and must not be less than itemset_length_min . |
| including_items | SYS_REFCURSOR | IN | A cursor from which a list of items can be fetched. At least one item from the list must appear in frequent itemsets that will be returned. The default is NULL . |
| excluding_items | SYS_REFCURSOR | IN | A cursor from which a list of items can be fetched. No item from the list can appear in frequent itemsets that will returned. The default is NULL . |

**Returns:** `TABLE`

## Usage Notes

In ' TRANSACTIONAL ' row format, each transaction is spread across multiple rows. All the rows of a given transaction have the same transaction id, and each row has a different item id. Combining all of the item ids which share a given transaction id results in a single transaction. Syntax DBMS_FREQUENT_ITEMSET.FI_TRANSACTIONAL ( tranx_cursor IN SYSREFCURSOR, support_threshold IN NUMBER, itemset_length_min IN NUMBER, itemset_length_max IN NUMBER, including_items IN SYS_REFCURSOR DEFAULT NULL, excluding_items IN SYS_REFCURSOR DEFAULT NULL) RETURN TABLE OF ROW ( itemset [Nested Table of Item Type DERIVED FROM tranx_cursor], support NUMBER, length NUMBER, total_tranx NUMBER); Parameters Table 74-4 FI_TRANSACTIONAL Function Parameters Parameter Description tranx_cursor The cursor parameter that the user will supply when calling the function. It should return two columns in its returning row, the first column being the transaction id, the second column being the item id. The item id must be number or character type (for example, VARCHAR2 (n)). support_threshold A fraction number of total transaction count. An itemset is termed "frequent" if [the number of transactions it occurs in] divided by [the total number of transactions] exceed the fraction. The parameter must be a NUMBER . itemset_length_min The minimum length for interested frequent itemset. The parameter must be a NUMBER between 1 and 20, inclusive. itemset_length_max The maximum length for interested frequent itemset. This parameter must be a NUMBER between 1 and 20, inclusive, and must not be less than itemset_length_min . including_items A cursor from which a list of items can be fetched. At least one item from the list must appear in frequent itemsets that will be returned. The default is NULL . excluding_items A cursor from which a list of items can be fetched. No item from the list can appear in frequent itemsets that will returned. The default is NULL . Return Values Table 74-5 FI_TRANSACTIONAL Return Values Parameter Description support The number of transactions in which a frequent itemset occurs. This will be returned as a NUMBER . itemset A collection of items which is computed as frequent itemset. This will be returned as a nested table of item type which is the item column type of the input cursor. length Number of items in a frequent itemset. This will be returned as a NUMBER . total_tranx The total transaction count. This will be returned as a NUMBER , and will be the same for all returned rows, similar to a reporting aggregate. Usage Notes Applications must predefine a nested table type of the input item type and cast the output itemset into this predefined nested table type before further processing, such as loading into a table.
---
id: 19c__DBMS_FREQUENT_ITEMSET.FI_HORIZONTAL
name: DBMS_FREQUENT_ITEMSET.FI_HORIZONTAL
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_FREQUENT_ITEMSET
tags: [dbms_frequent_itemset]
source_file: DBMS_FREQUENT_ITEMSET.html
---

# DBMS_FREQUENT_ITEMSET.FI_HORIZONTAL

The purpose of this table function is to count all frequent itemsets given a cursor for input data which is in ' HORIZONTAL ' row format, support threshold, minimum itemset length, maximum itemset length, items to be included, items to be excluded. The result will be a table of rows in form of itemset, support, length, total transactions counted.

## Syntax

```sql
DBMS_FREQUENT_ITEMSET.FI_HORIZONTAL(
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
| tranx_cursor | SYSREFCURSOR | IN | The cursor parameter that the user will supply when calling the function. There is no limits on the number of returning columns.Each column of cursor represents an item. All columns of the cursor must be of the same datatype. The item id must be number or character type (for example, VARCHAR2 (n)). |
| support_threshold | NUMBER | IN | A fraction number of total transaction count. An itemset is termed "frequent" if [the number of transactions it occurs in] divided by [the total number of transactions] exceed the fraction. The parameter must be a NUMBER . |
| itemset_length_min | NUMBER | IN | The minimum length for interested frequent itemset. The parameter must be a NUMBER between 1 and 20, inclusive. |
| itemset_length_max | NUMBER | IN | The maximum length for interested frequent itemset. This parameter must be a NUMBER between 1 and 20, inclusive, and must not be less than itemset_length_min . |
| including_items | SYS_REFCURSOR | IN | A cursor from which a list of items can be fetched. At least one item from the list must appear in frequent itemsets that are returned. The default is NULL . |
| excluding_items | SYS_REFCURSOR | IN | A cursor from which a list of items can be fetched. No item from the list can appear in frequent itemsets that are returned.The default is NULL . |

**Returns:** `TABLE`

## Usage Notes

In ' HORIZONTAL ' row format, each row contains all of the item ids for a single transaction. Since all of the items come together, no transaction id is necessary. The benefit of this table function is that if an application already has data in horizontal format, the database can skip the step of transforming rows that are in transactional format into horizontal format. Syntax DBMS_FREQUENT_ITEMSET.FI_HORIZONTAL( tranx_cursor IN SYSREFCURSOR, support_threshold IN NUMBER, itemset_length_min IN NUMBER, itemset_length_max IN NUMBER, including_items IN SYS_REFCURSOR DEFAULT NULL, excluding_items IN SYS_REFCURSOR DEFAULT NULL) RETURN TABLE OF ROW ( itemset [Nested Table of Item Type DERIVED FROM tranx_cursor], support NUMBER, length NUMBER, total_tranx NUMBER); Parameters Table 74-2 FI_HORIZONTAL Function Parameters Parameter Description tranx_cursor The cursor parameter that the user will supply when calling the function. There is no limits on the number of returning columns.Each column of cursor represents an item. All columns of the cursor must be of the same datatype. The item id must be number or character type (for example, VARCHAR2 (n)). support_threshold A fraction number of total transaction count. An itemset is termed "frequent" if [the number of transactions it occurs in] divided by [the total number of transactions] exceed the fraction. The parameter must be a NUMBER . itemset_length_min The minimum length for interested frequent itemset. The parameter must be a NUMBER between 1 and 20, inclusive. itemset_length_max The maximum length for interested frequent itemset. This parameter must be a NUMBER between 1 and 20, inclusive, and must not be less than itemset_length_min . including_items A cursor from which a list of items can be fetched. At least one item from the list must appear in frequent itemsets that are returned. The default is NULL . excluding_items A cursor from which a list of items can be fetched. No item from the list can appear in frequent itemsets that are returned.The default is NULL . Return Values Table 74-3 FI_HORIZONTAL Return Values Parameter Description support The number of transactions in which a frequent itemset occurs. This will be returned as a NUMBER . itemset A collection of items which is computed as frequent itemset. This will be returned as a nested table of item type which is the item column type of the input cursor. length Number of items in a frequent itemset. This will be returned as a NUMBER . total_tranx The total transaction count. This will be returned as a NUMBER . Example Suppose you have a table horiz_table_in . horiz_table_in(iid1 VARCHAR2(30), iid2 VARCHAR2(30), iid3 VARCHAR2(30), iid4 VARCHAR2(30), iid5 VARCHAR2(30)); and the data in horiz_table_in looks as follows: ('apple', 'banana', NULL, NULL, NULL) ('apple', 'milk', 'banana', NULL, NULL) ('orange', NULL, NULL, NULL, NULL) Suppose you want to find out what combinations of items is frequent with a given support threshold of 30%, requiring itemset containing at least one of ('apple','banana','orange'), but excluding any of ('milk') in any itemset. You use the following query: CREATE TYPE fi_varchar_nt AS TABLE OF VARCHAR2(30); SELECT CAST(itemset as FI_VARCHAR_NT)itemset, support, length, total_tranx FROM table(DBMS_FREQUENT_ITEMSET.FI_HORIZONTAL( CURSOR(SELECT iid1, iid2, iid3, iid4, iid5 FROM horiz_table_in), 0.3, 2, 5, CURSOR(SELECT * FROM table(FI_VARCHAR_NT ('apple','banana','orange'))), CURSOR(SELECT * FROM table(FI_VARCHAR_NT('milk')))));
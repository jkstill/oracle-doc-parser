---
id: 19c__DBMS_DATA_MINING_TRANSFORM.SET_TRANSFORM
name: DBMS_DATA_MINING_TRANSFORM.SET_TRANSFORM
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_DATA_MINING_TRANSFORM
tags: [dbms_data_mining_transform]
source_file: DBMS_DATA_MINING_TRANSFORM.html
---

# DBMS_DATA_MINING_TRANSFORM.SET_TRANSFORM

This procedure appends the transformation instructions for an attribute to a transformation list.

## Syntax

```sql
DBMS_DATA_MINING_TRANSFORM.SET_TRANSFORM (
          xform_list               IN OUT NOCOPY TRANSFORM_LIST,
          attribute_name           VARCHAR2,
          attribute_subname        VARCHAR2,
          expression               VARCHAR2,
          reverse_expression       VARCHAR2,
          attribute_spec           VARCHAR2 DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| xform_list | NOCOPY | IN OUT | A transformation list. See Table 48-1 for a description of the TRANSFORM_LIST object type. |
| attribute_name | VARCHAR2 | IN | Name of the attribute to be transformed |
| attribute_subname | VARCHAR2 | IN | Name of the nested attribute if attribute_name is a nested column, otherwise NULL . |
| expression | VARCHAR2 | IN | A SQL expression that specifies the transformation of the attribute. |
| reverse_expression | VARCHAR2 | IN | A SQL expression that reverses the transformation for readability in model details and in the target of a supervised model (if the attribute is a target) |
| attribute_spec | VARCHAR2 | IN | One or more keywords that identify special treatment for the attribute during model build. Values are: NOPREP — When ADP is on, prevents automatic transformation of the attribute. If ADP is not on, this value has no effect. TEXT — Causes the attribute to be treated as unstructured text data FORCE_IN — Forces the inclusion of the attribute in the model build. Applies only to GLM models with feature selection enabled ( ftr_selection_enable = yes). Feature selection is disabled by default. If the model is not using GLM with feature selection, this value has no effect. See "Specifying Transformation Instructions for an Attribute" in Oracle Data Mining User's Guide for more information about attribute_spec . |

## Usage Notes

Syntax DBMS_DATA_MINING_TRANSFORM.SET_TRANSFORM ( xform_list IN OUT NOCOPY TRANSFORM_LIST, attribute_name VARCHAR2, attribute_subname VARCHAR2, expression VARCHAR2, reverse_expression VARCHAR2, attribute_spec VARCHAR2 DEFAULT NULL); Parameters Table 48-33 SET_TRANSFORM Procedure Parameters Parameter Description xform_list A transformation list. See Table 48-1 for a description of the TRANSFORM_LIST object type. attribute_name Name of the attribute to be transformed attribute_subname Name of the nested attribute if attribute_name is a nested column, otherwise NULL . expression A SQL expression that specifies the transformation of the attribute. reverse_expression A SQL expression that reverses the transformation for readability in model details and in the target of a supervised model (if the attribute is a target) attribute_spec One or more keywords that identify special treatment for the attribute during model build. Values are: NOPREP — When ADP is on, prevents automatic transformation of the attribute. If ADP is not on, this value has no effect. TEXT — Causes the attribute to be treated as unstructured text data FORCE_IN — Forces the inclusion of the attribute in the model build. Applies only to GLM models with feature selection enabled ( ftr_selection_enable = yes). Feature selection is disabled by default. If the model is not using GLM with feature selection, this value has no effect. See "Specifying Transformation Instructions for an Attribute" in Oracle Data Mining User's Guide for more information about attribute_spec . Usage Notes See the following relevant sections in " Operational Notes " : About Transformation Lists Nested Data Transformations As shown in the following example, you can eliminate an attribute by specifying a null transformation expression and reverse expression. You can also use the STACK interface to remove a column ( CREATE_COL_REM Procedure and STACK_COL_REM Procedure ).
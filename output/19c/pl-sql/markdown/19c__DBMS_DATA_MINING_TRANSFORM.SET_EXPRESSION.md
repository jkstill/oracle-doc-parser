---
id: 19c__DBMS_DATA_MINING_TRANSFORM.SET_EXPRESSION
name: DBMS_DATA_MINING_TRANSFORM.SET_EXPRESSION
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_DATA_MINING_TRANSFORM
tags: [dbms_data_mining_transform]
source_file: DBMS_DATA_MINING_TRANSFORM.html
---

# DBMS_DATA_MINING_TRANSFORM.SET_EXPRESSION

This procedure appends a row to a VARCHAR2 array that stores a SQL expression.

## Syntax

```sql
DBMS_DATA_MINING_TRANSFORM.SET_EXPRESSION (
           expression    IN OUT NOCOPY EXPRESSION_REC,
           chunk                       VARCHAR2 DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| expression | NOCOPY | IN OUT | An expression record ( EXPRESSION_REC ) that specifies a transformation expression or a reverse transformation expression for an attribute. Each expression record includes a VARCHAR2 array and index fields for specifying upper and lower boundaries within the array. There are two EXPRESSION_REC fields within a transformation record ( TRANSFORM_REC ): one for the transformation expression; the other for the reverse transformation expression. See Table 48-1 for a description of the EXPRESSION_REC type. |
| chunk | VARCHAR2 | IN | A VARCHAR2 chunk (row) to be appended to expression . |

## Usage Notes

The array can be used for specifying a transformation expression that is too long to be used with the SET_TRANSFORM Procedure . The GET_EXPRESSION Function returns a row in the array. When you use SET_EXPRESSION to build a transformation expression, you must build a corresponding reverse transformation expression, create a transformation record, and add the transformation record to a transformation list. Syntax DBMS_DATA_MINING_TRANSFORM.SET_EXPRESSION ( expression IN OUT NOCOPY EXPRESSION_REC, chunk VARCHAR2 DEFAULT NULL); Parameters Table 48-32 SET_EXPRESSION Procedure Parameters Parameter Description expression An expression record ( EXPRESSION_REC ) that specifies a transformation expression or a reverse transformation expression for an attribute. Each expression record includes a VARCHAR2 array and index fields for specifying upper and lower boundaries within the array. There are two EXPRESSION_REC fields within a transformation record ( TRANSFORM_REC ): one for the transformation expression; the other for the reverse transformation expression. See Table 48-1 for a description of the EXPRESSION_REC type. chunk A VARCHAR2 chunk (row) to be appended to expression . Notes You can pass NULL in the chunk argument to SET_EXPRESSION to clear the previous chunk. The default value of chunk is NULL . See " About Transformation Lists " . See " Operational Notes " . Examples In this example, two calls to SET_EXPRESSION construct a transformation expression and two calls construct the reverse transformation. Note: This example is for illustration purposes only. It shows how SET_EXPRESSION appends the text provided in chunk to the text that already exists in expression . The SET_EXPRESSION procedure is meant for constructing very long transformation expressions that cannot be specified in a VARCHAR2 argument to SET_TRANSFORM . Similarly while transformation lists are intended for embedding in a model, the transformation list v_xlst is shown in an external view for illustration purposes. CREATE OR REPLACE VIEW mining_data AS SELECT cust_id, cust_year_of_birth, cust_postal_code, cust_credit_limit FROM sh.customers; DECLARE v_expr dbms_data_mining_transform.EXPRESSION_REC; v_rexp dbms_data_mining_transform.EXPRESSION_REC; v_xrec dbms_data_mining_transform.TRANSFORM_REC; v_xlst dbms_data_mining_transform.TRANSFORM_LIST := dbms_data_mining_transform.TRANSFORM_LIST(NULL); BEGIN dbms_data_mining_transform.SET_EXPRESSION( EXPRESSION => v_expr, CHUNK => '("CUST_YEAR_OF_BIRTH"-1910)'); dbms_data_mining_transform.SET_EXPRESSION( EXPRESSION => v_expr, CHUNK => '/77'); dbms_data_mining_transform.SET_EXPRESSION( EXPRESSION => v_rexp, CHUNK => '"CUST_YEAR_OF_BIRTH"*77'); dbms_data_mining_transform.SET_EXPRESSION( EXPRESSION => v_rexp, CHUNK => '+1910'); v_xrec := null; v_xrec.attribute_name := 'CUST_YEAR_OF_BIRTH'; v_xrec.expression := v_expr; v_xrec.reverse_expression := v_rexp; v_xlst.TRIM; v_xlst.extend(1); v_xlst(1) := v_xrec; dbms_data_mining_transform.XFORM_STACK ( xform_list => v_xlst, data_table_name => 'mining_data', xform_view_name => 'v_xlst_view'); dbms_output.put_line('===='); FOR i IN 1..v_xlst.count LOOP dbms_output.put_line('ATTR: '||v_xlst(i).attribute_name); dbms_output.put_line('SUBN: '||v_xlst(i).attribute_subname); FOR j IN v_xlst(i).expression.lb..v_xlst(i).expression.ub LOOP dbms_output.put_line('EXPR: '||v_xlst(i).expression.lstmt(j)); END LOOP; FOR j IN v_xlst(i).reverse_expression.lb.. v_xlst(i).reverse_expression.ub LOOP dbms_output.put_line('REXP: '||v_xlst(i).reverse_expression.lstmt(j)); END LOOP; dbms_output.put_line('===='); END LOOP; END; / ==== ATTR: CUST_YEAR_OF_BIRTH SUBN: EXPR: ("CUST_YEAR_OF_BIRTH"-1910) EXPR: /77 REXP: "CUST_YEAR_OF_BIRTH"*77 REXP: +1910 ====
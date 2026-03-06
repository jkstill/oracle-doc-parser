---
id: 19c__DBMS_DATA_MINING.REGISTER_ALGORITHM
name: DBMS_DATA_MINING.REGISTER_ALGORITHM
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_DATA_MINING
tags: [dbms_data_mining]
source_file: DBMS_DATA_MINING.html
---

# DBMS_DATA_MINING.REGISTER_ALGORITHM

User can register a new algorithm by providing algorithm name, mining function, and all other algorithm metadata to this function.

## Syntax

```sql
DBMS_DATA_MINING.REGISTER_ALGORITHM (
                     algorithm_name           IN VARCHAR2,
                     algorithm_metadata       IN CLOB,
                     algorithm_description    IN VARCHAR2 DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| algorithm_name | VARCHAR2 | IN | Name of the algorithm. |
| algorithm_metadata | CLOB | IN | Metadata of the algorithm. |
| algorithm_description | VARCHAR2 | IN | Description of the algorithm. |

## Usage Notes

Syntax DBMS_DATA_MINING.REGISTER_ALGORITHM ( algorithm_name IN VARCHAR2, algorithm_metadata IN CLOB, algorithm_description IN VARCHAR2 DEFAULT NULL); Parameters Table 47-110 REGISTER_ALGORITHM Procedure Parameters Parameter Description algorithm_name Name of the algorithm. algorithm_metadata Metadata of the algorithm. algorithm_description Description of the algorithm. Usage Notes The registration procedure performs the following: Checks whether algorithm_metadata has correct JSON syntax. Checks whether the input JSON object follows the predefined JSON schema. Checks whether current user has RQADMIN privilege. Checks duplicate algorithms such that the same algorithm is not registered twice. Checks for missing entries. For example, algorithm name, algorithm type, metadata, and build function. Register Algorithms After the JSON Object Is Created SQL users can register new algorithms by following the given procedure: Create a JSON object following JSON schema and pass it to REGISTER_ALGORITHM procedure. BEGIN DBMS_DATA_MINING.register_algorithm( algorithm_name => 't1', algorithm_metadata => '{"function_language" : "R", "mining_function" : { "mining_function_name" : "CLASSIFICATION", "build_function" : {"function_body": "function(dat, formula, family) { set.seed(1234); mod <- glm(formula = formula, data=dat, family=eval(parse(text=family))); mod}"}, "score_function" : {"function_body": "function(mod, dat) { res <- predict(mod, newdata = dat, type=''response''); res2=data.frame(1-res, res); res2}"}} }', algorithm_description => 't1'); END; /
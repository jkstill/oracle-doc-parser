---
id: 19c__DBMS_PREDICTIVE_ANALYTICS.PROFILE
name: DBMS_PREDICTIVE_ANALYTICS.PROFILE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_PREDICTIVE_ANALYTICS
tags: [dbms_predictive_analytics]
source_file: DBMS_PREDICTIVE_ANALYTICS.html
---

# DBMS_PREDICTIVE_ANALYTICS.PROFILE

The PROFILE procedure generates rules that describe the cases (records) from the input data.

## Syntax

```sql
DBMS_PREDICTIVE_ANALYTICS.PROFILE (
     data_table_name           IN VARCHAR2,
     target_column_name        IN VARCHAR2,
     result_table_name         IN VARCHAR2,
     data_schema_name          IN VARCHAR2 DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| data_table_name | VARCHAR2 | IN | Name of the table containing the data to be analyzed. |
| target_column_name | VARCHAR2 | IN | Name of the target column. |
| result_table_name | VARCHAR2 | IN | Name of the table where the results will be saved. |
| data_schema_name | VARCHAR2 | IN | Name of the schema where the input table or view resides and where the result table is created. Default: the current schema. |

## Usage Notes

For example, if a target column CHURN has values 'Yes' and 'No', PROFILE generates a set of rules describing the expected outcomes. Each profile includes a rule, record count, and a score distribution. The input data must contain some cases where the target value is known (not NULL ). These cases are used by the procedure to build a model that calculates the rules. Note: PROFILE does not support nested types or dates. Data requirements for Oracle Data Mining are described in Oracle Data Mining User's Guide. The PROFILE procedure creates a result table that specifies rules (profiles) and their corresponding target values. The result table is described in the Usage Notes. Note: PROFILE does not support nested types or dates. Data requirements for Oracle Data Mining are described in Oracle Data Mining User's Guide. Syntax DBMS_PREDICTIVE_ANALYTICS.PROFILE ( data_table_name IN VARCHAR2, target_column_name IN VARCHAR2, result_table_name IN VARCHAR2, data_schema_name IN VARCHAR2 DEFAULT NULL); Parameters Table 129-6 PROFILE Procedure Parameters Parameter Description data_table_name Name of the table containing the data to be analyzed. target_column_name Name of the target column. result_table_name Name of the table where the results will be saved. data_schema_name Name of the schema where the input table or view resides and where the result table is created. Default: the current schema. Usage Notes The PROFILE procedure creates a result table with the columns described in Table 129-7 . Table 129-7 PROFILE Procedure Result Table Column Name Datatype Description PROFILE_ID NUMBER A unique identifier for this profile (rule). RECORD_COUNT NUMBER The number of records described by the profile. DESCRIPTION SYS.XMLTYPE The profile rule. See " XML Schema for Profile Rules " . XML Schema for Profile Rules The DESCRIPTION column of the result table contains XML that conforms to the following XSD: <xs:element name="SimpleRule"> <xs:complexType> <xs:sequence> <xs:group ref="PREDICATE"/> <xs:element ref="ScoreDistribution" minOccurs="0" maxOccurs="unbounded"/> </xs:sequence> <xs:attribute name="id" type="xs:string" use="optional"/> <xs:attribute name="score" type="xs:string" use="required"/> <xs:attribute name="recordCount" type="NUMBER" use="optional"/> </xs:complexType> </xs:element>
---
id: 19c__DBA_ADVISOR_RATIONALE
name: DBA_ADVISOR_RATIONALE
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dba]
source_file: DBA_ADVISOR_RATIONALE.html
---

# DBA_ADVISOR_RATIONALE

DBA_ADVISOR_RATIONALE displays information about the rationales for all recommendations in the database.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| OWNER | VARCHAR2(128) | Owner of the task |
| TASK_ID | NUMBER | Identifier of the task |
| TASK_NAME | VARCHAR2(128) | Name of the task |
| EXECUTION_NAME | VARCHAR2(128) | The name of the task execution with which this entry (row) is associated |
| REC_ID | NUMBER | Recommendation associated with the rationale |
| RATIONALE_ID | NUMBER | Unique identifier for the rationale |
| IMPACT_TYPE | VARCHAR2(4000) | Impact on the system due to the problem described in the rationale. The impact can be described in terms of time, cost, or % degradation. |
| IMPACT | NUMBER | Calculated impact value |
| MESSAGE | VARCHAR2(4000) | Message containing an overview of the rationale |
| OBJECT_ID | NUMBER | Identifier of an object specified in the DBA_ADVISOR_OBJECTS view |
| TYPE | VARCHAR2(30) | Type of the rationale; defines what data exists in the attribute columns and how to interpret it: TEXT - Text sentence for descriptive messages. The ATTR1 column contains the text. CHART - Chart containing data to be displayed. The ATTR1 column contains the data. |
| ATTR1 | VARCHAR2(4000) | Parameters defining the rationale |
| ATTR2 | VARCHAR2(4000) | Parameters defining the rationale |
| ATTR3 | VARCHAR2(4000) | Parameters defining the rationale |
| ATTR4 | VARCHAR2(4000) | Parameters defining the rationale |
| ATTR5 | CLOB | Parameters defining the rationale |

## Usage Notes

Related View USER_ADVISOR_RATIONALE displays information about the rationales for the recommendations owned by the current user. This view does not display the OWNER column. See Also: " USER_ADVISOR_RATIONALE " See Also: " USER_ADVISOR_RATIONALE "
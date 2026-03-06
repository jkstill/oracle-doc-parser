---
id: 19c__ALL_TAB_HISTOGRAMS
name: ALL_TAB_HISTOGRAMS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [all]
source_file: ALL_TAB_HISTOGRAMS.html
---

# ALL_TAB_HISTOGRAMS

ALL_TAB_HISTOGRAMS describes histograms on tables and views accessible to the current user.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| OWNER | VARCHAR2(128) | Owner of the table |
| TABLE_NAME | VARCHAR2(128) | Name of the table |
| COLUMN_NAME | VARCHAR2(4000) | Column name or attribute of the object type column |
| ENDPOINT_NUMBER | NUMBER | Histogram bucket number |
| ENDPOINT_VALUE | NUMBER | Normalized endpoint value for this bucket |
| ENDPOINT_ACTUAL_VALUE | VARCHAR2(4000) | Actual (not normalized) string value of the endpoint for this bucket |
| ENDPOINT_ACTUAL_VALUE_RAW | RAW(1000) | Endpoint actual value in raw format |
| ENDPOINT_REPEAT_COUNT | NUMBER | Frequency of the endpoint (applies only to hybrid histograms, and is set to 0 for other histogram types) |
| SCOPE | VARCHAR2(7) | The value is SHARED for statistics gathered on any table other than global temporary tables. For a global tempoary table, the possible values are: SESSION - Indicates that the statistics are session-specific SHARED - Indicates that the statistics are shared across all sessions See Oracle Database PL/SQL Packages and Types Reference for information about using the GLOBAL_TEMP_TABLE_STATS preference of the DBMS_STATS package to control whether to gather session or shared statistics for global temporary tables. |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content The ALL_TAB_HISTOGRAMS view may contain a one-bucket histogram, which in fact signifies "No histogram" to the Oracle Database software. Therefore, it should not be queried to indicate the presence or absence of a histogram on a particular column. Instead, query the value of column HISTOGRAM in the ALL_TAB_COL_STATISTICS view. Related Views DBA_TAB_HISTOGRAMS describes histograms on all tables and views in the database. USER_TAB_HISTOGRAMS describes histograms on all tables and views owned by the current user. This view does not display the OWNER column. Note: These views are populated only if you collect statistics on the table using the DBMS_STATS package. For more information, see Oracle Database PL/SQL Packages and Types Reference . Note: These views are populated only if you collect statistics on the table using the DBMS_STATS package. For more information, see Oracle Database PL/SQL Packages and Types Reference .
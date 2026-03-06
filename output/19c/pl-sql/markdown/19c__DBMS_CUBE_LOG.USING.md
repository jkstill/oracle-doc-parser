---
id: 19c__DBMS_CUBE_LOG.USING
name: DBMS_CUBE_LOG.USING
object_type: plsql_subprogram
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_CUBE_LOG
tags: [dbms_cube_log]
source_file: DBMS_CUBE_LOG.html
---

# DBMS_CUBE_LOG.USING

DBMS_CUBE_LOG manages several logs that enable you to track the progress of long running processes, then use the results to profile performance characteristics.

## Syntax

```sql
EXECUTE dbms_cube_log.table_create(dbms_cube_log.type_build);
```

## Usage Notes

They provide information to help you diagnose and remedy problems that may occur during development and maintenance of a cube, such as hierarchies that are improperly structured in the relational source tables, records that fail to load, or data refreshes that take too long to complete. They also help diagnose performance problems in querying cubes. Analytic Workspace Manager creates the logs automatically using the default names and types. It also disables the logs when Analytic Workspace Manager is closed. To use the same logs outside of Analytic Workspace Manager, you must first enable them. Alternatively, you can create and manage different logs for use outside of Analytic Workspace Manager. This section contains the following topics: Logging Types Logging Targets Verbosity Levels Security Model Creating Cube Logs Cube Build Log Cube Dimension Compile Log Cube Operations Log Cube Rejected Records Log The logs and their contents are described later in this topic. Cube Build Log Cube Dimension Compile Log Cube Operations Log Cube Rejected Records Log DBMS_CUBE_LOG provides functions that return the binary integer for each log type. You can produce more readable code by using these functions instead of integers for the argument values of other DBMS_CUBE_LOG procedures and functions. Refer to these descriptions: TYPE_BUILD Function TYPE_DIMENSION_COMPILE Function TYPE_OPERATIONS Function TYPE_REJECTED_RECORDS Function These are the available targets: Disk file LOB Database table Trace file See ENABLE Procedure for more information about creating multiple targets. DBMS_CUBE_LOG provides functions that return the binary integer for each target type. You can produce more readable code by using these functions instead of integers for the argument values of other DBMS_CUBE_LOG procedures and functions. Refer to these descriptions: TARGET_FILE Function TARGET_LOB Function TARGET_TABLE Function TARGET_TRACE Function LOWEST : Logs the status of each command used to build the cube dimensions and cubes, the use of slave processes, and summary records. This is the basic logging level. LOW : Logs messages from the OLAP engine, such as start and finish records for SQL Import, Aggregate, and Update. MEDIUM : Logs messages at the level used by Analytic Workspace Manager. HIGH : Logs messages that provide tuning information, such as composite lengths, partitioning details, object sizes, and aggregation work lists. This level is intended for use by Oracle Field Services. HIGHEST : Logs debugging messages and other information typically sent to a trace file. This level is intended for use by Oracle Support Services. DBMS_CUBE_LOG provides functions that return the binary integer for each verbosity level. You can produce more readable code by using these functions instead of integers for the argument values of other DBMS_CUBE_LOG procedures and functions. Refer to these descriptions: LEVEL_LOWEST Function LEVEL_LOW Function LEVEL_MEDIUM Function LEVEL_HIGH Function LEVEL_HIGHEST Function To create a Cube Build log: Execute the TABLE_CREATE procedure.

## Storage / segments

### Query segments larger than 1GB with their tablespace

```bash
./oracle-rag ask --ollama-url http://lestrade:11434 --model qwen2.5:14b \
  "show all segments larger than 1GB with their tablespace"
```

### Results

[hybrid vector+FTS5 search]
[ollama/qwen2.5:14b @ http://lestrade:11434]
To show all segments larger than 1GB with their tablespace, you can use the `DBA_SEGMENTS` view. The query will filter on the `BYTES` column to find segments that are greater than 1GB (which is equivalent to 1073741824 bytes).

Here's the SQL query:

```sql
SELECT 
    SEGMENT_NAME, 
    TABLESPACE_NAME
FROM 
    DBA_SEGMENTS
WHERE 
    BYTES > 1073741824;
```

This query selects the `SEGMENT_NAME` and `TABLESPACE_NAME` columns from the `DBA_SEGMENTS` view where the size of the segment (`BYTES`) is larger than 1GB.

## Locking

### Query which sessions are blocking other sessions

```bash
./oracle-rag ask --ollama-url http://lestrade:11434 --model qwen2.5:14b \
  "show which sessions are blocking other sessions"
```

### Results

[hybrid vector+FTS5 search]
[ollama/qwen2.5:14b @ http://lestrade:11434]
To show which sessions are blocking other sessions using only the provided Oracle documentation context, we need to join several views together that provide information on both the blocker and blocked session states. The specific views relevant for this query include `V$SESSION`, `DBA_BLOCKERS`, and `V$SESSION_BLOCKERS`.

Here's a SQL query based on the columns provided:

```sql
SELECT b.holding_session AS BLOCKING_SID,
       s1.sid AS BLOCKED_SID,
       s2.username AS HOLDER_USERNAME, 
       s1.username AS BLOCKED_USERNAME,
       s1.status AS BLOCKED_STATUS,
       s2.serial# AS HOLDER_SERIAL_NUMBER,
       s1.serial# AS BLOCKED_SERIAL_NUMBER
FROM dba_blockers b
JOIN v$session s1 ON b.holding_session = s1.sid AND (s1.con_id = 0 OR s1.con_id = b.con_id)
JOIN v$session s2 ON s2.sid = b.holding_session AND (s2.con_id = 0 OR s2.con_id = b.con_id);
```

This SQL query does the following:
- Joins `DBA_BLOCKERS` to `V$SESSION` twice, once for the blocking session and once for the blocked session.
- Filters sessions by container ID if necessary to handle multitenant environments correctly.

Ensure you have appropriate privileges and are querying from an environment where these views are accessible. Adjustments might be required based on your specific database version and setup.

## AWR / performance history

### Query historical wait event data from AWR

```bash
./oracle-rag ask --ollama-url http://lestrade:11434 --model qwen2.5:14b \
  "query historical wait event data from AWR"
```

### Results

[hybrid vector+FTS5 search]
[ollama/qwen2.5:14b @ http://lestrade:11434]
To query historical wait event data from the Automatic Workload Repository (AWR) using the provided documentation context, you can utilize views such as `DBA_HIST_WAITCLASSMET_HISTORY`, `DBA_HIST_EVENT_NAME`, and `DBA_HIST_CON_SYSTEM_EVENT`.

Here's an example SQL query that retrieves historical wait event data:

```sql
SELECT 
    e.SNAP_ID,
    e.DBID,
    e.INSTANCE_NUMBER,
    en.EVENT_NAME,  
    e.WAIT_CLASS,
    e.TOTAL_WAITS,
    e.TIME_WAITED_MICRO,
    e.CON_DBID,
    e.CON_ID
FROM 
    DBA_HIST_CON_SYSTEM_EVENT e
JOIN 
    DBA_HIST_EVENT_NAME en ON e.EVENT_ID = en.EVENT_ID AND e.DBID = en.DBID
WHERE
    e.SNAP_ID BETWEEN <start_snap_id> AND <end_snap_id>
ORDER BY
    e.SNAP_ID, e.INSTANCE_NUMBER;
```

This query joins the `DBA_HIST_CON_SYSTEM_EVENT` and `DBA_HIST_EVENT_NAME` views to retrieve detailed wait event data for a specified snapshot range. The `<start_snap_id>` and `<end_snap_id>` placeholders should be replaced with actual numeric values corresponding to specific snapshots.

If you need more granular or different aspects of the historical wait events, further customization might include joining additional relevant views such as `DBA_HIST_WAITCLASSMET_HISTORY` based on requirements for detailed event classes or other metadata.

# PL/SQL task

### Query to gather statistics for all tables in a schema

```bash
./oracle-rag ask --ollama-url http://lestrade:11434 --model qwen2.5:14b \
  --task plsql \
  "gather statistics for all tables in a schema"
```

### Results

[hybrid vector+FTS5 search]
[ollama/qwen2.5:14b @ http://lestrade:11434]
Based on the provided documentation for Oracle's DBMS_STATS package, here is a PL/SQL code block that gathers statistics for all tables in a specific schema:

```sql
BEGIN
    -- Replace 'your_schema' with the name of your target schema.
    DBMS_STATS.GATHER_SCHEMA_STATS (
        ownname          => 'your_schema',
        estimate_percent => DBMS_STATS.AUTO_SAMPLE_SIZE,
        method_opt       => 'FOR ALL COLUMNS SIZE AUTO',
        cascade          => TRUE,  -- Gather index statistics as well
        no_invalidate    => FALSE  -- Invalidate dependent cursors immediately
    );
END;
/
```

This block uses the `DBMS_STATS.GATHER_SCHEMA_STATS` procedure to gather statistics for all tables in a specified schema. The parameters are set according to best practices and common usage:

- `ownname`: Specifies the target schema.
- `estimate_percent`: Uses `DBMS_STATS.AUTO_SAMPLE_SIZE` to let Oracle automatically determine an appropriate sample size.
- `method_opt`: Collects histograms on columns where necessary, based on data distribution and workload.
- `cascade`: Includes gathering statistics for indexes as well.
- `no_invalidate`: Set to `FALSE`, meaning dependent cursors will be invalidated immediately when new statistics are gathered.

Replace `'your_schema'` with the name of your target schema.


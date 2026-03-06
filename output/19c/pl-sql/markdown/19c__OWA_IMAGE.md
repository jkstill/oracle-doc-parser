---
id: 19c__OWA_IMAGE
name: OWA_IMAGE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: OWA_IMAGE
tags: [owa_image]
source_file: OWA_IMAGE.html
---

# OWA_IMAGE

This example shows use of OWA_IMAGE .

## Syntax

```sql
CREATE OR REPLACE PROCEDURE process_image
    (my_img in OWA_IMAGE.POINT)
    AS
    x integer := OWA_IMAGE.GET_X(my_img);
    y integer := OWA_IMAGE.GET_Y(my_img);
BEGIN
    /* process the coordinate */
END
```

## Usage Notes

CREATE OR REPLACE PROCEDURE process_image (my_img in OWA_IMAGE.POINT) AS x integer := OWA_IMAGE.GET_X(my_img); y integer := OWA_IMAGE.GET_Y(my_img); BEGIN /* process the coordinate */ END
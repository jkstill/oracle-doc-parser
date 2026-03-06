---
id: 19c__UTL_NLA.LAPACK_GTSV
name: UTL_NLA.LAPACK_GTSV
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: UTL_NLA
tags: [utl_nla]
source_file: UTL_NLA.html
---

# UTL_NLA.LAPACK_GTSV

This procedure solves the equation a * x = b , where a is an n by n tridiagonal matrix, by Gaussian elimination with partial pivoting.

## Syntax

```sql
UTL_NLA.LAPACK_GTSV (
   n      IN      POSITIVEN,
   nrhs   IN      POSITIVEN,
   dl     IN OUT  UTL_NLA_ARRAY_DBL,
   d      IN OUT  UTL_NLA_ARRAY_DBL,
   du     IN OUT  UTL_NLA_ARRAY_DBL,
   b      IN OUT  UTL_NLA_ARRAY_DBL,
   ldb    IN      POSITIVEN,
   info      OUT  INTEGER,
   pack   IN      flag DEFAULT 'C');
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| n | POSITIVEN | IN | The order of the matrix a . n >= 0 |
| nrhs | POSITIVEN | IN | The number of right-hand sides, which is the number of columns of the matrix b . nrhs >= 0 . |
| dl | UTL_NLA_ARRAY_DBL | IN OUT | UTL_NLA_ARRAY_FLT / DBL, DIMENSION (n-1) . On entry, dl must contain the (n-1) sub-diagonal elements of a . On exit, dl is overwritten by the (n-2) elements of the second super-diagonal of the upper triangular matrix U from the LU factorization of a , in dl(1), ..., dl(n-2) . |
| d | UTL_NLA_ARRAY_DBL | IN OUT | UTL_NLA_ARRAY_FLT / DBL, DIMENSION (n) . On entry, d must contain the diagonal elements of a . On exit, d is overwritten by the n diagonal elements of U . |
| du | UTL_NLA_ARRAY_DBL | IN OUT | UTL_NLA_ARRAY_FLT / DBL, DIMENSION (n-1) . On entry, du must contain the (n-1) super-diagonal elements of a . On exit, du is overwritten by the (n-1) elements of the first super-diagonal of U . |
| b | UTL_NLA_ARRAY_DBL | IN OUT | UTL_NLA_ARRAY_FLT / DBL, DIMENSION (LDB, nrhs) . On entry, the n by nrhs matrix of right hand side matrix b . On exit, if info = 0 , the n by nrhs solution matrix X . |
| ldb | POSITIVEN | IN | The leading dimension of the array b. ldb >= max (1, n) |
| info | INTEGER | OUT | = 0 : successful exit < 0 : if info = -i , the i -th argument had an illegal value > 0 : if info = i , U(i,i) is exactly zero, and the solution has not been computed. The factorization has not been completed unless i = n . |
| pack | flag | IN | (Optional) Flags the packing of the matrices: ' C ': column-major (default) ' R ': row-major |

## Usage Notes

Note that the equation a'*x = b may be solved by interchanging the order of the arguments du and dl . See Also: LAPACK Driver Routines (Linear Equations) Subprograms for other subprograms in this group See Also: LAPACK Driver Routines (Linear Equations) Subprograms for other subprograms in this group Syntax UTL_NLA.LAPACK_GTSV ( n IN POSITIVEN, nrhs IN POSITIVEN, dl IN OUT UTL_NLA_ARRAY_DBL, d IN OUT UTL_NLA_ARRAY_DBL, du IN OUT UTL_NLA_ARRAY_DBL, b IN OUT UTL_NLA_ARRAY_DBL, ldb IN POSITIVEN, info OUT INTEGER, pack IN flag DEFAULT 'C'); UTL_NLA.LAPACK_GTSV ( n IN POSITIVEN, nrhs IN POSITIVEN, dl IN OUT UTL_NLA_ARRAY_FLT, d IN OUT UTL_NLA_ARRAY_FLT, du IN OUT UTL_NLA_ARRAY_FLT, b IN OUT UTL_NLA_ARRAY_FLT, ldb IN POSITIVEN, info OUT INTEGER, pack IN flag DEFAULT 'C'); Parameters Table 271-46 LAPACK_GTSV Procedure Parameters Parameter Description n The order of the matrix a . n >= 0 nrhs The number of right-hand sides, which is the number of columns of the matrix b . nrhs >= 0 . dl UTL_NLA_ARRAY_FLT / DBL, DIMENSION (n-1) . On entry, dl must contain the (n-1) sub-diagonal elements of a . On exit, dl is overwritten by the (n-2) elements of the second super-diagonal of the upper triangular matrix U from the LU factorization of a , in dl(1), ..., dl(n-2) . d UTL_NLA_ARRAY_FLT / DBL, DIMENSION (n) . On entry, d must contain the diagonal elements of a . On exit, d is overwritten by the n diagonal elements of U . du UTL_NLA_ARRAY_FLT / DBL, DIMENSION (n-1) . On entry, du must contain the (n-1) super-diagonal elements of a . On exit, du is overwritten by the (n-1) elements of the first super-diagonal of U . b UTL_NLA_ARRAY_FLT / DBL, DIMENSION (LDB, nrhs) . On entry, the n by nrhs matrix of right hand side matrix b . On exit, if info = 0 , the n by nrhs solution matrix X . ldb The leading dimension of the array b. ldb >= max (1, n) info = 0 : successful exit < 0 : if info = -i , the i -th argument had an illegal value > 0 : if info = i , U(i,i) is exactly zero, and the solution has not been computed. The factorization has not been completed unless i = n . pack (Optional) Flags the packing of the matrices: ' C ': column-major (default) ' R ': row-major
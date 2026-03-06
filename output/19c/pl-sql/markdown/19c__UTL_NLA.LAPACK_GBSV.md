---
id: 19c__UTL_NLA.LAPACK_GBSV
name: UTL_NLA.LAPACK_GBSV
object_type: plsql_subprogram
oracle_version: 19c
doc_type: plsql_packages
parent: UTL_NLA
tags: [utl_nla]
source_file: UTL_NLA.html
---

# UTL_NLA.LAPACK_GBSV

This procedure computes the solution to a real system of linear equations a * x = b , where a is a band matrix of order n with kl sub diagonals and ku superdiagonals, and x and b are n by nrhs matrices.

## Syntax

```sql
a = L * U
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| n |  |  | The number of linear equations, equivalent to the order of the matrix a . n >= 0 |
| kl |  |  | The number of sub diagonals within the band of a. kl >= 0. |
| ku |  |  | The number of superdiagonals within the band of a . ku >= 0. |
| nrhs |  |  | The number of right-hand sides, which is the number of columns of the matrix b . nrhs >= 0 . |
| ab |  |  | UTL_NLA_ARRAY_FLT / DBL, DIMENSION (ldab, n) . On entry, the matrix a in band storage, in rows kl+1 to 2*kl+ku+1 ; rows 1 to kl of the array need not be set. The j -th column of A is stored in the j -th column of the array ab : ab(kl+ku+1+i-j,j) = a(i,j) for max(1,j-ku)<=i<=min(n,j+kl) On exit, details of the factorization: U is stored as an upper triangular band matrix with kl+ku superdiagonals in rows 1 to KL+KU+1 , and the multipliers used during the factorization are stored in rows: kl+ku+2 to 2*kl+ku+1 |
| ldab |  |  | The leading dimension of the array ab. ldab >= 2*kl+ku+1 |
| ipiv |  |  | INTEGER array, DIMENSION (n) . The pivot indices that define the permutation matrix P ; row i of the matrix was interchanged with row ipiv(i) . |
| b |  |  | UTL_NLA_ARRAY_FLT / DBL, DIMENSION (ldb, nrhs) . On entry, the n by nrhs matrix of right hand side matrix b . On exit, if info = 0 , the n by nrhs solution matrix X . |
| ldb |  |  | The leading dimension of the array b. ldb >= max(1,n) |
| info |  |  | = 0 : successful exit < 0 : if info = -i , the i -th argument had an illegal value > 0 : if info = i , U(i,i) is exactly zero. The factorization has been completed, but the factor U is exactly singular, and the solution has not been computed |
| pack |  |  | (Optional) Flags the packing of the matrices: ' C ': column-major (default) ' R ': row-major |

## Usage Notes

The LU decomposition with partial pivoting and row interchanges is used to factor A as a = L * U where L is a product of permutation and unit lower triangular matrices with kl sub diagonals, and U is upper triangular with kl+ku superdiagonals. The factored form of a is then used to solve the system of equations a * x = b See Also: LAPACK Driver Routines (Linear Equations) Subprograms for other subprograms in this group See Also: LAPACK Driver Routines (Linear Equations) Subprograms for other subprograms in this group Syntax UTL_NLA.LAPACK_GBSV ( n IN POSITIVEN, kl IN NATURALN, ku IN NATURALN, nrhs IN POSITIVEN, ab IN OUT UTL_NLA_ARRAY_DBL, ldab IN POSITIVEN, ipiv IN OUT UTL_NLA_ARRAY_INT, b IN OUT UTL_NLA_ARRAY_DBL, ldb IN POSITIVEN, info OUT INTEGER, pack IN flag DEFAULT 'C'); UTL_NLA.LAPACK_GBSV ( n IN POSITIVEN, kl IN NATURALN, ku IN NATURALN, nrhs IN POSITIVEN, ab IN OUT UTL_NLA_ARRAY_FLT, ldab IN POSITIVEN, ipiv IN OUT UTL_NLA_ARRAY_INT, b IN OUT UTL_NLA_ARRAY_FLT, ldb IN POSITIVEN, info OUT INTEGER, pack IN flag DEFAULT 'C'); Parameters Table 271-39 LAPACK_GBSV Procedure Parameters Parameter Description n The number of linear equations, equivalent to the order of the matrix a . n >= 0 kl The number of sub diagonals within the band of a. kl >= 0. ku The number of superdiagonals within the band of a . ku >= 0. nrhs The number of right-hand sides, which is the number of columns of the matrix b . nrhs >= 0 . ab UTL_NLA_ARRAY_FLT / DBL, DIMENSION (ldab, n) . On entry, the matrix a in band storage, in rows kl+1 to 2*kl+ku+1 ; rows 1 to kl of the array need not be set. The j -th column of A is stored in the j -th column of the array ab : ab(kl+ku+1+i-j,j) = a(i,j) for max(1,j-ku)<=i<=min(n,j+kl) On exit, details of the factorization: U is stored as an upper triangular band matrix with kl+ku superdiagonals in rows 1 to KL+KU+1 , and the multipliers used during the factorization are stored in rows: kl+ku+2 to 2*kl+ku+1 ldab The leading dimension of the array ab. ldab >= 2*kl+ku+1 ipiv INTEGER array, DIMENSION (n) . The pivot indices that define the permutation matrix P ; row i of the matrix was interchanged with row ipiv(i) . b UTL_NLA_ARRAY_FLT / DBL, DIMENSION (ldb, nrhs) . On entry, the n by nrhs matrix of right hand side matrix b . On exit, if info = 0 , the n by nrhs solution matrix X . ldb The leading dimension of the array b. ldb >= max(1,n) info = 0 : successful exit < 0 : if info = -i , the i -th argument had an illegal value > 0 : if info = i , U(i,i) is exactly zero. The factorization has been completed, but the factor U is exactly singular, and the solution has not been computed pack (Optional) Flags the packing of the matrices: ' C ': column-major (default) ' R ': row-major
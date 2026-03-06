---
id: 19c__UTL_NLA.LAPACK_GESDD
name: UTL_NLA.LAPACK_GESDD
object_type: plsql_subprogram
oracle_version: 19c
doc_type: plsql_packages
parent: UTL_NLA
tags: [utl_nla]
source_file: UTL_NLA.html
---

# UTL_NLA.LAPACK_GESDD

This procedures computes the singular value decomposition (SVD) of a real m by n matrix A , optionally computing the left and right singular vectors. If singular vectors are desired, it uses a divide-and-conquer algorithm that makes mild assumptions about floating point arithmetic.

## Syntax

```sql
A = U * SIGMA * transpose(V)
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| jobz |  |  | Specifies options for computing all or part of the matrix U : 'A' : All m columns of u and all n rows of V**T are returned in arrays u and vt . 'S' : The first min(m,n) columns of u and the first min(m,n) rows of V**T are returned in the arrays u and vt. 'O' : The first min(m,n) columns of u (the left singular vectors) are overwritten on the array a . jobu and jobvt cannot both be 'O 'N' : No columns of u (no left singular vectors) are computed. |
| m |  |  | The order of the matrix a. m >= 0 . |
| n |  |  | The order of the matrix a. n >= 0 . |
| a |  |  | UTL_NLA_ARRAY_FLT/DBL , DIMENSION (lda, n) . On entry, the n by n matrix A . On exit: If jobz = 'O' , a is overwritten with the first min(m,n) columns of u (the left singular vectors, stored columnwise). If m >= n , a is overwritten with the first m rows of V**T (the right singular vectors, stored rowwise). If jobz .ne. 'O' , the contents of a are destroyed. |
| lda |  |  | The leading dimension of the array a. lda >= max(1,m) . |
| s |  |  | UTL_NLA_ARRAY_FLT/DBL , DIMENSION (min(m,n)) . The singular values of a , sorted so that S(i) >= S(i+1) . |
| u |  |  | UTL_NLA_ARRAY_FLT/DBL . ucol = m if jobz = 'A' or jobz = 'O' and m < n ; ucol = min(m,n) if jobz = 'S' . If jobz = 'A' or jobz = 'O' and m < n , u contains the m by m orthogonal matrix u . If jobz = 'S' , u contains the first min(m,n) columns of u (the left singular vectors, stored columnwise). If jobz = 'O' and m >= n , or jobz = 'n' , u is not referenced. |
| ldu |  |  | The leading dimension of the array U. ldu >= 1. If jobz = 'S' or 'A' ,or jobz = 'O' and m < n , ldu >= m . |
| vt |  |  | UTL_NLA_ARRAY_FLT/DBL , DIMENSION (ldvt, n) . If jobz = 'A' or jobz = 'O' and m >= n , vt contains the n by n orthogonal matrix V**T . If jobz = 'S', vt contains the first min(m,n) rows of V**T (the right singular vectors, stored rowwise). If jobz = 'O' and m < n , or jobz = 'N' , vt is not referenced. |
| ldvt |  |  | The leading dimension of the array vt . ldvt >= 1 . If jobz = 'A' , or jobz = 'O' and m >= n , ldvt >= n . If jobz = 'S' , ldvt >= min(m,n) . |
| info |  |  | = 0 : successful exit < 0 : If info = -i , the i -th argument had an illegal value > 0 : SBDSDC did not converge, updating process failed. |
| pack |  |  | (Optional) Flags the packing of the matrices: 'C' : column-major (default) 'R' : row-major |

## Usage Notes

The SVD is written A = U * SIGMA * transpose(V) where SIGMA is an m by n matrix which is zero except for its min(m,n) diagonal elements, U is an m by m orthogonal matrix, and V is an n by n orthogonal matrix. The diagonal elements of SIGMA are the singular values of A , they are real and non-negative, and are returned in descending order. The first min(m,n) columns of U and V are the left and right singular vectors of A . Note that the routine returns V**T , not V . See Also: LAPACK Driver Routines (LLS and Eigenvalue Problems) Subprograms for other subprograms in this group See Also: LAPACK Driver Routines (LLS and Eigenvalue Problems) Subprograms for other subprograms in this group Syntax UTL_NLA.LAPACK_GESDD ( jobz IN flag, m IN POSITIVEN, n IN POSITIVEN, a IN OUT UTL_NLA_ARRAY_DBL, lda IN POSITIVEN, s IN OUT UTL_NLA_ARRAY_DBL, u IN OUT UTL_NLA_ARRAY_DBL, ldu IN POSITIVEN, vt IN OUT UTL_NLA_ARRAY_DBL, ldvt IN POSITIVEN, info OUT INTEGER, pack IN flag DEFAULT 'C'); UTL_NLA.LAPACK_GESDD ( jobz IN flag, m IN POSITIVEN, n IN POSITIVEN, a IN OUT UTL_NLA_ARRAY_FLT, lda IN POSITIVEN, s IN OUT UTL_NLA_ARRAY_FLT, u IN OUT UTL_NLA_ARRAY_FLT, ldu IN POSITIVEN, vt IN OUT UTL_NLA_ARRAY_FLT, ldvt IN POSITIVEN, info OUT INTEGER, pack IN flag DEFAULT 'C'); Parameters Table 271-42 LAPACK_GESDD Procedure Parameters Parameter Description jobz Specifies options for computing all or part of the matrix U : 'A' : All m columns of u and all n rows of V**T are returned in arrays u and vt . 'S' : The first min(m,n) columns of u and the first min(m,n) rows of V**T are returned in the arrays u and vt. 'O' : The first min(m,n) columns of u (the left singular vectors) are overwritten on the array a . jobu and jobvt cannot both be 'O 'N' : No columns of u (no left singular vectors) are computed. m The order of the matrix a. m >= 0 . n The order of the matrix a. n >= 0 . a UTL_NLA_ARRAY_FLT/DBL , DIMENSION (lda, n) . On entry, the n by n matrix A . On exit: If jobz = 'O' , a is overwritten with the first min(m,n) columns of u (the left singular vectors, stored columnwise). If m >= n , a is overwritten with the first m rows of V**T (the right singular vectors, stored rowwise). If jobz .ne. 'O' , the contents of a are destroyed. lda The leading dimension of the array a. lda >= max(1,m) . s UTL_NLA_ARRAY_FLT/DBL , DIMENSION (min(m,n)) . The singular values of a , sorted so that S(i) >= S(i+1) . u UTL_NLA_ARRAY_FLT/DBL . ucol = m if jobz = 'A' or jobz = 'O' and m < n ; ucol = min(m,n) if jobz = 'S' . If jobz = 'A' or jobz = 'O' and m < n , u contains the m by m orthogonal matrix u . If jobz = 'S' , u contains the first min(m,n) columns of u (the left singular vectors, stored columnwise). If jobz = 'O' and m >= n , or jobz = 'n' , u is not referenced. ldu The leading dimension of the array U. ldu >= 1. If jobz = 'S' or 'A' ,or jobz = 'O' and m < n , ldu >= m . vt UTL_NLA_ARRAY_FLT/DBL , DIMENSION (ldvt, n) . If jobz = 'A' or jobz = 'O' and m >= n , vt contains the n by n orthogonal matrix V**T . If jobz = 'S', vt contains the first min(m,n) rows of V**T (the right singular vectors, stored rowwise). If jobz = 'O' and m < n , or jobz = 'N' , vt is not referenced. ldvt The leading dimension of the array vt . ldvt >= 1 . If jobz = 'A' , or jobz = 'O' and m >= n , ldvt >= n . If jobz = 'S' , ldvt >= min(m,n) . info = 0 : successful exit < 0 : If info = -i , the i -th argument had an illegal value > 0 : SBDSDC did not converge, updating process failed. pack (Optional) Flags the packing of the matrices: 'C' : column-major (default) 'R' : row-major
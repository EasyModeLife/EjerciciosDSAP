"""C-1.28 The p-norm of a vector v = (v1 , v2 , . . . , vn ) in n-dimensional space is de-
ﬁned as
 -  - - - - - - 
Euclidean norm of 4 + 3 = 16 + 9 = 25 = 5. Give an implemen-
tation of a function named norm such that norm(v, p) returns the p-norm
value of v and norm(v) returns the Euclidean norm of v. You may assume
that v is a list of numbers."""

def norm( v = list, p = int(2)):
    return(sum([i**p for i in v])**(1/p))


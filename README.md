# CYK-algorithm---Python3-implementation

In computer science, the Cocke–Younger–Kasami algorithm (alternatively called CYK, or CKY) is a parsing algorithm for context-free grammars, named after its inventors, John Cocke, Daniel Younger and Tadao Kasami. It employs bottom-up parsing and dynamic programming.

The standard version of CYK operates only on context-free grammars given in Chomsky normal form (CNF). However any context-free grammar may be transformed to a CNF grammar expressing the same language (Sipser 1997).

The importance of the CYK algorithm stems from its high efficiency in certain situations. Using Landau symbols, the worst case running time of CYK is Ο {\displaystyle (n^{3}\cdot |G|)} {\displaystyle (n^{3}\cdot |G|)}, where n is the length of the parsed string and |G| is the size of the CNF grammar G (Hopcroft & Ullman 1979, p. 140). This makes it one of the most efficient parsing algorithms in terms of worst-case asymptotic complexity, although other algorithms exist with better average running time in many practical scenarios.

Input format:
In the first line enter the number of rules and the enter the rules (A -> a)
Terminal nodes : lowwer case
Non-terminal nodes : upper case

Example input 1: <br/>
5 <br/>
S -> AB <br/>
A -> BB <br/>
A -> a <br/>
B -> AB <br/>
B -> b <br/>
aabbb <br/>

Example output 1: <br/>
YES <br/>
a : [A] , a : [A] , b : [B] , b : [B] , b : [B] <br/>
aa : [] , ab : [B,S] , bb : [A] , bb : [A] <br/>
aab : [B,S] , abb : [A] , bbb : [B,S] <br/>
aabb : [A] , abbb : [B,S] <br/>
aabbb : [B,S] <br/>

Example input 2:<br/>
3<br/>
S -> ABB<br/>
A -> BB<br/>
B -> a<br/>
aa<br/>

Exmple output 2:<br/>
Wrong Grammar<br/>

Example input 3:<br/>
4<br/>
S -> AB<br/>
A -> a<br/>
B -> AB<br/>
B -> b<br/>
bababa<br/>

Example output 3:<br/>
NO<br/>

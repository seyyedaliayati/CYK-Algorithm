# Examples
Input format: <br/>
In the first line enter the number of rules and the enter the rules (A -> a) <br/>
Terminal nodes : lower case <br/>
Non-terminal nodes : upper case <br/>

---

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

---

Example input 2:<br/>
3<br/>
S -> ABB<br/>
A -> BB<br/>
B -> a<br/>
aa<br/>

Exmple output 2:<br/>
Wrong Grammar<br/>

---

Example input 3:<br/>
4<br/>
S -> AB<br/>
A -> a<br/>
B -> AB<br/>
B -> b<br/>
bababa<br/>

Example output 3:<br/>
NO<br/>

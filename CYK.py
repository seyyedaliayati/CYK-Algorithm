"""
--------------------------------------- CYK Algotithm --------------------------------------
author : Seyyed Ali Ayati
CE @ IUST
Final project
Data Structure
Dr. Rahmani
"""
NumOfNotations = int(input())
Grammer = list()


def check_grammer(Grammer):
    Variables = {}
    for Notation in Grammer:
        if len(Notation[0]) != 1 or not (Notation[0].isupper()):
            return False
        if Notation[0] not in Variables or Variables[Notation[0]] == "undefiend":
            Variables[Notation[0]] = "defined"
        if len(Notation[1]) > 2 or len(Notation[1]) == 0:
            return False
        if len(Notation[1]) == 1 and not (Notation[1][0].islower()):
            return False
        if len(Notation[1]) == 2:
            if not (Notation)[1][0].isupper() or not (Notation)[1][1].isupper():
                return False
            for i in range(2):
                if Notation[1][i] not in Variables:
                    Variables[Notation[1][i]] = "Undefiend"
    for Value in Variables.values():
        if Value == "undefiend":
            return False
    return True


def cyk(String, Computed={}, Grammer=Grammer):
    if String in Computed:
        return Computed
    else:
        if len(String) == 1:
            Computed[String] = ""
            for Notation in Grammer:
                if Notation[1] == String:
                    Computed[String] += (Notation[0])
            Computed[String] = str(sorted(Computed[String])).replace(
                "'", "").replace(" ", "")
            return Computed
        else:
            Computed[String] = ""
            for i in range(1, len(String)):
                Splitted1 = String[:i]
                Splitted2 = String[i:]
                Computed1 = cyk(Splitted1, Computed)[Splitted1]
                Computed2 = cyk(Splitted2, Computed)[Splitted2]
                if Computed1 != "" and Computed2 != "":
                    for Var1 in Computed1:
                        for Var2 in Computed2:
                            for Notation in Grammer:
                                if Var1+Var2 in Notation[1] and Notation[0] not in Computed[String]:
                                    Computed[String] += (Notation[0])
            Computed[String] = str(sorted(Computed[String])).replace(
                "'", "").replace(" ", "")
            return Computed


def print_cyk(String, Grammer):
    result = cyk(String, {}, Grammer)
    if result[String] != "[]" and "S" in result[String]:
        print("YES")
        for i in range(1, len(String)+1):
            for j in range(len(String) - i):
                if String[j:j+i] in result:
                    print(String[j:j+i]+" : " +
                          result[String[j:j+i]]+" , ", end="")
                else:
                    print(String[j:j+i]+" : "+"[]"+" , ", end="")
            print(String[-i:], " : "+result[String[-i:]])
    else:
        print("NO")


for i in range(NumOfNotations):
    Notation = input().split(" -> ")
    Grammer.append(Notation)
String = input()
if check_grammer(Grammer):
    print_cyk(String, Grammer)
else:
    print("Wrong Grammar")

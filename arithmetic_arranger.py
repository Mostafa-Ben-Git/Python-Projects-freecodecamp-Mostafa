def arithmetic_arranger(lis, sol=False):
    newlis = []
    for problem in lis:
        newlis.append(problem.split(" "))
    lin1 = ""
    lin2 = ""
    lin3 = ""
    lin4 = ""
    for j in newlis:
        if len(lis) > 5:
            return "Error: Too many problems."
        elif (j[0].isdecimal() and j[-1].isdecimal()) == False:
            return "Error: Numbers must only contain digits."
        elif len(j[0]) > 4 or len(j[-1]) > 4:
            return "Error: Numbers cannot be more than four digits."
        elif j[1] != "-" and j[1] != "+":
            return "Error: Operator must be '+' or '-'."
        else:
            k = len(max(j, key=len))
            num_1 = j[0].rjust(k + 2) + "    "
            num_2 = j[-1].rjust(k + 1) + "    "
            lin1 += num_1
            lin2 += j[1] + num_2
            lin3 += "-" * (k + 2) + "    "
            if j[1] == "+":
                result = str(int(j[0]) + int(j[-1]))
            else:
                result = str(int(j[0]) - int(j[-1]))
            lin4 += result.rjust(k + 2) + "    "
    problems = f"{lin1.rstrip()}\n{lin2.rstrip()}\n{lin3.rstrip()}"
    if sol == False:
        return problems
    return problems + f"\n{lin4.rstrip()}"


print(
    arithmetic_arranger(
        ["11 + 4", "3801 - 2999", "1 + 2", "123 + 49", "1 - 9380"], True
    )
)

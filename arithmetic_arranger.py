def arithmetic_arranger(problems, ans=False):
    if len(problems) > 5:
        return 'Error: Too many problems.'

    dict_lines = {}
    separate_problems = []
    for i in range(len(problems)):                    
        separate_problems = problems[i].split(" ")
        if separate_problems[1] not in "+-":
            return "Error: Operator must be '+' or '-'."
        if len(separate_problems[0]) > 4 or len(separate_problems[2]) > 4:
            return 'Error: Numbers cannot be more than four digits.'
        if separate_problems[0].isdigit() and separate_problems[2].isdigit():
            answer = str(eval(problems[i]))
            if len(separate_problems[0]) < len(separate_problems[2]):
                total_length = len(separate_problems[2]) + 2
            else:
                total_length = len(separate_problems[0]) + 2
            first_line = ' '*(total_length-len(separate_problems[0])) + separate_problems[0]
            second_line = separate_problems[1] + ' '*(total_length-len(separate_problems[2])-1) + separate_problems[2]
            dashes = '-'*total_length            
            answer = ' '*(total_length-len(answer)) + answer
            dict_lines[i] = [first_line, second_line, dashes, answer]
            
        else:
            return 'Error: Numbers must only contain digits.'
        
    arranged_problems = ''
    for i in range(4):
        for j in range(len(problems)):
            if j == len(problems) - 1:
                arranged_problems += dict_lines[j][i]
            else:
                arranged_problems += dict_lines[j][i] + '    '
        if ans == False and i == 2:
            break
        if i != 3:
            arranged_problems += '\n'
    return arranged_problems
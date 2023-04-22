def arithmetic_arranger(problems: list, ans: bool= False) -> str:
    """Return a string with the problems arranged vertically and side-by-side."""
    if len(problems) > 5:
        return 'Error: Too many problems.'
    
    dict_lines = {}
    for problem in range(len(problems)):                    
        problem_components = problems[problem].split(" ")
        num1 = problem_components[0]
        operator = problem_components[1]
        num2 = problem_components[2]
        if check_errors(num1, operator, num2):
            return check_errors(num1, operator, num2)
        
        answer = str(eval(problems[problem]))
        dict_lines[problem] = problem_solver(num1, operator, num2, answer)   
    
    return problems_arranger(problems, dict_lines, ans)

def check_errors(num1: str, operator: str, num2: str):
    """Check for errors in the input."""
    if operator not in "+-":
        return "Error: Operator must be '+' or '-'."        
    if len(num1) > 4 or len(num2) > 4:
        return 'Error: Numbers cannot be more than four digits.'
    if not num1.isdigit() or not num2.isdigit():
        return 'Error: Numbers must only contain digits.'

def problem_solver(num1: str, operator: str, num2: str, answer: str) -> list:
    """Create a list of strings with the problem solved.

    Args:
    num1 -- first number
    operator -- operator
    num2 -- second number
    answer -- answer to the problem

    Returns:
    list of strings with the problem solved
    """
    if len(num1) < len(num2):
        total_length = len(num2) + 2
    else:
        total_length = len(num1) + 2
    first_line = ' '*(total_length-len(num1)) + num1
    second_line = operator + ' '*(total_length-len(num2)-1) + num2
    dashes = '-'*total_length            
    answer = ' '*(total_length-len(answer)) + answer
    
    return [first_line, second_line, dashes, answer]

def problems_arranger(problems: list, dict_lines: dict, ans: bool) -> str:
    """Arrange the problems vertically and side-by-side.

    Args:
    problems -- list of problems to be arranged
    dict_lines -- dictionary with the problems solved
    ans -- boolean to show or not the answers

    Returns 
    string with the problems arranged vertically and side-by-side
    """
    arranged_problems = ''
    for line in range(4):
        for problem in range(len(problems)):
            if problem == len(problems) - 1:
                arranged_problems += dict_lines[problem][line]
            else:
                arranged_problems += dict_lines[problem][line] + '    '
        if ans == False and line == 2:
            break
        if line != 3:
            arranged_problems += '\n'
            
    return arranged_problems
from stack_array import Stackin

# You do not need to change this class
class PostfixFormatException(Exception):
    pass

def postfix_eval(input_str):
    '''Evaluates a postfix expression

    Input argument:  a string containing a postfix expression where tokens
    are space separated.  Tokens are either operators + - * / ** >> << or numbers.
    Returns the result of the expression evaluation.
    Raises an PostfixFormatException if the input is not well-formed
    DO NOT USE PYTHON'S EVAL FUNCTION!!!'''
    input_str = input_str.split(' ')
    length = len(input_str)
    post_stack = Stackin(length)
    i = 0
    while length > 0:
        try:
            x = int(input_str[i])
            post_stack.push(x)
            i += 1
            length -= 1
        except ValueError:
                if input_str[i] == '+':
                    if post_stack.size() < 2:
                        raise PostfixFormatException("Insufficient operands")
                    y = post_stack.pop()
                    x = post_stack.pop()
                    length -= 1
                    i += 1
                    post_stack.push(x + y)
                elif input_str[i] == '-':
                    if post_stack.size() < 2:
                        raise PostfixFormatException("Insufficient operands")
                    y = post_stack.pop()
                    x = post_stack.pop()
                    length -= 1
                    i += 1
                    post_stack.push(x - y)
                elif input_str[i] == '*':
                    if post_stack.size() < 2:
                        raise PostfixFormatException("Insufficient operands")
                    y = post_stack.pop()
                    x = post_stack.pop()
                    length -= 1
                    i += 1
                    post_stack.push(x * y)
                elif input_str[i] == '/':
                    if post_stack.size() < 2:
                        raise PostfixFormatException("Insufficient operands")
                    y = post_stack.pop()
                    x = post_stack.pop()
                    if y == 0:
                        raise ValueError
                    length -= 1
                    i += 1
                    post_stack.push(x / y)
                elif input_str[i] == '**':
                    if post_stack.size() < 2:
                        raise PostfixFormatException("Insufficient operands")
                    y = post_stack.pop()
                    x = post_stack.pop()
                    length -= 1
                    i += 1
                    post_stack.push(x ** y)
                elif input_str[i] == '>>':
                    if post_stack.size() < 2:
                        raise PostfixFormatException("Insufficient operands")
                    y = post_stack.pop()
                    x = post_stack.pop()
                    length -= 1
                    i += 1
                    post_stack.push(x >> y)
                elif input_str[i] == '<<':
                    if post_stack.size() < 2:
                        raise PostfixFormatException("Insufficient operands")
                    y = post_stack.pop()
                    x = post_stack.pop()
                    length -= 1
                    i += 1
                    post_stack.push(x << y)
                else:
                    raise PostfixFormatException("Invalid token")
    if post_stack.size() > 1:
        raise PostfixFormatException("Too many operands")

    result = post_stack.pop()
    return result


def prefix_to_postfix(input_str):
    '''Converts a prefix expression to an equivalent postfix expression

    Input argument:  a string containing a prefix expression where tokens are
    space separated.  Tokens are either operators + - * / ** >> << parentheses ( ) or numbers
    Returns a String containing a postfix expression(tokens are space separated)'''
    input_str = input_str.split(' ')
    length = len(input_str)
    post_stack = Stackin(length)
    i = 1
    while i <= length:
        try:
            x = int(input_str[length - i])
            post_stack.push(input_str[length - i])
            i += 1
        except ValueError:
            if input_str[length - i] == '+':
                y = post_stack.pop()
                x = post_stack.pop()
                i += 1
                post_stack.push(y+' '+x+' +')
            elif input_str[length - i] == '-':
                y = post_stack.pop()
                x = post_stack.pop()
                i += 1
                post_stack.push(y+' '+x+' -')
            elif input_str[length - i] == '*':
                y = post_stack.pop()
                x = post_stack.pop()
                i += 1
                post_stack.push(y+' '+x+' *')
            elif input_str[length - i] == '/':
                y = post_stack.pop()
                x = post_stack.pop()
                i += 1
                post_stack.push(y+' '+x+' /')
            elif input_str[length - i] == '**':
                y = post_stack.pop()
                x = post_stack.pop()
                i += 1
                post_stack.push(y+' '+x+' **')
            elif input_str[length - i] == '>>':
                y = post_stack.pop()
                x = post_stack.pop()
                i += 1
                post_stack.push(y+' '+x+' >>')
            elif input_str[length - i] == '<<':
                y = post_stack.pop()
                x = post_stack.pop()
                i += 1
                post_stack.push(y+' '+x+' <<')
    return post_stack.pop()

import logging

# logging.basicConfig(level = logging.INFO, filename = 'LoggingData.log', filemode = 'w')
logging.basicConfig(format='%(asctime)s :: %(levelname)s :: %(funcName)s :: %(lineno)d \
:: %(message)s', level = logging.INFO,filename = 'LoggingData.log', filemode = 'w')

logging.debug("A Debug Logging Message")
logging.info("A Info Logging Message")
logging.warning("A Warning Logging Message")
logging.error("An Error Logging Message")
logging.critical("A Critical Logging Message")


# real life example
def addition(x, y):
    add = x + y
    return add

def subtract(x, y):
    sub = x - y
    return sub

def multiply(x, y):
    mul = x * y
    return mul

def divide(x, y):
    div = x / y
    return div

def exponent(x, y):
    exp = x ** y
    return exp

num1 = 20
num2 = 2

def main():
    add_result = addition(num1, num2)
    logging.info('Add: {} + {} = {}'.format(num1, num2, add_result))

    sub_result = subtract(num1, num2)
    logging.info('Sub: {} - {} = {}'.format(num1, num2, sub_result))

    mul_result = multiply(num1, num2)
    logging.info('Mul: {} * {} = {}'.format(num1, num2, mul_result))

    div_result = divide(num1, num2)
    logging.info('Div: {} / {} = {}'.format(num1, num2, div_result))

    exp_result = exponent(num1, num2)
    logging.info('Exp: {} ** {} = {}'.format(num1, num2, exp_result))


main()

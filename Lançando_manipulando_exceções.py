import random


class ExcptError(Exception):
    """Custom exception for specific error cases."""
    pass


class OnlyEvens(list):
    def append(self, value):
        if not isinstance(value, int):
            raise ExcptError(f"Only integers can be added, not: {value}")
        if value % 2 != 0:
            raise ValueError("Only even numbers can be added.")
        super().append(value)


class ExceptionExamples:
    @staticmethod
    def raise_exception():
        raise ExcptError("Exception occurred.")

    @staticmethod
    def division(divisor):
        try:
            return 10 / divisor
        except ZeroDivisionError:
            return "Division by zero is not allowed!"

    @staticmethod
    def multiplication(multiplier):
        try:
            if multiplier == 7:
                raise ExcptError("Do not use number 7.")
            a = random.randint(10, 20)
            return f"Your number is: {a / multiplier:.4f}"
        except (ZeroDivisionError, TypeError):
            return "No division by zero and only numbers allowed, got it?"

    @staticmethod
    def addition(adder):
        try:
            if adder == 7:
                raise ExcptError("Do not use number 7.")
            a = random.randint(10, 20)
            return f"Number: {a + adder}"
        except TypeError:
            return "Please enter a numeric value."
        except ValueError as e:
            return str(e)
        except ExcptError as e:
            return f"Unknown problem encountered: {e}"

    @staticmethod
    def exception_with_args():
        try:
            raise ValueError("Value error.")
        except ValueError as e:
            print("Exception arguments:", e.args)
        finally:
            print("This always runs.")

    @staticmethod
    def hola(divisor):
        try:
            if divisor == 7:
                raise ExcptError("Do not use number 7.")
        except ZeroDivisionError:
            return "Do not divide by 0."
        except ValueError as e:
            return str(e)
        except TypeError:
            return "Type error detected."
        else:
            print("No exceptions occurred.")


if __name__ == "__main__":
    sp = OnlyEvens()

    for test_val in ["jupyter", 5, 10, 20, 4]:
        try:
            sp.append(test_val)
            print(f"Appended {test_val} successfully!")
        except (ExcptError, ValueError) as e:
            print(f"Error appending {test_val}: {e}")

    print("Current OnlyEvens list:", sp)

    try:
        ExceptionExamples.raise_exception()
    except ExcptError:
        print("Exception caught successfully!")

    print(ExceptionExamples.division(0))
    print(ExceptionExamples.division(3))

    print(ExceptionExamples.multiplication(0))
    print(ExceptionExamples.multiplication("pepper"))
    print(ExceptionExamples.multiplication(7))

    print(ExceptionExamples.addition(7))
    print(ExceptionExamples.addition("test"))
    print(ExceptionExamples.addition(10))

    ExceptionExamples.exception_with_args()

    ExceptionExamples.hola(0)

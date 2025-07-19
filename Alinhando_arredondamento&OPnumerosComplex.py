import logging

# Setup logging configuration
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class TextFormatterError(Exception):
    pass

class TextFormatter:
    def __init__(self, text: str):
        self._text = text

    @property
    def text(self):
        return self._text
    
    @text.setter
    def text(self, value: str):
        if not isinstance(value, str):
            logger.error("Attempted to set non-strings text.")
            raise TextFormatterError("Text must be a strings.")
        self._text = value
        logger.info(f"Text updated to: {self._text}")
    
    def left_justify(self, width: int, fillchar: str = ' '):
        try:
            result = self._text.ljust(width, fillchar)
            logger.info(f"Left justified text: '{result}'")
            return result
        except Exception as e:
            logger.error(f"Error in left_justify: {e}")
            raise
    
    def right_justify(self, width: int, fillchar: str= ' '):
        try:
            result = self._text.rjust(width, fillchar)
            logger.info(f"Right justified text: '{result}'")
            return result
        except Exception as e:
            logger.error(f"Error in right_justify: {e}")
            raise

    def center_text(self, width: int, fillchar: str= ' '):
        try:
            result = self._text.center(width, fillchar)
            logger.info(f"Centered text: '{result}'")
            return result
        except Exception as e:
            logger.eror(f"Error in center_text: {e}")
            raise
    
    def format_text(self, width: int, align: str= '>', fillchar: str= ' '):
        """
        Format text using Python's format specification.
        align: '>' right, '<', left, '^' center
        """
        if align not in ['>', '<', '^']:
            logger.error("Invalid aligment character used.")
            raise TextFormatterError("Aligment must be one of: '>', '<', '^'.")
        
        try:
            format_spec = f"{fillchar}{align}{width}"
            result = format(self._text, format_spec)
            logger.info(f"Formatted text with spec '{format_spec}': '{result}'")
            return result
        except Exception as e:
            logger.error(f"Error in format_text: {e}")
            raise

class MathOperations:
    @staticmethod
    def round_number(value: float, decimals: int = 0):
        try:
            result = round(value, decimals)
            logger.info(f"Rounded value: {result} (input was {value}), decimals={decimals}")
            return result
        except Exception as e:
            logger.error(f"Error in round_number: {e}")
            raise

    @staticmethod
    def complex_parts(c: complex):
        logger.info(f"Complex number: {c} -> Real: {c.real}, Imaginary: {c.imag}")
        return (c.real, c.imag)
    
    @staticmethod
    def add_complex(c1: complex, c2: complex):
        result = c1 + c2
        logger.info(f"Adding complex numbers: {c1} + {c2} = {result}")
        return result
    
    @staticmethod
    def subtract_complex(c1: complex, c2: complex):
        result = c1 - c2
        logger.info(f"Subtracting complex numbers: {c1} - {c2} = {result}")
        return result
    
if __name__ == "__main__":
    tf = TextFormatter("Dimmy Neutron")

    tf.text = "Dimmy Neutron"

    print(tf.left_justify(40))
    print(tf.right_justify(40))
    print(tf.center_text(40))

    print(tf.left_justify(40, 'n'))
    print(tf.right_justify(40, '%'))
    print(tf.center_text(40, '-'))

    print(tf.format_text(40, '>', '%'))
    print(tf.format_text(40, '<', 'n'))
    print(tf.format_text(40, '^', '-'))

    # Math operations
    print(MathOperations.round_number(1.27, 1))
    print(MathOperations.round_number(-1.27, 1))
    print(MathOperations.round_number(4.5))
    print(MathOperations.round_number(7.5))
    print(MathOperations.round_number(1.253, 2))
    print(MathOperations.round_number(1.258, 2))

    c1 = complex(2, 4)
    c2 = 3 + 5j

    MathOperations.complex_parts(c1)
    MathOperations.complex_parts(c2)

    print(MathOperations.add_complex(c1, c2))
    print(MathOperations.subtract_complex(c1, c2))
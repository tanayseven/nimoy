from nimoy.specification import Specification
from nimoy.spec_runner import SpecRunner


class WhereBlocksSpec(Specification):
    def single_variable(self):
        with given:
            spec_contents = """from nimoy.specification import Specification
        
class JimbobSpec(Specification):
    
    def test(self):
        with given:
            a = value_of_a
            
        with expect:
            (a % 2) == 0
        
        with where:
            value_of_a = [2, 4, 6, 8]
            """

        with when:
            result = self._run_spec_contents(spec_contents)
        with then:
            result.wasSuccessful() == True

    def single_variable_with_explicit_declaration(self):
        with given:
            spec_contents = """from nimoy.specification import Specification
        
class JimbobSpec(Specification):
    
    def test(self, value_of_a):
        with given:
            a = value_of_a
            
        with expect:
            (a % 2) == 0
        
        with where:
            value_of_a = [2, 4, 6, 8]
            """

        with when:
            result = self._run_spec_contents(spec_contents)
        with then:
            result.wasSuccessful() == True

    def single_variable_with_generator(self):
        with given:
            spec_contents = """from nimoy.specification import Specification
        
class JimbobSpec(Specification):
    
    def test(self):
        with given:
            a = value_of_a
            
        with expect:
            a < 10
        
        with where:
            value_of_a = (x for x in range(10))
            """

        with when:
            result = self._run_spec_contents(spec_contents)
        with then:
            result.wasSuccessful() == True

    def single_variable_with_single_value(self):
        with given:
            spec_contents = """from nimoy.specification import Specification
        
class JimbobSpec(Specification):
    
    def test(self):
        with given:
            a = value_of_a
            
        with expect:
            (a % 2) == 0
        
        with where:
            value_of_a = [2]
            """

        with when:
            result = self._run_spec_contents(spec_contents)
        with then:
            result.wasSuccessful() == True

    def single_variable_with_instance_function(self):
        with given:
            spec_contents = """from nimoy.specification import Specification
        
class JimbobSpec(Specification):
    
    def test(self):
        with given:
            a = value_of_a
            
        with expect:
            a == 0
        
        with where:
            value_of_a = self.set_of_numbers()
            
    def set_of_numbers(self):
        return [0, 0 ,0]
            """

        with when:
            result = self._run_spec_contents(spec_contents)
        with then:
            result.wasSuccessful() == True

    def single_variable_with_instance_function_that_receives_parameters(self):
        with given:
            spec_contents = """from nimoy.specification import Specification
        
class JimbobSpec(Specification):
    
    def test(self):
        with given:
            a = value_of_a
            
        with expect:
            a == 0
        
        with where:
            value_of_a = self._set_of_numbers(0)
    
    def _set_of_numbers(self, value):
        return [value, value, value]
            """

        with when:
            result = self._run_spec_contents(spec_contents)
        with then:
            result.wasSuccessful() == True

    def single_variable_with_static_function(self):
        with given:
            spec_contents = """from nimoy.specification import Specification
        
class JimbobSpec(Specification):
    
    def test(self):
        with given:
            a = value_of_a
            
        with expect:
            a == 0
        
        with where:
            value_of_a = JimbobSpec._set_of_numbers()
    
    @staticmethod
    def _set_of_numbers():
        return [0, 0 ,0]
            """

        with when:
            result = self._run_spec_contents(spec_contents)
        with then:
            result.wasSuccessful() == True

    def single_variable_with_static_function_that_receives_parameters(self):
        with given:
            spec_contents = """from nimoy.specification import Specification
        
class JimbobSpec(Specification):
    
    def test(self):
        with given:
            a = value_of_a
            
        with expect:
            a == 0
        
        with where:
            value_of_a = JimbobSpec._set_of_numbers(0)
    
    @staticmethod       
    def _set_of_numbers(value):
        return [value, value, value]
            """

        with when:
            result = self._run_spec_contents(spec_contents)
        with then:
            result.wasSuccessful() == True

    def single_variable_with_generator_function(self):
        with given:
            spec_contents = """from nimoy.specification import Specification

class JimbobSpec(Specification):
    def test(self):
        with given:
            a = value_of_a

        with expect:
            a < 3

        with where:
            value_of_a = JimbobSpec._generate_sequence(self)

    def _generate_sequence(self):
        i = 0
        while i < 3:
            yield i
            i += 1
            """

        with when:
            result = self._run_spec_contents(spec_contents)
        with then:
            result.wasSuccessful() == True

    def single_variable_with_static_generator_function(self):
        with given:
            spec_contents = """from nimoy.specification import Specification

class JimbobSpec(Specification):
    def test(self):
        with given:
            a = value_of_a

        with expect:
          a < 3

        with where:
            value_of_a = JimbobSpec._generate_sequence()

    @staticmethod
    def _generate_sequence():
        i = 0
        while i < 3:
            yield i
            i += 1
            """

        with when:
            result = self._run_spec_contents(spec_contents)
        with then:
            result.wasSuccessful() == True

    def single_variable_with_external_module_function(self):
        spec_contents = """import itertools
from nimoy.specification import Specification
        
class JimbobSpec(Specification):
    
    def test(self):
        with given:
            a = value_of_a
            
        with expect:
            len(list(a)) == 2
        
        with where:
            value_of_a = itertools.permutations(range(2), 2)
            """

        with when:
            result = self._run_spec_contents(spec_contents)
        with then:
            result.wasSuccessful() == True

    def single_variable_and_fail(self):
        with given:
            spec_contents = """from nimoy.specification import Specification
        
class JimbobSpec(Specification):
    
    def test(self):
        with given:
            a = value_of_a
            
        with expect:
            (a % 2) == 0
        
        with where:
            value_of_a = [4, 3]
            """

        with when:
            result = self._run_spec_contents(spec_contents)
        with then:
            result.wasSuccessful() == False

    def single_variable_with_single_value_and_fail(self):
        with given:
            spec_contents = """from nimoy.specification import Specification
        
class JimbobSpec(Specification):
    
    def test(self):
        with given:
            a = value_of_a
            
        with expect:
            (a % 2) == 0
        
        with where:
            value_of_a = [3]
            """

        with when:
            result = self._run_spec_contents(spec_contents)
        with then:
            result.wasSuccessful() == False

    def list_form_multi_variables(self):
        with given:
            spec_contents = """from nimoy.specification import Specification
        
class JimbobSpec(Specification):
    
    def test(self):
        with given:
            a = value_of_a
            b = value_of_b
            
        with expect:
            (a * b) == expected_value
        
        with where:
            value_of_a = [2, 4, 6]
            value_of_b = [1, 3, 5]
            expected_value = [2, 12, 30]
            """

        with when:
            result = self._run_spec_contents(spec_contents)
        with then:
            result.wasSuccessful() == True

    def list_form_multi_variables_with_a_single_value(self):
        with given:
            spec_contents = """from nimoy.specification import Specification
        
class JimbobSpec(Specification):
    
    def test(self):
        with given:
            a = value_of_a
            b = value_of_b
            
        with expect:
            (a * b) == expected_value
        
        with where:
            value_of_a = [2]
            value_of_b = [1]
            expected_value = [2]
            """

        with when:
            result = self._run_spec_contents(spec_contents)
        with then:
            result.wasSuccessful() == True

    def list_form_multi_variables_and_fail(self):
        with given:
            spec_contents = """from nimoy.specification import Specification
        
class JimbobSpec(Specification):
    
    def test(self):
        with given:
            a = value_of_a
            b = value_of_b
            
        with expect:
            (a * b) == expected_value
        
        with where:
            value_of_a = [1, 2]
            value_of_b = [1, 1]
            expected_value = [1, 5]
            """

        with when:
            result = self._run_spec_contents(spec_contents)
        with then:
            result.wasSuccessful() == False

    def list_form_multi_variables_with_a_single_value_and_fail(self):
        with given:
            spec_contents = """from nimoy.specification import Specification
        
class JimbobSpec(Specification):
    
    def test(self):
        with given:
            a = value_of_a
            b = value_of_b
            
        with expect:
            (a * b) == expected_value
        
        with where:
            value_of_a = [1]
            value_of_b = [1]
            expected_value = [5]
            """

        with when:
            result = self._run_spec_contents(spec_contents)
        with then:
            result.wasSuccessful() == False

    def matrix_form_multi_variables(self):
        with given:
            spec_contents = """from nimoy.specification import Specification
        
class JimbobSpec(Specification):
    
    def test(self):
        with given:
            a = value_of_a
            b = value_of_b
            
        with expect:
            (a * b) == expected_value
        
        with where:
            value_of_a | value_of_b | expected_value
            2          | 1          | 2
            4          | 3          | 12
            6          | 5          | 30
            """

        with when:
            result = self._run_spec_contents(spec_contents)
        with then:
            result.wasSuccessful() == True

    def stringy_matrix_form_variable_names(self):
        with given:
            spec_contents = """from nimoy.specification import Specification
        
class JimbobSpec(Specification):
    
    def test(self):
        with given:
            a = value_of_a
            b = value_of_b
            
        with expect:
            (a * b) == expected_value
        
        with where:
            "value_of_a" | "value_of_b" | "expected_value"
            2            | 1            | 2
            4            | 3            | 12
            6            | 5            | 30
            """

        with when:
            result = self._run_spec_contents(spec_contents)
        with then:
            result.wasSuccessful() == True

    def matrix_form_with_explicit_declaration(self):
        with given:
            spec_contents = """from nimoy.specification import Specification
        
class JimbobSpec(Specification):
    
    def test(self, value_of_a, value_of_b, expected_value):
        with given:
            a = value_of_a
            b = value_of_b
            
        with expect:
            (a * b) == expected_value
        
        with where:
            value_of_a | value_of_b | expected_value
            2          | 1          | 2
            
            """

        with when:
            result = self._run_spec_contents(spec_contents)
        with then:
            result.wasSuccessful() == True

    def matrix_form_multi_variables_with_a_single_value(self):
        with given:
            spec_contents = """from nimoy.specification import Specification
        
class JimbobSpec(Specification):
    
    def test(self):
        with given:
            a = value_of_a
            b = value_of_b
            
        with expect:
            (a * b) == expected_value
        
        with where:
            value_of_a | value_of_b | expected_value
            2          | 1          | 2
            """

        with when:
            result = self._run_spec_contents(spec_contents)
        with then:
            result.wasSuccessful() == True

    def matrix_form_multi_variables_and_fail(self):
        with given:
            spec_contents = """from nimoy.specification import Specification
        
class JimbobSpec(Specification):
    
    def test(self):
        with given:
            a = value_of_a
            b = value_of_b
            
        with expect:
            (a * b) == expected_value
        
        with where:
            value_of_a | value_of_b | expected_value
            1          | 1          | 1
            2          | 1          | 10
            """

        with when:
            result = self._run_spec_contents(spec_contents)
        with then:
            result.wasSuccessful() == False

    def matrix_form_multi_variables_with_a_single_value_and_fail(self):
        with given:
            spec_contents = """from nimoy.specification import Specification
        
class JimbobSpec(Specification):
    
    def test(self):
        with given:
            a = value_of_a
            b = value_of_b
            
        with expect:
            (a * b) == expected_value
        
        with where:
            value_of_a | value_of_b | expected_value
            2          | 1          | 10
            """

        with when:
            result = self._run_spec_contents(spec_contents)
        with then:
            result.wasSuccessful() == False

    def _run_spec_contents(self, spec_contents):
        return SpecRunner._run_on_contents([('/fake/path.py', spec_contents)])

'''Problem 4: Primitive Data Types and Basic Operations.

Write a Python program to explore **primitive data types in Python**, understand their **memory size**, and perform **basic operations and type conversions**.
Primitive data types include:
- Integer (`int`)
- Float (`float`)
- Complex (`complex`)
- Boolean (`bool`)
- String (`str`)

Part 1: Variable Creation
Create variables of the following primitive data types and assign suitable values.
| Data Type | Example Value |
| Integer | 25 |
| Float | 3.14 |
| Complex | 3 + 4j |
| Boolean | True |
| String | "Python Programming" |
Display the **value and data type** of each variable using the `type()` function.

Part 2: Memory Size of Data
Display the **memory size** of each variable using the `sys.getsizeof()` function.
Example:
```python
import sys
print(sys.getsizeof(a))
```
Print the size in **bytes** for each data type.
Display the **result and resulting data type**.

Part 3: Exploring Complex Numbers
For a complex number variable, display the following properties:
- Real part using `.real`
- Imaginary part using `.imag`
- Magnitude using `abs()`
Example:
z = 3 + 4j
print(z.real)
print(z.imag)
print(abs(z))

Part 4: Boolean Operations
Create two boolean variables and perform the following **logical operations**:
- AND (`and`)
- OR (`or`)
- NOT (`not`)
Example:
True and False
True or False
not True

Part 5: Type Conversion
Perform the following **type conversions** and display the results:
- Integer  Float
- Float  Integer
- Integer  String
- String  Integer
- Boolean  Integer
- Integer  Complex'''

#part1 - variable creation and type display
def var_create_type():
    a=25 
    b=3.14
    c=3+4j
    d=True
    e="Python Programming"
    print("Values and Data Types")
    print(a,type(a))
    print(b,type(b))
    print(c,type(c))
    print(d,type(d))
    print(e,type(e))
var_create_type()
print()

#part2 - memory size of data
def memory_size():
    import sys
    a=25
    b=3.14
    c=3+4j
    d=True
    e="Python Programming"
    print("Memory Size (bytes)")
    print("int:",sys.getsizeof(a))
    print("float:",sys.getsizeof(b))
    print("complex:",sys.getsizeof(c))
    print("bool:",sys.getsizeof(d))
    print("str:",sys.getsizeof(e))
memory_size()
print()


#part3 - complex number operations
def complex_op():
    z=3+4j
    print("Complex Number operations")
    print("Real part:",z.real)
    print("Imaginary part:",z.imag)
    print("Magnitude:",abs(z))
complex_op()
print()

#part4 - boolean operations
def boolean_op():
    x=True
    y=False
    print("Boolean Operations")
    print("AND:",x and y)
    print("OR:",x or y)
    print("NOT:",not x)
boolean_op()
print()

#part5 - type conversions
def type_conv():
    i=10
    f=5.6
    s="123"
    bo=True
    print("Type Conversion")
    print("int->float:",i,type(i),"->",float(i),type(float(i)))
    print("float->int:",f,type(f),"->",int(f),type(int(f)))
    print("int->str:",i,type(i),"->",str(i),type(str(i)))
    print("str->int:",s,type(s),"->",int(s),type(int(s)))
    print("bool->int:",bo,type(bo),"->",int(bo),type(int(bo)))
    print("int->complex:",i,type(i),"->",complex(i),type(complex(i)))
type_conv()
print()





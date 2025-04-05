# Write First C++ program - Hello World

The “Hello World” program is the first step towards learning any programming language and is also one of the most straightforward programs you will learn. It is the basic program that is used to demonstrate how the coding process works. All you have to do is display the message “Hello World” on the output screen.

## C++ Hello World Program

Below is the C++ program to print “Hello World” on the console screen.

```C++
// Header file for input output functions
#include <iostream>
using namespace std;

// main() function: where the execution of
// C++ program begins
int main() {

    // This statement prints "Hello World"
    cout << "Hello World";

    return 0;
}
```

## Working of Hello World Program in C++

```C++
// main() function: where the execution of
// C++ program begins
```

This line is a comment line. A comment is used to display additional information about the program. A comment does not contain any programming logic. When a comment is encountered by a compiler, the compiler simply skips that line of code.

```C++
#include <iostream>
```

The #include is a preprocessor directive tells the compiler to include the content of a file in the source code. For example, #include<iostream> tells the compiler to include the input-output library which contains all C++’s input/output library functions.

```C++
using namespace std
```

This is used to import the entity of the std namespace into the current namespace of the program. It is basically the space where all the inbuilt features of C++ are declared. For example, std::cout.

```C++
int main() { }
```

The main() function is the entry point of every C++ program, no matter where the function is located in the program. The opening braces '{' indicates the beginning of the main function and the closing braces '}' indicates the ending of the main function.

```C++
cout << "Hello World";
```

The cout is a tool (object) that is used to display output on the console screen. Everything followed by the character << in double quotes ” ” is displayed on the output screen. The semi-colon character at the end of the statement is used to indicate that the statement is ending there.

```C++
return 0
```

This statement is used to return a value from a function and indicates the finishing of a function. Here, it is used to sent the signal of successful execution of the main function.

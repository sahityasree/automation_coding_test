## dir(),help,__import__ functions in python ##
**Ref python program is:** dirfunc.py and help,import.py 

### dir() function :-###
dir() is a powerful inbuilt function in Python3, which returns list of the attributes and methods of any object (say functions , modules, strings, lists, dictionaries etc.)

**Syntax :** dir({object})

**Parameters :** object[optional] : Takes object name.

**Applications :-**

- The dir() has it’s own set of uses. It usually used for debugging purposes in simple day to day programs, and even in large projects taken up by a team of developers. The capability of dir() to list out all the attributes of the parameter passed, is really useful when handling a lot of classes and functions, separately.
- The dir() function can also list out all the available attributes for a module/list/dictionary. So, it also gives us information on the operations we can perform with the available list or module, which can be very useful when having little to no information about the module. It also helps to know new modules faster.

**Returns :-**
dir() tries to return a valid list of attributes of the object it is called upon. Also, dir() function behaves rather differently with different type of objects, as it aims to produce the most relevant one, rather than the complete information.

- For Class Objects, it returns a list of names of all the valid attributes and base attributes as well.
- For Modules/Library objects, it tries to return a list of names of all the attributes, contained in that module.
- If no parameters are passed it returns a list of names in the current local scope.

### help() function :- ###
The help() method calls the built-in Python help system.

**Syntax :** help(object).

**Parameter :** The help() method takes maximum of one parameter.

Object (optional) - you want to generate the help of the given object.

**How help() works in Python ?**

The help() method is used for interactive use. It's recommenced to try it in your interpreter when you need help to write Python program and use Python modules.

**object is passed to help() (not a string)**

If String is passed as an argument, name of a module, function, class, method, keyword, or documentation topic, and a help page is printed.help(list),help(dict),help(print),help([1,2,3]) are showed in python program.

**string is passed as an argument to help()**

If string is passed as an argument, the given string is looked up as the name of a module, function, class, method, keyword, or documentation topic, and a help page is printed.help('random thing'),help('print'),help('def'),help('math.pow')

**no argument is passed to help()**

If no argument is passed, Python's help utility (interactive help system) starts on the console.

help() : help>'print'

### __import__() function: ###

The import() is an advanced function that is called by the import statement.

**Syntax :**import(name, globals=None, locals=None, fromlist=(), level=0)

**Parameters :**

- name – name of the module you want to import.
- globals and locals  determines how to interpret name.
- fromlist – objects or submodules that should be imported by name.
- level – specifies whether to use absolute or relative imports.

**Use of import():**

This import() function is not necessary in everyday Python programming. It is rarely used and often discouraged.
This function can be used to changed the semantics of import statement as import statement calls this function. However, it is always better to use import hooks.
If you want to import a module by name, use importlib.import_module() instead.

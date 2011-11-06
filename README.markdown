# envparser
This is just a simple environment configurations parser. It aims to provide an easier way to parse configuration files
organized in a certain way that makes it easy to use as a basis for different environments.

It's based on the ConfigParser module, but aims to be easier and simpler to use, although being less flexible.

## Installing
If you use virtualenv:

```
$ pip install envparser
```

If you don't and your site-packages are shared for all users in your machine:

```
$ sudo pip install envparser
```

If you don't have any idea of what pip is (shame on you!), or can't use it:

```
$ easy_install envparser
```

or, after downloading ([here](http://pypi.python.org/pypi/envparser/)) and unpacking the .tar.gz/.zip package:

```
$ python setup.py install
```

### Development requirements
If you wish to contribute to the project as a developer, just install the requirements file included in the project with pip.

## Examples

Using only one configuration file:

```cfg
# /home/myuser/myproject/mybaseconfiguration.cfg
[DEFAULT]
name: John Doe
age: 30
salary: 560.00
```

```python
import envparser

parser = envparser.Parser('/home/myuser/myproject/mybaseconfiguration.cfg')
parser.get('name') # prints "John Doe"
parser.getint('age') # prints 30
parser.getfloat('salary') # prints 560.00
```
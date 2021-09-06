# C03P05 - Simple template engine

We are working on a piece of software that needs a simple templating engine, so we can send simple templated emails.

In a module called `template.py` implement the following class:

```python
class TemplateEngine:
    def __init__(self, template):
        pass

    def render(self, **context):
        """
        Renders `self.template` by interpolating the variables with data from `context`.

        Raise `TemplatEngineError` if not all variables, present in `self.template`, have values in `context`.
        """

    def extract_variables(self):
        """
        Returns a list of all variables names, that are present in `self.template`
        """
```

The class should behave as follows:

```python
template = "Hello there, {{ x }}"
engine = TemplateEngine(template)

rendered = engine.render(x="general Kenobi.")
print(rendered)  # "Hello there, general Kenobi."

variables = engine.extract_variables()
print(variables)  # ["x"]
```

**Few important things:**

1. The engine should support multiline strings.
1. All of those are valid: `{{x}}`, `{{ x}}`, `{{ x }}`, `{{         x}}`, etc. You can have arbitrary whitespace between `{{`, the variable name and `}}`.
1. One variable can occur in multiple places in the template.
1. Behavior of the `render` method is described in the docstring.
1. In order to show that your implementation is working as expected, **cover the `TemplateEngine` implementation with tests**, placed in `template_tests.py`

**Few more examples**

```python
template = """
Hello {{ first_name }} {{ last_name }},

I hope this email finds you well.

We are currently running a promotion for {{ product }}.

You can get your discount {{ here }}
"""

engine = TemplateEngine(template)

variables = engine.extract_variables()
print(variables)  # ["first_name", "last_name", "product", "here"]

rendered = engine.render(
  first_name="Ivan",
  last_name="Ivanov",
  product="Python course",
  here="https://hackbulgaria.com/python-101-forever"
)
print(rendered)
```

The rendered version should look like this:

```
Hello Ivan Ivanov,

I hope this email finds you well.

We are currently running a promotion for Python course.

You can get your discount https://hackbulgaria.com/python-101-forever
```

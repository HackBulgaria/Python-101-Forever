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

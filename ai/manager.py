class AIManager:

    def __init__(self):

        self.provider=None

    def set(self,provider):

        self.provider=provider

    def ask(self,prompt):

        if self.provider is None:

            raise Exception("No AI Provider")

        return self.provider.ask(prompt)
class SWAPIClient():
    def __init__(self):
        # Nothing to do yet
        pass
    
    def get_data(self, character_name):
        return {}

    def get_swapi_data(self):
        character_data = self.get_data("Luke Skywalker")
        # Merge with other data? From DB?
        # etc...
        return character_data
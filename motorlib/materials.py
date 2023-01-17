"""Material submodule that contains the material class."""

from .properties import PropertyCollection, FloatProperty, StringProperty, TabularProperty
from .simResult import SimAlert, SimAlertLevel, SimAlertType

class Material(PropertyCollection):
    """Contains the mechanical properties of a material."""
    def __init__(self, matDict=None):
        super().__init__()
        self.props['name'] = StringProperty('Name')
        self.props['density'] = FloatProperty('Density', 'kg/m^3', 1, 25000)

    def getErrors(self):
        """Define errors for materials here. May eventually check max temperature"""
        errors = []
        return errors

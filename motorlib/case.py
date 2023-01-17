"""This submodule houses the case object and functions related to the structural properties of the motor"""
import math

from scipy.optimize import fsolve

from .properties import FloatProperty, PropertyCollection
from . import geometry
from .simResult import SimAlert, SimAlertLevel, SimAlertType

class Case(PropertyCollection):
    """An object that contains the details about a motor's case."""
    def __init__(self):
        super().__init__()
        self.props['simulate_case'] = BooleanProperty('Simulate Case?')
        self.props['thickness'] = FloatProperty('Case Thickness', 'm', 0, 0.0254)
        self.props['length'] = FloatProperty('Case Length', 'm', 0, 10)
        self.props['material'] = FloatProperty('Efficiency', '', 0, 2)
        self.props['outer_diameter'] = FloatProperty('Divergence Half Angle', 'deg', 0, 90)
        self.props['bolt_holes'] = FloatProperty('Convergence Half Angle', 'deg', 0, 90)
        self.props['bolt_effective_diameter'] = FloatProperty('Throat Length', 'm', 0, 0.5)
        self.props['bolt_material'] = FloatProperty('Slag Buildup Coefficient', '(m*Pa)/s', 0, 1e6)

    def getDetailsString(self, lengthUnit='m', weightUnit='kg'):
        """Returns a human-readable string containing some details about the case."""
        return 'Case: {} m long, {} m thick, weighing {} kg'.format(self.props['length'].dispFormat(lengthUnit), self.props['thickness'].dispFormat(lengthUnit), self.props['weight'].dispFormat(weightUnit))

    def calcBurstPressure(self):
        """Returns the pressure at which it is anticipated the case will fail due to hoop rupture. Thin wall calculation is conservative. Using outer diameter is conservative."""
        return stress_yield * thickness/(diameter/2)
        
    def calcBoltShearForce(self):
    

    def getGeometryErrors(self):
        """Returns a list containing any errors with the nozzle's properties."""
        errors = []
        if self.props['throat'].getValue() == 0:
            aText = 'Throat diameter must not be 0'
            errors.append(SimAlert(SimAlertLevel.ERROR, SimAlertType.GEOMETRY, aText, 'Nozzle'))
        if self.props['exit'].getValue() < self.props['throat'].getValue():
            aText = 'Exit diameter must not be smaller than throat diameter'
            errors.append(SimAlert(SimAlertLevel.ERROR, SimAlertType.GEOMETRY, aText, 'Nozzle'))
        if self.props['efficiency'].getValue() == 0:
            aText = 'Efficiency must not be 0'
            errors.append(SimAlert(SimAlertLevel.ERROR, SimAlertType.CONSTRAINT, aText, 'Nozzle'))
        return errors

# This file was automatically generated by SWIG (http://www.swig.org).
# Version 2.0.9
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.



from sys import version_info
if version_info >= (2,6,0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_pinspec', [dirname(__file__)])
        except ImportError:
            import _pinspec
            return _pinspec
        if fp is not None:
            try:
                _mod = imp.load_module('_pinspec', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _pinspec = swig_import_helper()
    del swig_import_helper
else:
    import _pinspec
del version_info
try:
    _swig_property = property
except NameError:
    pass # Python < 2.2 doesn't have 'property'.
def _swig_setattr_nondynamic(self,class_type,name,value,static=1):
    if (name == "thisown"): return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    if (not static):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)

def _swig_setattr(self,class_type,name,value):
    return _swig_setattr_nondynamic(self,class_type,name,value,0)

def _swig_getattr(self,class_type,name):
    if (name == "thisown"): return self.this.own()
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError(name)

def _swig_repr(self):
    try: strthis = "proxy of " + self.this.__repr__()
    except: strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object : pass
    _newclass = 0


INFINITE_HOMOGENEOUS = _pinspec.INFINITE_HOMOGENEOUS
HOMOGENEOUS_EQUIVALENCE = _pinspec.HOMOGENEOUS_EQUIVALENCE
HETEROGENEOUS = _pinspec.HETEROGENEOUS
class Geometry(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Geometry, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Geometry, name)
    __repr__ = _swig_repr
    def __init__(self): 
        this = _pinspec.new_Geometry()
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _pinspec.delete_Geometry
    __del__ = lambda self : None;
    def getNumNeutronsPerBatch(self): return _pinspec.Geometry_getNumNeutronsPerBatch(self)
    def getTotalNumNeutrons(self): return _pinspec.Geometry_getTotalNumNeutrons(self)
    def getNumBatches(self): return _pinspec.Geometry_getNumBatches(self)
    def getNumThreads(self): return _pinspec.Geometry_getNumThreads(self)
    def getSpatialType(self): return _pinspec.Geometry_getSpatialType(self)
    def setNeutronsPerBatch(self, *args): return _pinspec.Geometry_setNeutronsPerBatch(self, *args)
    def setNumBatches(self, *args): return _pinspec.Geometry_setNumBatches(self, *args)
    def setNumThreads(self, *args): return _pinspec.Geometry_setNumThreads(self, *args)
    def setSpatialType(self, *args): return _pinspec.Geometry_setSpatialType(self, *args)
    def setDancoffFactor(self, *args): return _pinspec.Geometry_setDancoffFactor(self, *args)
    def addRegion(self, *args): return _pinspec.Geometry_addRegion(self, *args)
    def runMonteCarloSimulation(self): return _pinspec.Geometry_runMonteCarloSimulation(self)
    def computeBatchStatistics(self): return _pinspec.Geometry_computeBatchStatistics(self)
    def computeScaledBatchStatistics(self): return _pinspec.Geometry_computeScaledBatchStatistics(self)
    def outputBatchStatistics(self, *args): return _pinspec.Geometry_outputBatchStatistics(self, *args)
Geometry_swigregister = _pinspec.Geometry_swigregister
Geometry_swigregister(Geometry)

FUEL = _pinspec.FUEL
MODERATOR = _pinspec.MODERATOR
INFINITE = _pinspec.INFINITE
class Region(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Region, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Region, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _pinspec.new_Region(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _pinspec.delete_Region
    __del__ = lambda self : None;
    def getRegionName(self): return _pinspec.Region_getRegionName(self)
    def getVolume(self): return _pinspec.Region_getVolume(self)
    def getMaterial(self): return _pinspec.Region_getMaterial(self)
    def getRegionType(self): return _pinspec.Region_getRegionType(self)
    def isFuel(self): return _pinspec.Region_isFuel(self)
    def isModerator(self): return _pinspec.Region_isModerator(self)
    def isInfinite(self): return _pinspec.Region_isInfinite(self)
    def getFuelRadius(self): return _pinspec.Region_getFuelRadius(self)
    def getPitch(self): return _pinspec.Region_getPitch(self)
    def setVolume(self, *args): return _pinspec.Region_setVolume(self, *args)
    def setMaterial(self, *args): return _pinspec.Region_setMaterial(self, *args)
    def addTally(self, *args): return _pinspec.Region_addTally(self, *args)
    def setFuelRadius(self, *args): return _pinspec.Region_setFuelRadius(self, *args)
    def setPitch(self, *args): return _pinspec.Region_setPitch(self, *args)
    def setNumBatches(self, *args): return _pinspec.Region_setNumBatches(self, *args)
    def addFuelRingRadius(self, *args): return _pinspec.Region_addFuelRingRadius(self, *args)
    def addModeratorRingRadius(self, *args): return _pinspec.Region_addModeratorRingRadius(self, *args)
    def collideNeutron(self, *args): return _pinspec.Region_collideNeutron(self, *args)
    def computeBatchStatistics(self): return _pinspec.Region_computeBatchStatistics(self)
    def computeScaledBatchStatistics(self, *args): return _pinspec.Region_computeScaledBatchStatistics(self, *args)
    def outputBatchStatistics(self, *args): return _pinspec.Region_outputBatchStatistics(self, *args)
Region_swigregister = _pinspec.Region_swigregister
Region_swigregister(Region)

ELASTIC = _pinspec.ELASTIC
CAPTURE = _pinspec.CAPTURE
FISSION = _pinspec.FISSION
LEAKAGE = _pinspec.LEAKAGE
ISOTROPIC_CM = _pinspec.ISOTROPIC_CM
ISOTROPIC_LAB = _pinspec.ISOTROPIC_LAB
class Isotope(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Isotope, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Isotope, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _pinspec.new_Isotope(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _pinspec.delete_Isotope
    __del__ = lambda self : None;
    def parseName(self): return _pinspec.Isotope_parseName(self)
    def makeFissionable(self): return _pinspec.Isotope_makeFissionable(self)
    def getIsotopeName(self): return _pinspec.Isotope_getIsotopeName(self)
    def getA(self): return _pinspec.Isotope_getA(self)
    def getAlpha(self): return _pinspec.Isotope_getAlpha(self)
    def getN(self): return _pinspec.Isotope_getN(self)
    def getAO(self): return _pinspec.Isotope_getAO(self)
    def getTemperature(self): return _pinspec.Isotope_getTemperature(self)
    def getMuAverage(self): return _pinspec.Isotope_getMuAverage(self)
    def isFissionable(self): return _pinspec.Isotope_isFissionable(self)
    def getNumXSEnergies(self): return _pinspec.Isotope_getNumXSEnergies(self)
    def getElasticXS(self, *args): return _pinspec.Isotope_getElasticXS(self, *args)
    def getElasticAngleType(self): return _pinspec.Isotope_getElasticAngleType(self)
    def getAbsorptionXS(self, *args): return _pinspec.Isotope_getAbsorptionXS(self, *args)
    def getCaptureXS(self, *args): return _pinspec.Isotope_getCaptureXS(self, *args)
    def getFissionXS(self, *args): return _pinspec.Isotope_getFissionXS(self, *args)
    def getTotalXS(self, *args): return _pinspec.Isotope_getTotalXS(self, *args)
    def getTransportXS(self, *args): return _pinspec.Isotope_getTransportXS(self, *args)
    def usesThermalScattering(self): return _pinspec.Isotope_usesThermalScattering(self)
    def isRescaled(self): return _pinspec.Isotope_isRescaled(self)
    def getEnergyGridIndex(self, *args): return _pinspec.Isotope_getEnergyGridIndex(self, *args)
    def retrieveXSEnergies(self, *args): return _pinspec.Isotope_retrieveXSEnergies(self, *args)
    def retrieveXS(self, *args): return _pinspec.Isotope_retrieveXS(self, *args)
    def setIsotopeType(self, *args): return _pinspec.Isotope_setIsotopeType(self, *args)
    def setA(self, *args): return _pinspec.Isotope_setA(self, *args)
    def setAO(self, *args): return _pinspec.Isotope_setAO(self, *args)
    def setN(self, *args): return _pinspec.Isotope_setN(self, *args)
    def setTemperature(self, *args): return _pinspec.Isotope_setTemperature(self, *args)
    def setNumBatches(self, *args): return _pinspec.Isotope_setNumBatches(self, *args)
    def clone(self): return _pinspec.Isotope_clone(self)
    def getCollisionType(self, *args): return _pinspec.Isotope_getCollisionType(self, *args)
    def collideNeutron(self, *args): return _pinspec.Isotope_collideNeutron(self, *args)
    def getDistanceTraveled(self, *args): return _pinspec.Isotope_getDistanceTraveled(self, *args)
    def getThermalScatteringEnergy(self, *args): return _pinspec.Isotope_getThermalScatteringEnergy(self, *args)
    def getNumThermalCDFs(self): return _pinspec.Isotope_getNumThermalCDFs(self)
    def getNumThermalCDFBins(self): return _pinspec.Isotope_getNumThermalCDFBins(self)
    def retrieveThermalCDFs(self, *args): return _pinspec.Isotope_retrieveThermalCDFs(self, *args)
    def retrieveThermalDistributions(self, *args): return _pinspec.Isotope_retrieveThermalDistributions(self, *args)
    def retrieveEtokT(self, *args): return _pinspec.Isotope_retrieveEtokT(self, *args)
    def retrieveEprimeToE(self, *args): return _pinspec.Isotope_retrieveEprimeToE(self, *args)
    def addTally(self, *args): return _pinspec.Isotope_addTally(self, *args)
    def computeBatchStatistics(self): return _pinspec.Isotope_computeBatchStatistics(self)
    def computeScaledBatchStatistics(self, *args): return _pinspec.Isotope_computeScaledBatchStatistics(self, *args)
    def outputBatchStatistics(self, *args): return _pinspec.Isotope_outputBatchStatistics(self, *args)
Isotope_swigregister = _pinspec.Isotope_swigregister
Isotope_swigregister(Isotope)

GRAM_CM3 = _pinspec.GRAM_CM3
NUM_CM3 = _pinspec.NUM_CM3
class Material(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Material, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Material, name)
    __repr__ = _swig_repr
    def __init__(self): 
        this = _pinspec.new_Material()
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _pinspec.delete_Material
    __del__ = lambda self : None;
    def clone(self): return _pinspec.Material_clone(self)
    def getMaterialName(self): return _pinspec.Material_getMaterialName(self)
    def getMaterialNumberDensity(self): return _pinspec.Material_getMaterialNumberDensity(self)
    def getIsotope(self, *args): return _pinspec.Material_getIsotope(self, *args)
    def getDensity(self): return _pinspec.Material_getDensity(self)
    def getIsotopeNumDensity(self, *args): return _pinspec.Material_getIsotopeNumDensity(self, *args)
    def getNumXSEnergies(self): return _pinspec.Material_getNumXSEnergies(self)
    def getTotalMacroXS(self, *args): return _pinspec.Material_getTotalMacroXS(self, *args)
    def getTotalMicroXS(self, *args): return _pinspec.Material_getTotalMicroXS(self, *args)
    def getElasticMacroXS(self, *args): return _pinspec.Material_getElasticMacroXS(self, *args)
    def getElasticMicroXS(self, *args): return _pinspec.Material_getElasticMicroXS(self, *args)
    def getAbsorptionMacroXS(self, *args): return _pinspec.Material_getAbsorptionMacroXS(self, *args)
    def getAbsorptionMicroXS(self, *args): return _pinspec.Material_getAbsorptionMicroXS(self, *args)
    def getCaptureMacroXS(self, *args): return _pinspec.Material_getCaptureMacroXS(self, *args)
    def getCaptureMicroXS(self, *args): return _pinspec.Material_getCaptureMicroXS(self, *args)
    def getFissionMacroXS(self, *args): return _pinspec.Material_getFissionMacroXS(self, *args)
    def getFissionMicroXS(self, *args): return _pinspec.Material_getFissionMicroXS(self, *args)
    def getTransportMicroXS(self, *args): return _pinspec.Material_getTransportMicroXS(self, *args)
    def getTransportMacroXS(self, *args): return _pinspec.Material_getTransportMacroXS(self, *args)
    def retrieveXSEnergies(self, *args): return _pinspec.Material_retrieveXSEnergies(self, *args)
    def retrieveXS(self, *args): return _pinspec.Material_retrieveXS(self, *args)
    def setMaterialName(self, *args): return _pinspec.Material_setMaterialName(self, *args)
    def setDensity(self, *args): return _pinspec.Material_setDensity(self, *args)
    def setNumberDensity(self, *args): return _pinspec.Material_setNumberDensity(self, *args)
    def setAtomicMass(self, *args): return _pinspec.Material_setAtomicMass(self, *args)
    def setNumBatches(self, *args): return _pinspec.Material_setNumBatches(self, *args)
    def addIsotope(self, *args): return _pinspec.Material_addIsotope(self, *args)
    def sampleIsotope(self, *args): return _pinspec.Material_sampleIsotope(self, *args)
    def addTally(self, *args): return _pinspec.Material_addTally(self, *args)
    def collideNeutron(self, *args): return _pinspec.Material_collideNeutron(self, *args)
    def computeBatchStatistics(self): return _pinspec.Material_computeBatchStatistics(self)
    def computeScaledBatchStatistics(self, *args): return _pinspec.Material_computeScaledBatchStatistics(self, *args)
    def outputBatchStatistics(self, *args): return _pinspec.Material_outputBatchStatistics(self, *args)
Material_swigregister = _pinspec.Material_swigregister
Material_swigregister(Material)

EQUAL = _pinspec.EQUAL
LOGARITHMIC = _pinspec.LOGARITHMIC
OTHER = _pinspec.OTHER
MATERIAL = _pinspec.MATERIAL
ISOTOPE = _pinspec.ISOTOPE
REGION = _pinspec.REGION
FLUX = _pinspec.FLUX
COLLISION_RATE = _pinspec.COLLISION_RATE
ELASTIC_RATE = _pinspec.ELASTIC_RATE
ABSORPTION_RATE = _pinspec.ABSORPTION_RATE
CAPTURE_RATE = _pinspec.CAPTURE_RATE
FISSION_RATE = _pinspec.FISSION_RATE
TRANSPORT_RATE = _pinspec.TRANSPORT_RATE
DIFFUSION_RATE = _pinspec.DIFFUSION_RATE
LEAKAGE_RATE = _pinspec.LEAKAGE_RATE
class Tally(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Tally, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Tally, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _pinspec.new_Tally(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _pinspec.delete_Tally
    __del__ = lambda self : None;
    def getTallyName(self): return _pinspec.Tally_getTallyName(self)
    def getNumBins(self): return _pinspec.Tally_getNumBins(self)
    def getBinEdges(self): return _pinspec.Tally_getBinEdges(self)
    def getBinCenters(self): return _pinspec.Tally_getBinCenters(self)
    def getBinDelta(self, *args): return _pinspec.Tally_getBinDelta(self, *args)
    def getBinSpacingType(self): return _pinspec.Tally_getBinSpacingType(self)
    def getTallyDomainType(self): return _pinspec.Tally_getTallyDomainType(self)
    def getTallyType(self): return _pinspec.Tally_getTallyType(self)
    def getTallies(self): return _pinspec.Tally_getTallies(self)
    def getTally(self, *args): return _pinspec.Tally_getTally(self, *args)
    def getNumTallies(self, *args): return _pinspec.Tally_getNumTallies(self, *args)
    def getMaxTally(self): return _pinspec.Tally_getMaxTally(self)
    def getMinTally(self): return _pinspec.Tally_getMinTally(self)
    def getBinIndex(self, *args): return _pinspec.Tally_getBinIndex(self, *args)
    def retrieveTallyEdges(self, *args): return _pinspec.Tally_retrieveTallyEdges(self, *args)
    def retrieveTallyCenters(self, *args): return _pinspec.Tally_retrieveTallyCenters(self, *args)
    def retrieveTallyMu(self, *args): return _pinspec.Tally_retrieveTallyMu(self, *args)
    def retrieveTallyVariance(self, *args): return _pinspec.Tally_retrieveTallyVariance(self, *args)
    def retrieveTallyStdDev(self, *args): return _pinspec.Tally_retrieveTallyStdDev(self, *args)
    def retrieveTallyRelErr(self, *args): return _pinspec.Tally_retrieveTallyRelErr(self, *args)
    def getNumBatches(self): return _pinspec.Tally_getNumBatches(self)
    def getBatchMu(self): return _pinspec.Tally_getBatchMu(self)
    def getBatchVariance(self): return _pinspec.Tally_getBatchVariance(self)
    def getBatchStdDev(self): return _pinspec.Tally_getBatchStdDev(self)
    def getBatchRelativeError(self): return _pinspec.Tally_getBatchRelativeError(self)
    def setBinSpacingType(self, *args): return _pinspec.Tally_setBinSpacingType(self, *args)
    def setBinEdges(self, *args): return _pinspec.Tally_setBinEdges(self, *args)
    def generateBinEdges(self, *args): return _pinspec.Tally_generateBinEdges(self, *args)
    def setNumBatches(self, *args): return _pinspec.Tally_setNumBatches(self, *args)
    def clone(self): return _pinspec.Tally_clone(self)
    def generateBinCenters(self): return _pinspec.Tally_generateBinCenters(self)
    def tally(self, *args): return _pinspec.Tally_tally(self, *args)
    def weightedTally(self, *args): return _pinspec.Tally_weightedTally(self, *args)
    def normalizeTallies(self, *args): return _pinspec.Tally_normalizeTallies(self, *args)
    def computeBatchStatistics(self): return _pinspec.Tally_computeBatchStatistics(self)
    def computeScaledBatchStatistics(self, *args): return _pinspec.Tally_computeScaledBatchStatistics(self, *args)
    def outputBatchStatistics(self, *args): return _pinspec.Tally_outputBatchStatistics(self, *args)
Tally_swigregister = _pinspec.Tally_swigregister
Tally_swigregister(Tally)

class neutron(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, neutron, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, neutron, name)
    __repr__ = _swig_repr
    __swig_setmethods__["_batch_num"] = _pinspec.neutron__batch_num_set
    __swig_getmethods__["_batch_num"] = _pinspec.neutron__batch_num_get
    if _newclass:_batch_num = _swig_property(_pinspec.neutron__batch_num_get, _pinspec.neutron__batch_num_set)
    __swig_setmethods__["_x"] = _pinspec.neutron__x_set
    __swig_getmethods__["_x"] = _pinspec.neutron__x_get
    if _newclass:_x = _swig_property(_pinspec.neutron__x_get, _pinspec.neutron__x_set)
    __swig_setmethods__["_y"] = _pinspec.neutron__y_set
    __swig_getmethods__["_y"] = _pinspec.neutron__y_get
    if _newclass:_y = _swig_property(_pinspec.neutron__y_get, _pinspec.neutron__y_set)
    __swig_setmethods__["_z"] = _pinspec.neutron__z_set
    __swig_getmethods__["_z"] = _pinspec.neutron__z_get
    if _newclass:_z = _swig_property(_pinspec.neutron__z_get, _pinspec.neutron__z_set)
    __swig_setmethods__["_mu"] = _pinspec.neutron__mu_set
    __swig_getmethods__["_mu"] = _pinspec.neutron__mu_get
    if _newclass:_mu = _swig_property(_pinspec.neutron__mu_get, _pinspec.neutron__mu_set)
    __swig_setmethods__["_phi"] = _pinspec.neutron__phi_set
    __swig_getmethods__["_phi"] = _pinspec.neutron__phi_get
    if _newclass:_phi = _swig_property(_pinspec.neutron__phi_get, _pinspec.neutron__phi_set)
    __swig_setmethods__["_energy"] = _pinspec.neutron__energy_set
    __swig_getmethods__["_energy"] = _pinspec.neutron__energy_get
    if _newclass:_energy = _swig_property(_pinspec.neutron__energy_get, _pinspec.neutron__energy_set)
    __swig_setmethods__["_weight"] = _pinspec.neutron__weight_set
    __swig_getmethods__["_weight"] = _pinspec.neutron__weight_get
    if _newclass:_weight = _swig_property(_pinspec.neutron__weight_get, _pinspec.neutron__weight_set)
    __swig_setmethods__["_alive"] = _pinspec.neutron__alive_set
    __swig_getmethods__["_alive"] = _pinspec.neutron__alive_get
    if _newclass:_alive = _swig_property(_pinspec.neutron__alive_get, _pinspec.neutron__alive_set)
    __swig_setmethods__["_in_fuel"] = _pinspec.neutron__in_fuel_set
    __swig_getmethods__["_in_fuel"] = _pinspec.neutron__in_fuel_get
    if _newclass:_in_fuel = _swig_property(_pinspec.neutron__in_fuel_get, _pinspec.neutron__in_fuel_set)
    def __init__(self): 
        this = _pinspec.new_neutron()
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _pinspec.delete_neutron
    __del__ = lambda self : None;
neutron_swigregister = _pinspec.neutron_swigregister
neutron_swigregister(neutron)


def initializeNewNeutron():
  return _pinspec.initializeNewNeutron()
initializeNewNeutron = _pinspec.initializeNewNeutron
class Fissioner(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Fissioner, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Fissioner, name)
    __repr__ = _swig_repr
    def __init__(self): 
        this = _pinspec.new_Fissioner()
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _pinspec.delete_Fissioner
    __del__ = lambda self : None;
    def getNumBins(self): return _pinspec.Fissioner_getNumBins(self)
    def setNumBins(self, *args): return _pinspec.Fissioner_setNumBins(self, *args)
    def setEMax(self, *args): return _pinspec.Fissioner_setEMax(self, *args)
    def buildCDF(self): return _pinspec.Fissioner_buildCDF(self)
    def wattSpectrum(self, *args): return _pinspec.Fissioner_wattSpectrum(self, *args)
    def emitNeutronMeV(self): return _pinspec.Fissioner_emitNeutronMeV(self)
    def emitNeutroneV(self): return _pinspec.Fissioner_emitNeutroneV(self)
    def retrieveCDF(self, *args): return _pinspec.Fissioner_retrieveCDF(self, *args)
    def retrieveCDFEnergies(self, *args): return _pinspec.Fissioner_retrieveCDFEnergies(self, *args)
Fissioner_swigregister = _pinspec.Fissioner_swigregister
Fissioner_swigregister(Fissioner)

DEBUG = _pinspec.DEBUG
INFO = _pinspec.INFO
NORMAL = _pinspec.NORMAL
WARNING = _pinspec.WARNING
CRITICAL = _pinspec.CRITICAL
RESULT = _pinspec.RESULT
ERROR = _pinspec.ERROR

def log_setlevel(*args):
  return _pinspec.log_setlevel(*args)
log_setlevel = _pinspec.log_setlevel

def log_printf(*args):
  return _pinspec.log_printf(*args)
log_printf = _pinspec.log_printf
# This file is compatible with both classic and new-style classes.

cvar = _pinspec.cvar


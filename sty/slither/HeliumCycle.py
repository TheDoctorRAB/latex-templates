import convert

class Fluid:
    R = 8.3145 #kJ/kmol-K
    cPs = {'helium': 5.1926,
           'argon': 0.5203,
           'neon': 1.0299,
           'air':1.005,
           'hydrogen':14.307}
    MWs = {'helium': 4.003,
           'argon': 39.948,
           'neon': 20.183,
           'air':28.97,
           'hydrogen':2.016}

    def __init__(self,gas):
        self.cP = Fluid.cPs[gas] #kJ/kg-K
        self.MW = Fluid.MWs[gas]
        self.specR = self.R/self.MW #kJ/kg-K
        self.cV = self.cP-self.specR #kJ/kg-K
        self.gamma = self.cP/self.cV
        self.gamma_bar = (self.gamma-1)/self.gamma


############################################################
class State:
    MASSFLOW = 0 #kg/s

    states = {1:'Compressor Inlet',
              2:'Compressor Outlet',
              3:'Expander Inlet',
              4:'Expander Outlet'}

    lowP,highP = 0.93,7
    temperatures = {1:25,
                    2:'???',
                    3:900,
                    4:'???'} #degC

    pressures = {1:lowP,
                 2:highP,
                 3:highP,
                 4:lowP} #MPa

    list = []

    def __init__(self, stream):
        self.stream = stream
        self.name = State.states[stream]
        self.pressure = State.pressures[stream]
        self.temperature = State.temperatures[stream]
        State.list.append(self)


    def get_info(self):
        print(f'Stream {self.stream} is the {self.name}. T = {round(self.temperature,1)} degC, P= {self.pressure} MPa ')

    @classmethod
    def carnot_efficiency(cls):
        hotT, coldT = max(stream.temperature for stream in cls.list), min(stream.temperature for stream in cls.list)
        hotT, coldT = convert.Temperature(hotT,'C','K'), convert.Temperature(coldT,'C','K')
        eta = 100*(1-coldT/hotT)
        eta = round(eta,2)
        print(f'Carnot Efficiency: {eta}%')

    @classmethod
    def massflow(cls):
        print(f'Mass Flow Rate {round(cls.MASSFLOW,1)} kg/s')

##################################
class Equipment:
    list=[]

    def __init__(self, inlet, outlet):
        self.inlet = inlet
        self.outlet = outlet
        Equipment.list.append(self)

class Work(Equipment):
    POWER = 0

    efficiencies = {'compressor': 0.9,
                    'expander': 0.9}

    eff_exponent = {'compressor': -1,
                    'expander': 1}


    @classmethod
    def net_power(cls):
        net = round(Heat.POWER_NET,1)
        print(f'Net Shaft Power: {net} MW' )

    def __init__(self, inlet, outlet, descr):
        super().__init__(inlet, outlet)
        self.descr = descr
        self.work = '???'

    def shaft_work(self,gas):
        inT = convert.Temperature(self.inlet.temperature,'C','K') #K
        outTrev = inT*(self.outlet.pressure/self.inlet.pressure)**gas.gamma_bar #K
        self.work = gas.cP*(inT-outTrev)*Work.efficiencies[self.descr]**Work.eff_exponent[self.descr]
        return self.work

    def outT(self, gas):
        return self.inlet.temperature - self.shaft_work(gas)/gas.cP

    def find_power(self):
        self.power = self.work*State.MASSFLOW
        self.power = convert.Metric(self.power, 'k', 'M')
        Work.POWER +=self.power
        self.power = round(self.power,1)

    def get_info(self):
        print(f'{self.descr}: {self.power} MW')

class Heat(Equipment):
    powers = {'reactor': 600,
             'cooler': '???'}

    POWER_IN = POWER_NET = powers['reactor']

    def __init__(self, inlet, outlet, descr):
        super().__init__(inlet, outlet)
        self.descr = descr
        self.power = Heat.powers[descr]


    def find_massflow(self,gas):
        State.MASSFLOW = convert.Metric(self.power,'M','k')/(gas.cP*(self.outlet.temperature-self.inlet.temperature))

    def find_power(self,gas):
        self.power = State.MASSFLOW*gas.cP*(self.outlet.temperature-self.inlet.temperature)
        self.power = convert.Metric(self.power,'k','M')
        Heat.POWER_NET+=self.power
        self.power = round(self.power,1)

    def get_info(self):
        print (f'{self.descr}: {self.power} MW')

    @classmethod
    def thermal_efficiency(cls):
        eta = cls.POWER_NET/cls.POWER_IN*100
        eta = round(eta,2)
        print(f'Thermal Efficiency: {eta}%')
############################################################
def main():
    #Initialize Fluids
    helium = Fluid('helium')
    argon  = Fluid('argon')
    neon = Fluid('neon')
    air = Fluid('air')
    hydrogen = Fluid('hydrogen')
    GAS = hydrogen

    #Initialize Streams
    compressorIn = State(1)
    compressorOut = State(2)
    expanderIn = State(3)
    expanderOut = State(4)

    #Initialize Equipment
    compressor = Work(compressorIn,compressorOut,'compressor')
    expander = Work(expanderIn,expanderOut,'expander')
    reactor = Heat(compressorOut,expanderIn,'reactor')
    cooler = Heat(expanderOut,compressorIn,'cooler')

    #Solve Unknown States
    compressorOut.temperature = compressor.outT(GAS)
    expanderOut.temperature = expander.outT(GAS)

    #Solve Powers
    reactor.find_massflow(GAS)
    cooler.find_power(GAS)
    compressor.find_power()
    expander.find_power()

def print_out():
    for stream in State.list:
        stream.get_info()

    State.massflow()

    for equipment in Equipment.list:
        equipment.get_info()

    Work.net_power()

    Heat.thermal_efficiency()
    State.carnot_efficiency()


if __name__ == '__main__':
    main()
    print_out()

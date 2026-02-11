designFile = "D:/HardWare Reppos/ALTIUM-reppo/Documents/MP3_player/PDNAnalyzer_Output/MP3_Player/odb.tgz"

powerNets = ["+5", "+3V3", "+3V3A"]

groundNets = ["GND"]

excitation = [
{
"id": "0",
"type": "source",
"power_pins": [ ("J1", "2"), ("J1", "1") ],
"ground_pins": [ ("J1", "11"), ("J1", "12") ],
"voltage": 5,
"Rpin": 0,
}
,
{
"id": "1",
"type": "load",
"power_pins": [ ("D1", "2") ],
"ground_pins": [ ("R1", "2") ],
"current": 0.01,
"Rpin": 10,
}
,
{
"id": "2",
"type": "load",
"power_pins": [ ("U2", "1"), ("U2", "24"), ("U2", "36"), ("U2", "48") ],
"ground_pins": [ ("U2", "23"), ("U2", "35"), ("U2", "47") ],
"current": 0.056,
"Rpin": 6.122448979591838,
}
,
{
"id": "3",
"type": "load",
"power_pins": [ ("J16", "4") ],
"ground_pins": [ ("J16", "6") ],
"current": 0.01,
"Rpin": 10,
}
,
{
"id": "4",
"type": "load",
"power_pins": [ ("U2", "9") ],
"ground_pins": [ ("U2", "8") ],
"current": 0.002,
"Rpin": 50,
}
,
{
"id": "5",
"type": "load",
"power_pins": [ ("U1", "2") ],
"ground_pins": [ ("U1", "1") ],
"current": 0.0001,
"Rpin": 1000,
}
]


voltage_regulators = [
{
"id": "6",
"type": "linear",

"in": [ ("U1", "2") ],
"out": [ ("U1", "3") ],
"ref": [ ("U1", "1") ],

"v2": -1.7000000000000002,
"i1": 2E-06,
"Ro": 0,
"Rpin": 0,
}
,
{
"id": "7",
"type": "linear",

"in": [ ("FB1", "1") ],
"out": [ ("FB1", "2") ],
"ref": [],

"v2": -0,
"i1": 0,
"Ro": 1E-06,
"Rpin": 0.045,
}
]


# Resistors / Inductors

passives = []


# Material Properties:

tech = [

        {'name': 'TOP_SOLDER', 'DielectricConstant': 3.8, 'Thickness': 3.048E-05},
        {'name': 'TOP_LAYER', 'Conductivity': 47000000, 'Thickness': 3.5000000000000004E-05},
        {'name': 'SUBSTRATE-1', 'DielectricConstant': 4.4, 'Thickness': 0.0002104},
        {'name': 'INT1__GND_', 'Conductivity': 47000000, 'Thickness': 1.52E-05},
        {'name': 'SUBSTRATE-2', 'DielectricConstant': 4.6, 'Thickness': 0.001065},
        {'name': 'INT2__PWR_', 'Conductivity': 47000000, 'Thickness': 1.52E-05},
        {'name': 'SUBSTRATE-3', 'DielectricConstant': 4.4, 'Thickness': 0.0002104},
        {'name': 'BOTTOM_LAYER', 'Conductivity': 47000000, 'Thickness': 3.5000000000000004E-05},
        {'name': 'BOTTOM_SOLDER', 'DielectricConstant': 3.8, 'Thickness': 3.048E-05}

       ]

special_settings = {'removecutoutsize' : 7.8 }


plating_thickness = 0.7
finished_hole_diameters = False

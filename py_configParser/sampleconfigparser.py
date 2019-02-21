print("This code assumes python 3.7.2\n")

print("install localconfig using pip install localconfig - substitue for configparser")
print("configparser reads all values as string. localconfig tries to interpret the value into correct datatype.")
print(" Warning - localconfig does not work for python2\n")

from localconfig import LocalConfig
from configparser import ExtendedInterpolation
import json

config = LocalConfig(interpolation=ExtendedInterpolation())
config._parser.optionxform = str  #Make keys case sensitive. otherwise keys are all interpreted as lowercase strings. so camelcase, uppercase all goes to hell.
config.read("config.ini")
prop = dict(config.items("PROPERTIES"))
print("Iterate over all variables in section PROPERTIES...")
for key, value in prop.items():
    print(key + " " + str(value) + " " + str(type(value)))

print("\nIterate over all variables in section New Section...")
for key, value in config.items('New Section'):
    print(key + " " + str(value) + " " + str(type(value)))

print("\nno special function to read it as list though. have to break a string into a list yourself.")
print("one easy way to do that if you used json-like string as the value for your listKey is to just parse the value as json.")
listKey = json.loads(prop['listkey'])
listKey[4] = "No Longer!!"
listKey[10] = "do"
##### Updating the dict back to reflect a list, not a string ####
prop['listkey'] = listKey
print("listKey " + str(listKey) + " " + str(type(listKey)))

print("\n Now try badListKey")
try:
    badListKey = json.loads(prop['badListKey'])
    print("badListKey " + str(badListKey) + " " + str(type(badListKey)))
except json.decoder.JSONDecodeError as e:
    print("interpreting badListKey as a json threw error. json expects strings to be within quotes\n")

print(" HeterogenousList")
print(" Benefit of using json.loads to interpret string to list intead of using string.split(',')")
print(" is that json.loads will interpret the datatype of each list element correctly.")
hetListKey = json.loads(prop['heterogenousListKey'])
print("hetListKey " + str(hetListKey) + " " + str(type(hetListKey)))
for val in hetListKey:
    print(str(val) + " " + str(type(val)))
prop['heterogenousListKey'] = hetListKey


print("\n Bad HeterogenousList")
try:
    badhetListKey = json.loads(prop['badHeterogenousListKey'])
    print("badhetListKey " + str(badhetListKey) + " " + str(type(badhetListKey)))
    for val in hetListKey:
        print(str(val) + " " + str(type(val)))
except json.decoder.JSONDecodeError as e:
    print("Threw error ! inside config file, for boolean, True is wrong. true is correct\n")

print("In case you want to keep some config in config.ini file and some harcoded in python file, merge the two dicts")
print("While merging, ensure you merge the updated dict - the one where you converted string to lists")
MODEL_DICT = {'firstname': 'devi', 'lastname':'ayyagari', 'height':5}
print(MODEL_DICT)
MODEL_DICT.update(prop)
print(MODEL_DICT)

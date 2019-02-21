import configparser
import sys

value = None
if len(sys.argv) == 1:
    print("No arguments passed.\nUsage: python updateConfig <configFilePath> <Existingkey> <Value> -- This assumes there is only one Section in the file.")
    exit(-1)
elif len(sys.argv) == 2:
    print("No key passed.\nUsage: python updateConfig <configFilePath> <Existingkey> <Value>")
    exit(-1)
elif len(sys.argv) == 3:
    print("No value passed. Using blank.")
    value = ""
else:
    value = sys.argv[3]

filePath = sys.argv[1]
key = sys.argv[2]

config = configparser.ConfigParser(interpolation=configparser.ExtendedInterpolation())
config.read(filePath)
if len(config.sections()) > 1:
    print("Config File has more than one section. Not yet supported")
    exit(-2);

config.set(config.sections()[0], key, value)

with open(filePath, 'wb') as configfile:
    config.write(configfile)

import ConfigParser

config = ConfigParser.RawConfigParser(allow_no_value=True)
config.read("./conf.config")

assert config.sections()
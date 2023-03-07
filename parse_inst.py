def get_instrument_codes():
    inst_data = {}
    instruments = open("InstProgram.csv")
    instruments.readline()
    for data in instruments:
        split_data = data.split(",")
        inst_data[split_data[1]] = int(split_data[0])
    return inst_data

def valid_inst(inst):
    inst_data = {}
    instruments = open("InstProgram.csv")
    instruments.readline()
    for data in instruments:
        split_data = data.split(",")
        inst_data[split_data[1]] = int(split_data[0])
    return inst in inst_data
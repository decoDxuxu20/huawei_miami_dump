#######################################################################################################################################
#   filename        :   gas_sim_msg.py
#
#   author          :   sunbing 00184266
#
#   description     :   list pid
#
#   modify  record  :   2016-01-07 create file
#
#######################################################################################################################################

gas_sim_enum_table = {
	 6:	"USIMM_UPDATEFILE_REQ",
	 7:	"USIMM_READFILE_REQ",
}

sim_gas_enum_table = {
	 6:	"USIMM_UPDATEFILE_CNF",
	 7:	"USIMM_READFILE_CNF",
}

def get_gas_sim_str( MsgId):
    for MsgIdIndex in gas_sim_enum_table.keys():
        if MsgIdIndex == MsgId:
            return gas_sim_enum_table[MsgIdIndex]

    return "none"

def get_sim_gas_str( MsgId):
    for MsgIdIndex in sim_gas_enum_table.keys():
        if MsgIdIndex == MsgId:
            return sim_gas_enum_table[MsgIdIndex]

    return "none"
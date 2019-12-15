#######################################################################################################################################
#   filename        :   gas_apm_msg.py
#
#   author          :   sunbing 00184266
#
#   description     :   list gas css msg
#
#   modify  record  :   2016-01-07 create file
#
#######################################################################################################################################

gas_apm_msg_enum_table = {
0x8740 : "MPH_AS_ACTIVE_DSDS_STATUS_IND",
}

def get_gas_apm_msg_str( MsgId):
    for MsgIdIndex in gas_apm_msg_enum_table.keys():
        if MsgIdIndex == MsgId:
            return gas_apm_msg_enum_table[MsgIdIndex]

    return "none"
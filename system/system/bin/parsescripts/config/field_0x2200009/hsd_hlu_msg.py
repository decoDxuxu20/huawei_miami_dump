#######################################################################################################################################
#   filename        :   hsd_hlu_msg.py
#
#   author          :   j00354216
#
#   description     :   list hsd hlu msg
#
#   modify  record  :   2016-04-27 create file
#
#######################################################################################################################################

hsd_hlu_msg_enum_table = {
0x0001 : "ID_HSD_HLU_START_REQ",
0x0002 : "ID_HLU_HSD_START_CNF",
0x0003 : "ID_HSD_HLU_POWER_OFF_REQ",
0x0004 : "ID_HLU_HSD_POWER_OFF_CNF",
}

def get_hsd_hlu_msg_str( MsgId):
    for MsgIdIndex in hsd_hlu_msg_enum_table.keys():
        if MsgIdIndex == MsgId:
            return hsd_hlu_msg_enum_table[MsgIdIndex]

    return "none"
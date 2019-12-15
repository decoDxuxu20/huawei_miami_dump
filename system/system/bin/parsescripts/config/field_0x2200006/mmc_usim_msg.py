#######################################################################################################################################
#   filename        :   mmc_usim_msg.py
#
#   author          :   fanjing 00179208
#
#   description     :   list mmc usim msg
#
#   modify  record  :   2016-02-01 create file
#
#######################################################################################################################################

mmc_usim_msg_enum_table = {
6 : "USIMM_UPDATEFILE_CNF",
7 : "USIMM_READFILE_CNF",
8 : "USIMM_QUERYFILE_CNF",
}

def get_mmc_usim_msg_str( MsgId):
    for MsgIdIndex in mmc_usim_msg_enum_table.keys():
        if MsgIdIndex == MsgId:
            return mmc_usim_msg_enum_table[MsgIdIndex]

    return "none"
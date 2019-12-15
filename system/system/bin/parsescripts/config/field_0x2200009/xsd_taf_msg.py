#######################################################################################################################################
#   filename        :   xsd_taf_msg.py
#
#   author          :   j00354216
#
#   description     :   list xsd taf msg
#
#   modify  record  :   2016-04-27 create file
#
#######################################################################################################################################

xsd_taf_msg_enum_table = {
0x0000 : "ID_XSD_TAF_NDSS_RESULT_IND",
}

def get_xsd_taf_msg_str( MsgId):
    for MsgIdIndex in xsd_taf_msg_enum_table.keys():
        if MsgIdIndex == MsgId:
            return xsd_taf_msg_enum_table[MsgIdIndex]

    return "none"
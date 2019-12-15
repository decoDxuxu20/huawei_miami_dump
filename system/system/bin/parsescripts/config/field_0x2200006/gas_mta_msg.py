#######################################################################################################################################
#   filename        :   gas_mta_msg.py
#
#   author          :   sunbing 00184266
#
#   description     :   list gas mta msg
#
#   modify  record  :   2016-01-07 create file
#
#######################################################################################################################################

gas_mta_msg_enum_table = {
0x0004 : "ID_RRC_MTA_QRY_NMR_CNF",
0x0019 : "ID_MTA_GRR_NECLL_MONITOR_SET_REQ",
0x001A : "ID_GRR_MTA_NCELL_MONITOR_SET_CNF",
0x001D : "ID_MTA_GRR_JAM_DETECT_REQ",
0x001F : "ID_MTA_RR_CHECK_FREQ_VALIDITY_REQ",
0x0020 : "ID_RRC_MTA_JAM_DETECT_CNF",
0x0021 : "ID_MTA_GRR_FREQLOCK_SET_REQ",
0x0022 : "ID_RRC_MTA_JAM_DETECT_IND",
0x0024 : "ID_RRC_MTA_CHECK_REQ_VALIDITY_CNF",
0x0025 : "ID_MTA_GRR_NETMON_CELL_QRY_REQ",
0x0026 : "ID_RRC_MTA_FREQLOCK_SET_CNF",
0x0027 : "ID_MTA_GRR_NETMON_TA_QRY_REQ",
0x0028 : "ID_RRC_MTA_NETMON_CELL_QRY_CNF",
0x002A : "ID_RRC_MTA_NETMON_TA_QRY_CNF",
0x002B : "ID_MTA_RRC_PLMN_FREQ_QRY_REQ",
0x1009 : "ID_MTA_RRC_PROTECT_PS_IND",
}

def get_gas_mta_msg_str( MsgId):
    for MsgIdIndex in gas_mta_msg_enum_table.keys():
        if MsgIdIndex == MsgId:
            return gas_mta_msg_enum_table[MsgIdIndex]

    return "none"
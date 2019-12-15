#######################################################################################################################################
#   filename        :   was_mta_msg.py
#
#   author          :   sunbing 00184266
#
#   description     :   list MtaRrcInterface.h
#
#   modify  record  :   2016-01-07 create file
#
#######################################################################################################################################

guas_mta_msg_enum_table = {
0x0001 : "ID_RRC_MTA_MSG_POSITION_REQ",
0x0003 : "ID_MTA_RRC_QRY_NMR_REQ",
0x0005 : "ID_MTA_RRC_RESEL_OFFSET_CFG_NTF",
0x0007 : "ID_MTA_WRR_AUTOTEST_QRY_REQ",
0x0009 : "ID_MTA_WRR_CELLINFO_QRY_REQ",
0x000B : "ID_MTA_WRR_MEASRPT_QRY_REQ",
0x000D : "ID_MTA_WRR_FREQLOCK_SET_REQ",
0x000F : "ID_MTA_WRR_RRC_VERSION_SET_REQ",
0x0011 : "ID_MTA_WRR_CELLSRH_SET_REQ",
0x0013 : "ID_MTA_WRR_FREQLOCK_QRY_REQ",
0x0015 : "ID_MTA_WRR_RRC_VERSION_QRY_REQ",
0x0017 : "ID_MTA_WRR_CELLSRH_QRY_REQ",
0x0019 : "ID_MTA_GRR_NCELL_MONITOR_SET_REQ",
0x001B : "ID_MTA_GRR_NCELL_MONITOR_QRY_REQ",
0x001D : "ID_MTA_RRC_JAM_DETECT_REQ",
0x001F : "ID_MTA_RRC_CHECK_FREQ_VALIDITY_REQ",
0x0021 : "ID_MTA_GRR_FREQLOCK_SET_REQ",
0x0023 : "ID_MTA_RRC_NETMON_CELL_QRY_REQ",
0x0025 : "ID_MTA_GRR_NETMON_CELL_QRY_REQ",
0x0027 : "ID_MTA_GRR_NETMON_TA_QRY_REQ",
0x0029 : "ID_MTA_WRR_JAM_DETECT_REQ",
0x002B : "ID_MTA_RRC_PLMN_FREQ_QRY_REQ",
0x002D : "ID_MTA_WRR_CSNR_QRY_REQ",
0x0002 : "ID_MTA_RRC_MSG_POSITION_CNF",
0x0004 : "ID_RRC_MTA_QRY_NMR_CNF",
0x0008 : "ID_WRR_MTA_AUTOTEST_QRY_CNF",
0x000A : "ID_WRR_MTA_CELLINFO_QRY_CNF",
0x000C : "ID_WRR_MTA_MEASRPT_QRY_CNF",
0x000E : "ID_WRR_MTA_FREQLOCK_SET_CNF",
0x0010 : "ID_WRR_MTA_RRC_VERSION_SET_CNF",
0x0012 : "ID_WRR_MTA_CELLSRH_SET_CNF",
0x0014 : "ID_WRR_MTA_FREQLOCK_QRY_CNF",
0x0016 : "ID_WRR_MTA_RRC_VERSION_QRY_CNF",
0x0018 : "ID_WRR_MTA_CELLSRH_QRY_CNF",
0x001A : "ID_GRR_MTA_NCELL_MONITOR_SET_CNF",
0x001C : "ID_GRR_MTA_NCELL_MONITOR_QRY_CNF",
0x001E : "ID_GRR_MTA_NCELL_MONITOR_IND",
0x0020 : "ID_RRC_MTA_JAM_DETECT_CNF",
0x0022 : "ID_RRC_MTA_JAM_DETECT_IND",
0x0024 : "ID_RRC_MTA_CHECK_FREQ_VALIDITY_CNF",
0x0026 : "ID_GRR_MTA_FREQLOCK_SET_CNF",
0x0028 : "ID_GRR_MTA_NETMON_CELL_QRY_CNF",
0x002A : "ID_GRR_MTA_NETMON_TA_QRY_CNF",
0x002C : "ID_RRC_MTA_NETMON_CELL_QRY_CNF",
0x002E : "ID_RRC_MTA_PLMN_FREQ_QRY_CNF",
0x0030 : "ID_WRR_MTA_CSNR_QRY_CNF",
}

def get_guas_mta_msg_str( MsgId):
    for MsgIdIndex in guas_mta_msg_enum_table.keys():
        if MsgIdIndex == MsgId:
            return guas_mta_msg_enum_table[MsgIdIndex]

    return "none"
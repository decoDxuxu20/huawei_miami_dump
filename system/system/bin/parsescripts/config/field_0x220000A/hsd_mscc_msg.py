#######################################################################################################################################
#   filename        :   hsd_mscc_msg.py
#
#   author          :   j00354216
#
#   description     :   list hsd mscc msg
#
#   modify  record  :   2016-01-27 create file
#
#######################################################################################################################################

hsd_mscc_msg_enum_table = {
0x3000 : "ID_MSCC_HSD_START_REQ",
0x3001 : "ID_HSD_MSCC_START_CNF",
0x3002 : "ID_MSCC_HSD_POWER_OFF_REQ",
0x3003 : "ID_HSD_MSCC_POWER_OFF_CNF",
0x3004 : "ID_MSCC_HSD_SYSTEM_ACQUIRE_REQ",
0x3005 : "ID_HSD_MSCC_SYSTEM_ACQUIRE_START_IND",
0x3006 : "ID_HSD_MSCC_SYSTEM_ACQUIRE_CNF",
0x3007 : "ID_HSD_MSCC_SYSTEM_ACQUIRE_END_IND",
0x3008 : "ID_MSCC_HSD_DATA_CALL_START_NTF",
0x3009 : "ID_MSCC_HSD_DATA_CALL_REDIAL_SYS_ACQ_REQ",
0x300A : "ID_HSD_MSCC_DATA_CALL_REDIAL_SYS_ACQ_CNF",
0x300B : "ID_MSCC_HSD_DATA_CALL_SUCC_NTF",
0x300C : "ID_MSCC_HSD_DATA_CALL_END_NTF",
0x300D : "ID_HSD_MSCC_HRPD_IRAT_TO_LTE_NTF",
0x300E : "ID_HSD_MSCC_SESSION_NEG_RSLT_IND",
0x300F : "ID_HSD_MSCC_OVERHEAD_MSG_IND",
0x3010 : "ID_MSCC_HSD_1X_SYS_CHANGE_IND",
0x3011 : "ID_MSCC_HSD_DISABLE_LTE_NTF",
0x3012 : "ID_HSD_MSCC_INTERSYS_START_IND",
0x3013 : "ID_HSD_MSCC_INTERSYS_END_IND",
0x3014 : "ID_MSCC_HSD_QRY_HRPD_SYS_INFO_REQ",
0x3015 : "ID_HSD_MSCC_QRY_HRPD_SYS_INFO_CNF",
0x3016 : "ID_MSCC_HSD_BG_SEARCH_REQ",
0x3017 : "ID_HSD_MSCC_BG_SEARCH_CNF",
0x3018 : "ID_MSCC_HSD_SYS_CFG_REQ",
0x3019 : "ID_HSD_MSCC_SYS_CFG_CNF",
0x301A : "ID_HSD_MSCC_SYSTEM_SYNC_IND",
0x301B : "ID_HSD_MSCC_SESSION_INFO_IND",
0x301C : "ID_MSCC_HSD_POWER_SAVE_REQ",
0x301D : "ID_HSD_MSCC_POWER_SAVE_CNF",
0x301E : "ID_HSD_MSCC_CAS_STATUS_IND",
0x301F : "ID_MSCC_HSD_STOP_BG_SEARCH_REQ",
0x3020 : "ID_HSD_MSCC_STOP_BG_SEARCH_CNF",
0x3021 : "ID_HSD_MSCC_RF_AVAILABLE_IND",
0x3022 : "ID_MSCC_HSD_SRV_ACQ_REQ",
0x3023 : "ID_HSD_MSCC_SRV_ACQ_CNF",
0x3024 : "ID_MSCC_HSD_BEGIN_SESSION_NOTIFY",
0x3025 : "ID_MSCC_HSD_END_SESSION_NOTIFY",
0x3026 : "ID_MSCC_HSD_CFREQLOCK_NTF",
0x3027 : "ID_HSD_MSCC_HRPD_NO_SERVICE_IND",
0x3028 : "ID_MSCC_HSD_HDR_CSQ_SET_REQ",
0x3029 : "ID_HSD_MSCC_HDR_CSQ_SET_CNF",
0x302A : "ID_HSD_MSCC_HDR_CSQ_IND",
0x302B : "ID_MSCC_HSD_ENABLE_LTE_NTF",
0x302C : "ID_HSD_MSCC_STOP_BG_SEARCH_IND",
}

def get_hsd_mscc_msg_str( MsgId):
    for MsgIdIndex in hsd_mscc_msg_enum_table.keys():
        if MsgIdIndex == MsgId:
            return hsd_mscc_msg_enum_table[MsgIdIndex]

    return "none"
#######################################################################################################################################
#   filename        :   regm_mscc_msg.py
#
#   author          :   jiangzhizhou 00354216
#
#   description     :   list regm mscc msg
#
#   modify  record  :   2018-01-30 create file
#
#######################################################################################################################################

regm_mscc_msg_enum_table = {
0x6000 : "ID_MSCC_REGM_IMS_VOICE_CAP_NOTIFY",
0x6002 : "ID_MSCC_REGM_MODE_CHANGE_REQ",
0x6004 : "ID_MSCC_REGM_OTHER_MODEM_DPLMN_NPLMN_INFO_NOTIFY",
0x6006 : "ID_MSCC_REGM_CFPLMN_SET_REQ",
0x6008 : "ID_MSCC_REGM_CFPLMN_QUERY_REQ",
0x600A : "ID_MSCC_REGM_DPLMN_SET_REQ",
0x600C : "ID_MSCC_REGM_BORDER_INFO_SET_REQ",
0x600E : "ID_MSCC_REGM_SRV_INFO_NOTIFY",
0x6010 : "ID_MSCC_REGM_DETACH_REQ",
0x6001 : "ID_REGM_MSCC_ATTACH_REQ",
0x6003 : "ID_REGM_MSCC_SERVICE_STATUS_IND",
0x6005 : "ID_REGM_MSCC_DETACH_IND",
0x6007 : "ID_REGM_MSCC_REG_RESULT_IND",
0x6009 : "ID_REGM_MSCC_PS_REG_CN_RSLT_IND",
0x600B : "ID_REGM_MSCC_DISPLAY_SERVICE_STATUS_IND",
0x600D : "ID_REGM_MSCC_LTE_COMBINED_START_IND",
0x600F : "ID_REGM_MSCC_TAU_END_IND",
0x6011 : "ID_REGM_MSCC_SYS_INFO_IND",
0x6012 : "ID_REGM_MSCC_PS_SERVICE_CONN_STATUS_IND",
0x6013 : "ID_REGM_MSCC_SRV_REJ_IND",
0x6015 : "ID_REGM_MSCC_MM_INFO_IND",
0x6017 : "ID_REGM_MSCC_GPRS_CIPHER_INFO_IND",
0x6019 : "ID_REGM_MSCC_USIM_AUTH_FAIL_IND",
0x601B : "ID_REGM_MSCC_NETWORK_CAPABILITY_INFO_IND",
0x601D : "ID_REGM_MSCC_CS_PAGING_IND",
0x601F : "ID_REGM_MSCC_CS_SERVICE_CONN_STATUS_IND",
0x6021 : "ID_REGM_MSCC_CFPLMN_SET_CNF",
0x6023 : "ID_REGM_MSCC_CFPLMN_QUERY_CNF",
0x6025 : "ID_REGM_MSCC_DPLMN_SET_CNF",
0x6027 : "ID_REGM_MSCC_BORDER_INFO_SET_CNF",
0x6029 : "ID_REGM_MSCC_GPRS_STATE_IND",
0x602B : "ID_REGM_MSCC_CSFB_STATE_INFO_IND",
0x602D : "ID_REGM_MSCC_ATTACH_CNF",
0x602F : "ID_REGM_MSCC_DETACH_CNF",
}

def get_regm_mscc_msg_str( MsgId):
    for MsgIdIndex in regm_mscc_msg_enum_table.keys():
        if MsgIdIndex == MsgId:
            return regm_mscc_msg_enum_table[MsgIdIndex]

    return "none"
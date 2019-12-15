#######################################################################################################################################
#   filename        :   mmc_regm_msg.py
#
#   author          :   jiangzhizhou 00354216
#
#   description     :   list mmc regm msg
#
#   modify  record  :   2018-01-30 create file
#
#######################################################################################################################################

mmc_regm_msg_enum_table = {
0x00 : "ID_MMC_REGM_START_REQ",
0x02 : "ID_MMC_REGM_POWER_OFF_REQ",
0x04 : "ID_MMC_REGM_ENTER_PLMN_SRCH_STATE_REQ",
0x06 : "ID_MMC_REGM_COVERAGE_LOST_NTF",
0x08 : "ID_MMC_REGM_SYS_INFO_NTF",
0x0A : "ID_MMC_REGM_HPLMN_CHANGE_NTF",
0x0C : "ID_MMC_REGM_PROCEDURE_START_NTF",
0x0E : "ID_MMC_REGM_PROCEDURE_END_NTF",
0x10 : "ID_MMC_REGM_STK_REFRESH_NTF",
0x12 : "ID_MMC_REGM_INTERSYS_SUSPEND_REQ",
0x14 : "ID_MMC_REGM_INTERSYS_RESUME_REQ",
0x16 : "ID_MMC_REGM_W_AC_INFO_CHANGE_NTF",
0x18 : "ID_MMC_REGM_INTERSYS_RSLT_NTF",
0x1A : "ID_MMC_REGM_W_LIMIT_SERVICE_CAMP_NTF",
0x1C : "ID_MMC_REGM_LAU_REQ",
0x1E : "ID_MMC_REGM_SRVCC_INFO_NTF",
0x20 : "ID_MMC_REGM_SUSPEND_INFO_CHANGE_NTF",
0x22 : "ID_MMC_REGM_NO_CARD_NTF",
0x24 : "ID_MMC_REGM_VOICE_DOMAIN_CHANGE_NTF",
0x26 : "ID_MMC_REGM_PS_REG_REQ",
0x28 : "ID_MMC_REGM_STEERING_OF_ROAMING_NTF",
0x2A : "ID_MMC_REGM_ENABLE_LTE_EXPIRED_NTF",
0x01 : "ID_REGM_MMC_START_CNF",
0x03 : "ID_REGM_MMC_POWER_OFF_CNF",
0x05 : "ID_REGM_MMC_ENTER_PLMN_SRCH_STATE_CNF",
0x07 : "ID_REGM_MMC_NEED_DISABLE_LTE_IND",
0x09 : "ID_REGM_MMC_REG_RESULT_IND",
0x0B : "ID_REGM_MMC_CSGID_LIST_CHANGE_IND",
0x0D : "ID_REGM_MMC_USER_SPEC_PLMN_REG_RSLT_IND",
0x0F : "ID_REGM_MMC_IMMEDIATE_REPORT_CURR_CELL_SIGN_IND",
0x11 : "ID_REGM_MMC_EPS_SERVICE_RSLT_IND",
0x13 : "ID_REGM_MMC_DATARAN_ATTRI_IND",
0x15 : "ID_REGM_MMC_FPLMN_INFO_IND",
0x17 : "ID_REGM_MMC_NEED_ENABLE_LTE_IND",
0x19 : "ID_REGM_MMC_INTERSYS_SUSPEND_CNF",
0x1B : "ID_REGM_MMC_INTERSYS_RESUME_CNF",
0x1D : "ID_REGM_MMC_FORBLA_CHANGE_IND",
0x1F : "ID_REGM_MMC_DPLMN_SET_IND",
0x21 : "ID_REGM_MMC_CM_SERVICE_IND",
0x23 : "ID_REGM_MMC_PLMN_SEARCH_IND",
0x25 : "ID_REGM_MMC_RPLMN_CHANGED_IND",
0x27 : "ID_REGM_MMC_TIMER_T3247_STATE_IND",
0x29 : "ID_REGM_MMC_EST_IND",
0x2B : "ID_REGM_MMC_MO_ATTACH_RSLT_IND",
0x2D : "ID_REGM_MMC_DETACH_RSLT_IND",
0x2F : "ID_REGM_MMC_INTERSYS_IND",
}

def get_mmc_regm_msg_str( MsgId):
    for MsgIdIndex in mmc_regm_msg_enum_table.keys():
        if MsgIdIndex == MsgId:
            return mmc_regm_msg_enum_table[MsgIdIndex]

    return "none"
#######################################################################################################################################
#   filename        :   was_om_msg.py
#
#   author          :   sunbing 00184266
#
#   description     :   list WasOmInterface.h
#
#   modify  record  :   2016-01-07 create file
#
#######################################################################################################################################

was_om_msg_enum_table = {
0xB000 : "ID_OM_WAS_PRINT_LEVEL_CTRL_REQ",
0xB001 : "ID_WAS_OM_PRINT_LEVEL_CTRL_CNF",
0xB002 : "ID_OM_WAS_FREQ_LOCK_REQ",
0xB003 : "ID_WAS_OM_FREQ_LOCK_CNF",
0xB004 : "ID_OM_WAS_ENCRYPT_REQ",
0xB005 : "ID_WAS_OM_ENCRYPT_CNF",
0xB006 : "ID_OM_WAS_COMPRESS_REQ",
0xB007 : "ID_WAS_OM_COMPRESS_CNF",
0xB008 : "ID_OM_WAS_POWERCTRL_REQ",
0xB009 : "ID_WAS_OM_POWERCTRL_CNF",
0xB010 : "ID_OM_WAS_ACT_OR_SERV_CELL_INFO_REQ",
0xB011 : "ID_WAS_OM_ACT_OR_SERV_CELL_INFO_CNF",
0xB012 : "ID_WAS_OM_ACT_OR_SERV_CELL_INFO_IND",
0xB013 : "ID_OM_WAS_W_NCELL_INFO_REQ",
0xB014 : "ID_WAS_OM_W_NCELL_INFO_CNF",
0xB015 : "ID_WAS_OM_W_NCELL_INFO_IND",
0xB016 : "ID_OM_WAS_G_NCELL_INFO_REQ",
0xB017 : "ID_WAS_OM_G_NCELL_INFO_CNF",
0xB018 : "ID_WAS_OM_G_NCELL_INFO_IND",
0xB019 : "ID_OM_WAS_W_CELL_CHG_INFO_REQ",
0xB01A : "ID_WAS_OM_W_CELL_CHG_INFO_CNF",
0xB01B : "ID_WAS_OM_W_CELL_CHG_INFO_IND",
0xB01C : "ID_OM_WAS_UE_STATE_REQ",
0xB01D : "ID_OM_WAS_UE_STATE_CNF",
0xB01E : "ID_WAS_OM_UE_STATE_IND",
0XB020 : "ID_OM_WAS_OTA_REQ",
0XB021 : "ID_WAS_OM_OTA_CNF",
0XB022 : "ID_WAS_OM_OTA_IND",
0XB027 : "ID_WAS_OM_WCDMA_WORK_MODE_REQ",
0XB028 : "ID_OM_WAS_WCDMA_WORK_MODE_CNF",
0xB035 : "ID_WAS_FREQ_LOCK_IND",
0xeeee : "ID_WAS_FIXED_DATA_RECUR",
0xB037 : "ID_WAS_ALL_DATA_IND",
0xaaaa : "ID_OM_WAS_CONNECTED_IND",
0xaaab : "ID_WAS_OM_CONNECTED_CNF",
0xB040 : "ID_WAS_PRINT_MSG",
0xB041 : "ID_WAS_SIB3_SIB4_IND",
0xB042 : "ID_WAS_CELL_LIST_IND",
0xB043 : "ID_WAS_SIB19_INFO_IND",
0xB049 : "ID_WAS_LAST_SMC_INTEGRITY_F9_IND",
0xB050 : "ID_WAS_AFC_INFO_IND",
0xB051 : "ID_WAS_JAM_DETECT_INFO_IND",
0xB052 : "ID_WAS_LTE_UNSUPPORT_FREQ",
0xB053 : "ID_WAS_CSS_BAND_INFO_IND",
0xB054 : "ID_WAS_FFT_PLMN_BAND_INFO_IND",
0xB055 : "ID_WAS_OM_CELL_INDI_OFFSET_MODIFY_INFO_IND",
0xB056 : "ID_WAS_CSS_PRE_FREQ_INFO_IND",
0xB057 : "ID_WAS_CSS_PRE_BAND_INFO_IND",
0xB058 : "ID_WAS_AM_SRB_SEND_STATE_INFO_IND",
0xB060 : "ID_OM_WAS_L_NCELL_INFO_REQ",
0xB061 : "ID_WAS_OM_L_NCELL_INFO_CNF",
0xB062 : "ID_WAS_OM_L_NCELL_INFO_IND",
0xB063 : "ID_OM_WAS_SECOND_CELL_INFO_REQ",
0xB064 : "ID_WAS_OM_SECOND_CELL_INFO_CNF",
0xB065 : "ID_WAS_OM_SECOND_CELL_INFO_IND",
0xB066 : "ID_OM_WAS_TIMER_EVENT_REQ",
0xB067 : "ID_WAS_OM_TIMER_EVENT_CNF",
}

def get_was_om_msg_str( MsgId):
    for MsgIdIndex in was_om_msg_enum_table.keys():
        if MsgIdIndex == MsgId:
            return was_om_msg_enum_table[MsgIdIndex]

    return "none"
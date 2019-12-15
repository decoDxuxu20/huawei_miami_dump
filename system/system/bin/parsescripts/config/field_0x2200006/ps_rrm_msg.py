#######################################################################################################################################
#   filename        :   ps_rrm_msg.py
#
#   author          :   fanjing 00179208
#
#   description     :   list ps rrm msg
#
#   modify  record  :   2016-02-01 create file
#
#######################################################################################################################################

ps_rrm_msg_enum_table = {
0x0001 : "ID_PS_RRM_RADIO_RESOURCE_APPLY_REQ",
0x0002 : "ID_RRM_PS_RADIO_RESOURCE_APPLY_CNF",
0x0003 : "ID_PS_RRM_RADIO_RESOURCE_RELEASE_IND",
0x0004 : "ID_RRM_PS_RADIO_RESOURCE_OCCUPY_REQ",
0x0005 : "ID_PS_RRM_RADIO_RESOURCE_OCCUPY_CNF",
0x0006 : "ID_PS_RRM_PROTECT_PS_IND",
0x0007 : "ID_PS_RRM_DEPROTECT_PS_IND",
0x0008 : "ID_PS_RRM_REGISTER_IND",
0x0009 : "ID_PS_RRM_DEREGISTER_IND",
0x000a : "ID_RRM_PS_STATUS_IND",
0x000b : "ID_RRM_PS_ERROR_IND",
0x000c : "ID_RRM_PS_ABNORMAL_STATUS_IND",
0x000d : "ID_PS_RRM_PROTECT_SIGNAL_IND",
0x000e : "ID_PS_RRM_DEPROTECT_SIGNAL_IND",
0x000f : "ID_RRM_PS_USED_TASK_STATUS_IND",
0x0010 : "ID_PS_RRM_RAT_COMBINED_MODE_IND",
0x0011 : "ID_PS_RRM_MODEM_CAP_UPDATE_REQ",
0x0012 : "ID_RRM_PS_MODEM_CAP_UPDATE_CNF",
0x0013 : "ID_RRM_PS_RADIO_RESOURCE_CHECK_IND",
0x0014 : "ID_PS_RRM_SIM_STATUS_IND",
0x0015 : "ID_PS_RRM_INIT_IND",
0x0016 : "ID_PS_RRM_START_REQ",
0x0017 : "ID_RRM_PS_START_CNF",
0x0018 : "ID_PS_RRM_POWER_OFF_IND",
0X0019 : "ID_RRM_PS_DS_MODE_SET_IND",
0x001a : "ID_PS_RRM_IMS_CALL_STATUS_IND",
0x001b : "ID_PS_RRM_CL_MODE_LTE_ONLY_MODE_IND",
0x001c : "ID_RRM_PS_DSDS_STATUS_IND",
0x001d : "ID_PS_RRM_DSDS_REGISTER_IND",
0x001e : "ID_PS_RRM_DSDS_DEREGISTER_IND",
0x001f : "ID_PS_RRM_DSDS_BAND_IND",
0x0020 : "ID_PS_RRM_RAT_PLMN_NOTIFY",
0x0021 : "ID_RRM_PS_DSDS_STATE_NOTIFY",
0x0022 : "ID_RRM_PS_OCCUPY_CTRL_CHECK_IND",
}

def get_ps_rrm_msg_str( MsgId):
    for MsgIdIndex in ps_rrm_msg_enum_table.keys():
        if MsgIdIndex == MsgId:
            return ps_rrm_msg_enum_table[MsgIdIndex]

    return "none"
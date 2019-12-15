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
	0x0013 : "ID_RRM_PS_RADIO_RESOURCE_CHECK_IND",
}

def get_ps_rrm_msg_str( MsgId):
    for MsgIdIndex in ps_rrm_msg_enum_table.keys():
        if MsgIdIndex == MsgId:
            return ps_rrm_msg_enum_table[MsgIdIndex]

    return "unknown"
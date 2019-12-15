#######################################################################################################################################
#   filename        :   cproc_rm_msg.py
#
#   author          :   linchengwen 00322531
#
#   description     :   list cproc rm msg
#
#   modify  record  :   2016-03-10 create file
#
#######################################################################################################################################

cproc_rm_msg_enum_table = {
    0xF230  : "ID_CPROC_RM_INIT_REQ",
    0xF231  : "ID_CPROC_RM_TIMING_UPDATE_REQ",
    0xF232  : "ID_CPROC_RM_INIT_CNF",
    0xF233  : "ID_CPROC_RM_ACTIVITY_REQ",
    0xF234  : "ID_CPROC_RM_ACTIVITY_IND",
    0xF235  : "ID_CPROC_RM_ASSIGN_FAIL_IND",
    0xF236  : "ID_CPROC_RM_PAGING_REQ",
    0xF237  : "ID_CPROC_RM_ACTIVITY_SUSPEND_IND",
    0xF238  : "ID_CPROC_RM_ACTIVITY_SUSPEND_RSP",
    0xF239  : "ID_CPROC_RM_ACTIVITY_REL_REQ",
    0xF23A  : "ID_CPROC_RM_BT_CHANNEL_IND",
    0xF23B  : "ID_CPROC_RM_RAT_CAP_UPDATE_REQ",
    0xF23C  : "ID_CPROC_RM_RAT_CAP_UPDATE_CNF",
    0xF23D  : "ID_CPROC_RM_SAR_CTRL_ADDITIONAL_REQ",
    0xF23E  : "ID_CPROC_RM_TX_STATE_IND",
    0x1801  : "ID_PHY_RCM_TASK_APPLY_REQ",
    0x1802  : "ID_PHY_RCM_TASK_REL_REQ",
    0x1803  : "ID_PHY_RCM_TASK_RELALL_REQ",
    0x1804  : "ID_PHY_RCM_TASK_PREEMPT_ACK",
    0x1805  : "ID_PHY_RCM_TASK_RESUME_ACK",
    0x1807  : "ID_PHY_RCM_AWAKE_REQ",
    0x1808  : "ID_PHY_RCM_SLEEP_REQ",
    0x1809  : "ID_PHY_RCM_ASSIGN_ACK",
    0x180A  : "ID_PHY_RCM_CLOCK_CAL_ACK",
    0x180C  : "ID_PHY_RCM_GET_MSGLISTADDR_REQ",
    0x180D  : "ID_PHY_RCM_PERIOD_TASK_COMPLETE_REQ",
    0x1828  : "ID_PHY_RCM_GET_LTE_TIMING_REQ",
    0x1881  : "ID_RCM_PHY_TASK_APPLY_CNF",
    0x1882  : "ID_RCM_PHY_TASK_REL_CNF",
    0x1883  : "ID_RCM_PHY_TASK_RELALL_CNF",
    0x1884  : "ID_RCM_PHY_TASK_PREEMPT_IND",
    0x1885  : "ID_RCM_PHY_TASK_RESUME_IND",
    0x1889  : "ID_RCM_PHY_ASSIGN_IND",
    0x188A  : "ID_RCM_PHY_CLOCK_CAL_IND",
    0x188B  : "ID_RCM_PHY_OVERTIME_IND",
    0x188C  : "ID_RCM_PHY_GET_MSGLISTADDR_CNF",
    0x188D  : "ID_RCM_PHY_PERIOD_TASK_COMPLETE_CNF",
    0x18A1  : "ID_RCM_PHY_TASK_PROTECT_IND",
    0x18A2  : "ID_RCM_PHY_TASK_DEPROTECT_IND",
    0x18A8  : "ID_RCM_PHY_SAR_CTRL_ADDITIONAL_NOTIFY",
    0x18B1  : "ID_PHY_RCM_TX_STATE_IND",
    0x18B6  : "ID_RCM_PHY_CLT_ALG_REQ",
    0x18B7  : "ID_PHY_RCM_CLT_ALG_CNF",
    0x18B9  : "ID_RCM_PHY_CLT_SET_TEST_TUNE_TYPE_REQ",
    0x18BA  : "ID_PHY_RCM_CLT_SET_TEST_TUNE_TYPE_CNF",
    0xB000  : "ID_CSDR_CPROC_1X_TX_INFO_IND",
    0xB010  : "ID_CSDR_CPROC_HRPD_TX_INFO_IND",
    0xB020  : "ID_CPROC_STATISTICS_START_REQ",
    0xB021  : "ID_CPROC_STATISTICS_STOP_REQ",
    0xB022  : "ID_CPROC_STATISTICS_CLIENT_RESET_REQ",
}

def get_cproc_rm_msg_str(MsgId, usVersion):
    for MsgIdIndex in cproc_rm_msg_enum_table.keys():
        if MsgIdIndex == MsgId:
            return cproc_rm_msg_enum_table[MsgIdIndex]

    return "unknown"

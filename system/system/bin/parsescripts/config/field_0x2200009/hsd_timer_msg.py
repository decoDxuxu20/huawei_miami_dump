#######################################################################################################################################
#   filename        :   hsd_mscc_msg.py
#
#   author          :   j00354216
#
#   description     :   list hsd timer msg
#
#   modify  record  :   2016-04-27 create file
#
#######################################################################################################################################

hsd_timer_msg_enum_table = {
0x00 : "TI_CNAS_HSD_WAIT_CARD_FILE_CNF",
0x01 : "TI_CNAS_HSD_WAIT_HSM_START_CNF",
0x02 : "TI_CNAS_HSD_WAIT_HLU_START_CNF",
0x03 : "TI_CNAS_HSD_WAIT_CAS_START_CNF",
0x04 : "TI_CNAS_HSD_WAIT_HSM_POWEROFF_CNF",
0x05 : "TI_CNAS_HSD_WAIT_HLU_POWEROFF_CNF",
0x06 : "TI_CNAS_HSD_WAIT_CAS_POWEROFF_CNF",
0x07 : "TI_CNAS_HSD_WAIT_CAS_SYSTEM_SYNC_CNF",
0x08 : "TI_CNAS_HSD_WAIT_CAS_OHM_IND",
0x09 : "TI_CNAS_HSD_WAIT_CAS_STOP_SYSTEM_SYNC_CNF",
0x0A : "TI_CNAS_HSD_AVAILABLE_TIMER",
0x0B : "TI_CNAS_HSD_AVAILABLE_MRU0_TIMER",
0x0C : "TI_CNAS_HSD_SLICE_REVERSE_PROTECT_TIMER",
0x0D : "TI_CNAS_HSD_WAIT_SESSION_NEG_RSLT_IND",
0x0E : "TI_CNAS_HSD_WAIT_CAS_SUSPEND_CNF",
0x0F : "TI_CNAS_HSD_WAIT_CAS_IRAT_OR_RESUME_IND",
0x10 : "TI_CNAS_HSD_WAIT_EHSM_START_CNF",
0x11 : "TI_CNAS_HSD_WAIT_EHSM_POWEROFF_CNF",
0x12 : "TI_CNAS_HSD_WAIT_HSM_POWERSAVE_CNF",
0x13 : "TI_CNAS_HSD_WAIT_RRM_STATUS_IND",
0x14 : "TI_CNAS_HSD_WAIT_CAS_SUSPEND_REL_CNF",
0x15 : "TI_CNAS_HSD_WAIT_HRM_START_CNF",
0x16 : "TI_CNAS_HSD_WAIT_HRM_POWEROFF_CNF",
0x17 : "TI_CNAS_HSD_SYS_ACQ_NO_RF_PROTECT_TIMER",
0x18 : "TI_CNAS_HSD_WAIT_CAS_BG_SRCH_CNF",
0x19 : "TI_CNAS_HSD_WAIT_CAS_STOP_BG_SRCH_CNF",
}

def get_hsd_timer_msg_str( MsgId):
    for MsgIdIndex in hsd_timer_msg_enum_table.keys():
        if MsgIdIndex == MsgId:
            return hsd_timer_msg_enum_table[MsgIdIndex]

    return "none"
#######################################################################################################################################
#   filename        :   xsd_mscc_msg.py
#
#   author          :   j00354216
#
#   description     :   list xsd timer msg
#
#   modify  record  :   2016-04-27 create file
#
#######################################################################################################################################

xsd_timer_msg_enum_table = {
0x00 : "TI_CNAS_XSD_WAIT_CARD_FILE_CNF",
0x01 : "TI_CNAS_XSD_WAIT_XCC_START_CNF",
0x02 : "TI_CNAS_XSD_WAIT_XREG_START_CNF",
0x03 : "TI_CNAS_XSD_WAIT_CAS_START_CNF",
0x04 : "TI_CNAS_XSD_WAIT_XCC_POWEROFF_CNF",
0x05 : "TI_CNAS_XSD_WAIT_XREG_POWEROFF_CNF",
0x06 : "TI_CNAS_XSD_WAIT_CAS_POWEROFF_CNF",
0x07 : "TI_CNAS_XSD_WAIT_CAS_SYSTEM_SYNC_CNF",
0x08 : "TI_CNAS_XSD_WAIT_CAS_OHM_IND",
0x09 : "TI_CNAS_XSD_WAIT_CAS_STOP_SYSTEM_SYNC_CNF",
0x0A : "TI_CNAS_XSD_AVAILABLE_TIMER",
0x0B : "TI_CNAS_XSD_T_BSR_DIG",
0x0C : "TI_CNAS_XSD_T_BSR_CALL",
0x0D : "TI_CNAS_XSD_T_BSR_NEWSYS",
0x0E : "TI_CNAS_XSD_WAIT_CAS_SYSTEM_DETERMIN_IND",
0x0F : "TI_CNAS_XSD_POWEROFF_CAMP_ON_PROTECT_TIMER",
0x10 : "TI_CNAS_XSD_SLICE_REVERSE_PROTECT_TIMER",
0x11 : "TI_CNAS_XSD_AVAILABLE_MRU0_TIMER",
0x12 : "TI_CNAS_XSD_WAIT_CAS_SUSPEND_CNF",
0x13 : "TI_CNAS_XSD_EMC_CALLBACK_NETWORK_SRCH_PROTECT_TIMER",
0x14 : "TI_CNAS_XSD_EMC_CALLBACK_MODE_PROTECT_TIMER",
0x15 : "TI_CNAS_XSD_EMC_CALLBACK_NETWORK_SRCH_BREAK_TIMER",
0x16 : "TI_CNAS_XSD_OOS_SYS_ACQ_CURRENT_PHASE_TOTAL_TIMER",
0x17 : "TI_CNAS_XSD_SYS_ACQ_NO_RF_PROTECT_TIMER",
0x18 : "TI_CNAS_XSD_REDIR_NO_RF_PROTECT_TIMER",
0x19 : "TI_CNAS_XSD_SYS_ACQ_WHEN_LTE_OR_DO_CONN_SYNC_DELAY_TIMER",
}

def get_xsd_timer_msg_str( MsgId):
    for MsgIdIndex in xsd_timer_msg_enum_table.keys():
        if MsgIdIndex == MsgId:
            return xsd_timer_msg_enum_table[MsgIdIndex]

    return "none"
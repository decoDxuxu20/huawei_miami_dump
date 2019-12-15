#######################################################################################################################################
#   filename        :   timer_mm_msg.py
#
#   author          :   fanjing 00179208
#
#   description     :   list timer mm msg
#
#   modify  record  :   2016-02-01 create file
#
#######################################################################################################################################

timer_mm_msg_enum_table = {
0 : "MM_TIMER_T3210",
1 : "MM_TIMER_T3211",
2 : "MM_TIMER_T3212",
3 : "MM_TIMER_T3213",
4 : "MM_TIMER_T3214",
5 : "MM_TIMER_T3216",
6 : "MM_TIMER_T3218",
7 : "MM_TIMER_T3220",
8 : "MM_TIMER_T3230",
9 : "MM_TIMER_T3240",
10 : "MM_TIMER_PROTECT_AGENT",
11 : "MM_TIMER_PROTECT_DETACH",
12 : "MM_TIMER_PROTECT_SIGNALLING",
13 : "MM_TIMER_PROTECT_CC",
14 : "MM_TIMER_PROTECT_CCBS",
15 : "MM_TIMER_PROTECT_SUSPEND",
16 : "MM_TIMER_DELAY_LU_GSM",
17 : "MM_TIMER_DELAY_CS_SERVICE_GSM",
18 : "MM_TIMER_WAIT_CONNECT_REL",
19 : "MM_TIMER_NORMAL_CSFB_HO_WAIT_SYSINFO",
20 : "MM_TIMER_EMERGENCY_CSFB_HO_WAIT_SYSINFO",
21 : "MM_TIMER_MODE_I_CS_PS_POWER_OFF_PROTECT",
22 : "MM_TIMER_PROTECT_CS_DETACH",
23 : "MM_TIMER_WAIT_GET_HO_SECU_INFO_CNF",
24 : "MM_TIMER_T3242",
25 : "MM_TIMER_T3243",
26 : "MM_TIMER_PROTECT_MT_CSFB_PAGING_PROCEDURE",
27 : "MM_TIMER_CS_HO_WAIT_SYSINFO",
28 : "MM_TIMER_DELAY_RADIO_CAPA_TRIGED_LAU",
29 : "MM_TIMER_T3241",
30 : "MM_TIMER_DELAY_NETWORK_SEARCH_AFTER_EMC",
31 : "MM_TIMER_PAGING_RSP_RETRY_PERIOD",
32 : "MM_TIMER_PAGING_RSP_RETRY_INTERVAL",
33 : "MM_TIMER_PAGING_CACHE_RETRY_INTERVAL",
34 : "MM_TIMER_DELAY_ENABLE_RF_OCCUPY",
35 : "MM_TIMER_T3247",
36 : "MM_TIMER_DELAY_DETACH_RRC_EXIST",
37 : "MM_TIMER_T3245",
}

def get_timer_mm_msg_str( MsgId):
    for MsgIdIndex in timer_mm_msg_enum_table.keys():
        if MsgIdIndex == MsgId:
            return timer_mm_msg_enum_table[MsgIdIndex]

    return "none"
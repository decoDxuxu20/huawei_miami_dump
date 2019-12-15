#######################################################################################################################################
#   filename        :   timer_gmm_msg.py
#
#   author          :   fanjing 00179208
#
#   description     :   list timer mm msg
#
#   modify  record  :   2016-02-01 create file
#
#######################################################################################################################################

timer_gmm_msg_enum_table = {
0 : "GMM_TIMER_T3302",
1 : "GMM_TIMER_T3310",
2 : "GMM_TIMER_T3311",
3 : "GMM_TIMER_T3312",
4 : "GMM_TIMER_T3316",
5 : "GMM_TIMER_T3317",
6 : "GMM_TIMER_T3318",
7 : "GMM_TIMER_T3320",
8 : "GMM_TIMER_T3321",
9 : "GMM_TIMER_T3330",
10 : "GMM_TIMER_1S",
11 : "GMM_TIMER_PROTECT",
12 : "GMM_TIMER_PROTECT_FOR_SIGNALING",
13 : "GMM_TIMER_SUSPENDED",
14 : "GMM_TIMER_T3314",
15 : "GMM_TIMER_RAU_RSP",
16 : "GMM_TIMER_PROTECT_FOR_RR_REL",
17 : "GMM_TIMER_PROTECT_OLD_TLLI",
18 : "GMM_TIMER_T3319",
19 : "GMM_TIMER_T3340",
20 : "GMM_TIMER_INTERRAT_HANDOVER_INFO_CNF",
21 : "GMM_TIMER_WAIT_GET_RESEL_SECU_INFO_CNF",
22 : "GMM_TIMER_WAIT_GET_HO_SECU_INFO_CNF",
23 : "GMM_TIMER_WAIT_CONNECT_REL",
24 : "GMM_TIMER_TC_DELAY_SUSPEND_RSP",
25 : "GMM_TIMER_T3323",
26 : "GMM_TIMER_HO_WAIT_SYSINFO",
27 : "GMM_TIMER_DELAY_RADIO_CAPA_TRIGED_RAU",
28 : "GMM_TIMER_WAIT_AS_MS_RADIO_CAPA_INFO",
29 : "GMM_TIMER_DETACH_FOR_POWER_OFF",
30 : "GMM_TIMER_PROTECT_PS_DETACH",
31 : "GMM_TIMER_DELAY_VOICE_DOMAIN_TRIG_RAU",
32 : "GMM_TIMER_DELAY_PS_SMS_CONN_REL",
33 : "GMM_TIMER_DELAY_ENABLE_RF_OCCUPY",
34 : "GMM_TIMER_PS_SERVICE_REQUEST_LIMIT_FORBID",
35 : "GMM_TIMER_DATA_SERVICE_REQUEST_LIMIT_FORBID",
36 : "GMM_TIMER_SIGNALLING_SERVICE_REQUEST_LIMIT_FORBID",
}

def get_timer_gmm_msg_str( MsgId):
    for MsgIdIndex in timer_gmm_msg_enum_table.keys():
        if MsgIdIndex == MsgId:
            return timer_gmm_msg_enum_table[MsgIdIndex]

    return "none"
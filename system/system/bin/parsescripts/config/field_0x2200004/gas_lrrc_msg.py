#######################################################################################################################################
#   filename        :   gas_lrrc_msg.py
#
#   author          :   sunbing 00184266
#
#   description     :   list gas lrrc msg
#
#   modify  record  :   2016-01-07 create file
#
#######################################################################################################################################

gas_lrrc_msg_enum_table = {
0x12B0 : "LRRC_GRR_CELL_RESEL_CNF",
0x12B1 : "LRRC_GRR_CELL_RESEL_STOP_CNF",
0x12B2 : "LRRC_GRR_REDIRECTED_CNF",
0x12B3 : "LRRC_GRR_REDIRECTED_STOP_CNF",
0x12B4 : "LRRC_GRR_CELL_CHANGE_ORDER_CNF",
0x12B5 : "LRRC_GRR_CELL_CHANGE_ORDER_STOP_CNF",
0x12B6 : "LRRC_GRR_HANDOVER_CNF",
0x12B7 : "LRRC_GRR_HANDOVER_STOP_CNF",
0x12B8 : "LRRC_GRR_SET_DSP_POWER_CNF",
0x12B9 : "LRRC_GRR_IDLE_MEASURE_CNF",
0x12BA : "LRRC_GRR_IDLE_MEASURE_IND",
0x12BB : "LRRC_GRR_CONNECTED_MEASURE_CNF",
0x12BC : "LRRC_GRR_CONNECTED_MEASURE_IND",
0x12BD : "LRRC_GRR_CELL_RESEL_REQ",
0x12BE : "LRRC_GRR_CELL_RESEL_STOP_REQ",
0x12BF : "LRRC_GRR_REDIRECTED_REQ",
0x12C0 : "LRRC_GRR_REDIRECTED_STOP_REQ",
0x12C1 : "LRRC_GRR_CELL_CHANGE_ORDER_REQ",
0x12C2 : "LRRC_GRR_CELL_CHANGE_ORDER_STOP_REQ",
0x12C3 : "LRRC_GRR_HANDOVER_REQ",
0x12C4 : "LRRC_GRR_HANDOVER_STOP_REQ",
0x12C5 : "LRRC_GRR_SET_DSP_POWER_REQ",
0x12C6 : "LRRC_GRR_GETUECAPINFO_REQ",
0x12C7 : "LRRC_GRR_IDLE_MEASURE_REQ",
0x12C8 : "LRRC_GRR_CONNECT_MEASURE_REQ",
0x12C9 : "LRRC_GRR_BSIC_VERIFIED_REQ",
0x12CA : "LRRC_GRR_RELALL_REQ",
0x12CC : "LRRC_GRR_CELL_SRCH_REQ",
0x12CD : "LRRC_GRR_CELL_SRCH_STOP_REQ",
0x12CE : "LRRC_GRR_BG_PLMN_SEARCH_CNF",
0x12CF : "LRRC_GRR_BG_PLMN_SEARCH_IND",
0x12D0 : "LRRC_GRR_BG_SEARCH_STOP_CNF",
0x12D1 : "LRRC_GRR_BG_SEARCH_SUSPEND_CNF",
0x12D2 : "LRRC_GRR_BG_SEARCH_RESUME_CNF",
0x12D3 : "LRRC_GRR_BG_PLMN_SEARCH_REQ",
0x12D4 : "LRRC_GRR_BG_SEARCH_STOP_REQ",
0x12D5 : "LRRC_GRR_BG_SEARCH_SUSPEND_REQ",
0x12D6 : "LRRC_GRR_BG_SEARCH_RESUME_REQ",
0x12D7 : "LRRC_GRR_GET_CGI_REQ",
0x12D8 : "LRRC_GRR_GET_CGI_STOP_REQ",
0x12D9 : "LRRC_GRR_FR_INFO_CNF",
0x12F0 : "GRR_LRRC_CELL_RESEL_REQ",
0x12F1 : "GRR_LRRC_CELL_RESEL_STOP_REQ",
0x12F2 : "GRR_LRRC_REDIRECTED_REQ",
0x12F3 : "GRR_LRRC_REDIRECTED_STOP_REQ",
0x12F4 : "GRR_LRRC_CELL_CHANGE_ORDER_REQ",
0x12F5 : "GRR_LRRC_CELL_CHANGE_ORDER_STOP_REQ",
0x12F6 : "GRR_LRRC_HANDOVER_REQ",
0x12F7 : "GRR_LRRC_HANDOVER_STOP_REQ",
0x12F8 : "GRR_LRRC_SET_DSP_POWER_REQ",
0x12F9 : "GRR_LRRC_IDLE_MEASURE_REQ",
0x12FA : "GRR_LRRC_CONNECTED_MEASURE_REQ",
0x12FB : "GRR_LRRC_CELL_RESEL_CNF",
0x12FC : "GRR_LRRC_CELL_RESEL_STOP_CNF",
0x12FD : "GRR_LRRC_REDIRECTED_CNF",
0x12FE : "GRR_LRRC_REDIRECTED_STOP_CNF",
0x12FF : "GRR_LRRC_CELL_CHANGE_ORDER_CNF",
0x1300 : "GRR_LRRC_CELL_CHANGE_ORDER_STOP_CNF",
0x1301 : "GRR_LRRC_HANDOVER_CNF",
0x1302 : "GRR_LRRC_HANDOVER_STOP_CNF",
0x1303 : "GRR_LRRC_SET_DSP_POWER_CNF",
0x1304 : "GRR_LRRC_GETUECAPINFO_CNF",
0x1305 : "GRR_LRRC_IDLE_MEASURE_CNF",
0x1306 : "GRR_LRRC_IDLE_MEASURE_IND",
0x1307 : "GRR_LRRC_CONNECTED_MEASURE_CNF",
0x1308 : "GRR_LRRC_CONNECTED_MEASURE_IND",
0x1309 : "GRR_LRRC_BSIC_VERIFIED_CNF",
0x130A : "GRR_LRRC_BSIC_VERIFIE_IND",
0x130B : "GRR_LRRC_RELALL_CNF",
0x130D : "GRR_LRRC_CELL_SRCH_CNF",
0x130E : "GRR_LRRC_CELL_SRCH_STOP_CNF",
0x130F : "GRR_LRRC_BG_PLMN_SEARCH_REQ",
0x1310 : "GRR_LRRC_BG_SEARCH_STOP_REQ",
0x1311 : "GRR_LRRC_BG_SEARCH_SUSPEND_REQ",
0x1312 : "GRR_LRRC_BG_SEARCH_RESUME_REQ",
0x1313 : "GRR_LRRC_BG_PLMN_SEARCH_CNF",
0x1314 : "GRR_LRRC_BG_PLMN_SEARCH_IND",
0x1315 : "GRR_LRRC_BG_SEARCH_STOP_CNF",
0x1316 : "GRR_LRRC_BG_SEARCH_SUSPEND_CNF",
0x1317 : "GRR_LRRC_BG_SEARCH_RESUME_CNF",
0x1318 : "GRR_LRRC_GET_CGI_CNF",
0x1319 : "GRR_LRRC_GET_CGI_IND",
0x131A : "GRR_LRRC_GET_CGI_STOP_CNF",
0x131B : "GRR_LRRC_FR_INFO_REQ",
}

def get_gas_lrrc_msg_str( MsgId):
    for MsgIdIndex in gas_lrrc_msg_enum_table.keys():
        if MsgIdIndex == MsgId:
            return gas_lrrc_msg_enum_table[MsgIdIndex]

    return "none"
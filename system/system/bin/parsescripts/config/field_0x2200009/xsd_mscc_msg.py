#######################################################################################################################################
#   filename        :   xsd_mscc_msg.py
#
#   author          :   j00354216
#
#   description     :   list xsd mscc msg
#
#   modify  record  :   2016-04-27 create file
#
#######################################################################################################################################

xsd_mscc_msg_enum_table = {
0x2000 : "ID_MSCC_XSD_START_REQ",
0x2001 : "ID_XSD_MSCC_START_CNF",
0x2002 : "ID_MSCC_XSD_POWER_OFF_REQ",
0x2003 : "ID_XSD_MSCC_POWER_OFF_CNF",
0x2004 : "ID_MSCC_XSD_MO_CALL_START_NTF",
0x2005 : "ID_MSCC_XSD_CALL_REDIAL_SYSTEM_ACQUIRE_NTF",
0x2006 : "ID_MSCC_XSD_MO_CALL_SUCCESS_NTF",
0x2007 : "ID_MSCC_XSD_MO_CALL_END_NTF",
0x2008 : "ID_MSCC_XSD_SYSTEM_ACQUIRE_REQ",
0x2009 : "ID_XSD_MSCC_SYSTEM_ACQUIRE_CNF",
0x200A : "ID_XSD_MSCC_SYSTEM_ACQUIRE_IND",
0x200B : "ID_XSD_MSCC_SYSTEM_ACQUIRE_START_IND",
0x200C : "ID_XSD_MSCC_1X_SYSTEM_SERVICE_INFO_IND",
0x200D : "ID_MSCC_XSD_CFREQLOCK_NTF",
0x200E : "ID_MSCC_XSD_CDMACSQ_SET_REQ",
0x200F : "ID_XSD_MSCC_CDMACSQ_SET_CNF",
0x2010 : "ID_XSD_MSCC_CDMACSQ_SIGNAL_QUALITY_IND",
0x2011 : "ID_XSD_MSCC_1X_SYSTEM_TIME_IND",
0x2012 : "ID_MSCC_XSD_POWER_SAVE_REQ",
0x2013 : "ID_XSD_MSCC_POWER_SAVE_CNF",
0x2014 : "ID_MSCC_XSD_CAS_STATUS_IND",
0x2015 : "ID_MSCC_XSD_SYS_CFG_REQ",
0x2016 : "ID_XSD_MSCC_SYS_CFG_CNF",
0x2017 : "ID_XSD_MSCC_RF_AVAILABLE_IND",
0x2018 : "ID_MSCC_XSD_SRV_ACQ_REQ",
0x2019 : "ID_XSD_MSCC_SRV_ACQ_CNF",
0x201A : "ID_MSCC_XSD_BEGIN_SESSION_NOTIFY",
0x201B : "ID_MSCC_XSD_END_SESSION_NOTIFY",
0x201C : "ID_MSCC_XSD_HANDSET_INFO_QRY_REQ",
0x201D : "ID_XSD_MSCC_HANDSET_INFO_QRY_CNF",
0x201E : "ID_XSD_MSCC_EMC_CALLBACK_IND",
0x201F : "ID_MSCC_XSD_END_EMC_CALLBACK_NTF",
0x2020 : "ID_XSD_MSCC_SID_NID_IND",
0x2021 : "ID_MSCC_XSD_SET_CSIDLIST_REQ",
0x2022 : "ID_XSD_MSCC_SET_CSIDLIST_CNF",
0x2023 : "ID_XSD_MSCC_SYNC_SERVICE_AVAILABLE_IND",
0x2024 : "ID_XSD_MSCC_CDMA_UE_STATUS_IND",
0x2025 : "ID_XSD_MSCC_1X_NO_SERVICE_IND",
0x2026 : "ID_MSCC_XSD_NORMAL_SERVICE_IND",
0x2027 : "ID_XSD_MSCC_PRL_HEADER_INFO_IND",
}

def get_xsd_mscc_msg_str( MsgId):
    for MsgIdIndex in xsd_mscc_msg_enum_table.keys():
        if MsgIdIndex == MsgId:
            return xsd_mscc_msg_enum_table[MsgIdIndex]

    return "none"
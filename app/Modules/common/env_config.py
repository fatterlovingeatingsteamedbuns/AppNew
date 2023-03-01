# module_type = 'playwright'
# module_type = 'selenium'

ReadonlyUsers = ['testRbacSH@cpcsh0001.onmicrosoft.com']


class EnvList:
    SH = "SH"
    PPE = "PPE"
    PE = "PROD"
    GCB = "GCB"
    GCP = "GCP"
    GHB = "GHB"
    GHP = "GHP"
    INT = "INT"


SH_EnvConf = {
    "mem_portal_url": "https://intune.microsoft.com/?Microsoft_Azure_CloudPC=selfhost&Microsoft_Intune=selfhost&Microsoft_Intune_Apps=selfhost&Microsoft_Intune_Devices=selfhost&Microsoft_Intune_DeviceSettings=selfhost&Microsoft_Intune_Enrollment=selfhost&Microsoft_Intune_Workflows=selfhost#view/Microsoft_Intune_DeviceSettings/DevicesMenu/~/overview",
    "iwp_url": "https://deschutes-sh.microsoft.com",
}

PPE_EnvConf = {
    "mem_portal_url": "https://intune.microsoft.com/?Microsoft_Azure_CloudPC=canary&Microsoft_Intune=canary&Microsoft_Intune_Apps=canary&Microsoft_Intune_Devices=canary&Microsoft_Intune_DeviceSettings=canary&Microsoft_Intune_Enrollment=canary&Microsoft_Intune_Workflows=canary&l=en.en-us#view/Microsoft_Intune_DeviceSettings/DevicesMenu/~/overview",
    "iwp_url": "https://deschutes-ppe.microsoft.com",
}

PE_EnvConf = {
    "mem_portal_url": "https://intune.microsoft.com/#view/Microsoft_Intune_DeviceSettings/DevicesMenu/~/overview",
    "iwp_url": "https://cloudpc.microsoft.com",
}

GCB_EnvConf = {
    "mem_portal_url": "https://intune.microsoft.com/#view/Microsoft_Intune_DeviceSettings/DevicesMenu/~/overview",
    "iwp_url": "https://cloudpc.microsoft.com",
}

GCP_EnvConf = {
    "mem_portal_url": "https://intune.microsoft.com/#view/Microsoft_Intune_DeviceSettings/DevicesMenu/~/overview",
    "iwp_url": "https://cloudpc.microsoft.com",
}

GHB_EnvConf = {
    "mem_portal_url": "https://intune.microsoft.us/#view/Microsoft_Intune_DeviceSettings/DevicesMenu/~/overview",
    "iwp_url": "https://windows365.microsoft.us",
}

GHP_EnvConf = {
    "mem_portal_url": "https://intune.microsoft.us/#view/Microsoft_Intune_DeviceSettings/DevicesMenu/~/overview",
    "iwp_url": "https://windows365.microsoft.us",
}

INT_EnvConf = {
    "mem_portal_url": "https://intune.microsoft.com/?feature.CloudPCGraphVersion=testprodbeta_cpc_int&Microsoft_Azure_CloudPC=int&canmodifyextensions=true&Microsoft_Intune=selfhost&Microsoft_Intune_Apps=selfhost&Microsoft_Intune_Devices=selfhost&Microsoft_Intune_DeviceSettings=selfhost&Microsoft_Intune_Enrollment=selfhost&Microsoft_Intune_Workflows=selfhost#blade/Microsoft_Intune_DeviceSettings/DevicesMenu/overview",
    "iwp_url": "https://deschutes-int.microsoft.com/",
}

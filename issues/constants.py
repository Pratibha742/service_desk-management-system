from datetime import timedelta



ROLE_STATUS_TRANSITIONS = {
    "Client": {
        "RESOLVED" :["CLOSED"]
    },
    "Support":{
        "OPEN" :["IN_PROGRESS"]
    },
    "Developer":{
        "IN_PROGRESS" :["RESOLVED"]
    },
    "Admin":{
        "OPEN" : ["IN_PROGRESS", "RESOLVED","CLOSED"],
        "IN_PROGRESS" :["RESOLVED","CLOSED"],
        "RESOLVED": ["CLOSED"],

    }
}

SLA_RULES = {
    "HIGH": timedelta(hours=4),
    "MEDIUM": timedelta(hours=24),
    "LOW": timedelta(hours=72)

}
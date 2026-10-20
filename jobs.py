jobs = [
    {
    "id":  0 , 
    "type" : "generate_report" ,
    "input" : {
        "date" : "2026-10-19",
        "time" : "14:23:12"
    },
    "status" : "pending"
    },
    {
    "id":  1 , 
        "type" : "validate_csv" ,
        "input" : {
            "date" : "2026-10-19",
            "time" : "14:23:12"
        },
        "status" : "pending"
},
{
    "id":  2 , 
        "type" : "backup_database" ,
        "input" : {
            "date" : "2026-10-19",
            "time" : "14:23:12"
        },
        "status" : "pending"
}
]

print(jobs[1]["type"])
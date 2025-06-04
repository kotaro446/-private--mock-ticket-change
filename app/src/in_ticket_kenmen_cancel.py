from in_ticket_kenmen_library import (
    get_common_dict,
    get_success_dict,
)

def get_in_ticket_kenmen_cancel(req:dict, mapping:list) -> tuple[int,dict,dict]:
    common_dict, httpstatus = get_common_dict(req, mapping)
    success_dict = get_success_dict(req, mapping, common_dict)
    return (httpstatus, common_dict, success_dict)


from services.log_parser import parse_log

log = (
    "Nov 05 10:15:22 server sshd[1234]: "
    "Failed password for root from "
    "192.168.1.10 port 51234 ssh2"
)

result = parse_log(log)

print(result)

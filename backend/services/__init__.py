
import re

def parse_log(line):
    pattern = (
        r"(\w+\s+\d+\s+\d+:\d+:\d+)\s+"
        r"(\S+)\s+sshd\[(\d+)\]:\s+"
        r"(Failed password|Accepted password|Invalid user)"
        r"(?: for (?:invalid user )?(\S+))?"
        r".*?from\s+(\d+\.\d+\.\d+\.\d+)"
    )

    match = re.search(pattern, line)

    if match:
        return {
            "timestamp": match.group(1),
            "hostname": match.group(2),
            "process_id": match.group(3),
            "event": match.group(4),
            "username": match.group(5),
            "ip_address": match.group(6)
        }

    return None

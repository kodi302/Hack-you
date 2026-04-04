from core.dns_enum import run_dns_enum
from core.subdomain_enum import run_subdomain_enum
from core.port_scanner import run_port_scan
from core.dir_enum import run_dir_enum
from core.risk_engine import analyze_risk
from core.reporter import generate_report

target = input("Enter target: ").strip()

dns_data = run_dns_enum(target)

subs = run_subdomain_enum(target, "fast")

open_ports = run_port_scan(target, "fast")

dirs = run_dir_enum(target, "fast")

analyze_risk(open_ports)

generate_report(target, dns_data, subs, open_ports, dirs)
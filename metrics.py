import psutil
import argparse
from psutil._common import bytes2human

parser = argparse.ArgumentParser()
parser.add_argument("a", help="Input one of arguments: cpu/mem/disk/proc")
args = parser.parse_args()


def cpu_metrics():
    cpu_dict = dict(psutil.cpu_times()._asdict())
    print(f"system.cpu.idle {bytes2human(cpu_dict['idle'])}" + 
            f"\nsystem.cpu.user {bytes2human(cpu_dict['user'])}" + 
            f"\nsystem.cpu.guest {bytes2human(cpu_dict['guest'])}" + 
            f"\nsystem.cpu.iowait {bytes2human(cpu_dict['iowait'])}" +
            f"\nsystem.cpu.stolen {bytes2human(cpu_dict['steal'])}" + 
            f"\nsystem.cpu.system {bytes2human(cpu_dict['system'])}")


def mem_metrics():
    mem_dict = dict(psutil.virtual_memory()._asdict())
    swap_dict = dict(psutil.swap_memory()._asdict())
    print(f"virtual total {bytes2human(mem_dict['total'])}" +
            f"\nvirtual used {bytes2human(mem_dict['used'])}" + 
            f"\nvirtual free {bytes2human(mem_dict['free'])}" + 
            f"\nvirtual shared {bytes2human(mem_dict['shared'])}" + 
            f"\nswap total {bytes2human(swap_dict['total'])}" + 
            f"\nswap used {bytes2human(swap_dict['used'])}" + 
            f"\nswap free {bytes2human(swap_dict['free'])}")


def disk_metrics():
    templ = "%-35s %10s %8s %8s %5s%% %9s  %s"
    print(templ % ("Device", "Total", "Used", "Free", "Use ", "Type",
                   "Mount"))
    for part in psutil.disk_partitions(all=False):
        usage = psutil.disk_usage(part.mountpoint)
        print(templ % (
            part.device,
            bytes2human(usage.total),
            bytes2human(usage.used),
            bytes2human(usage.free),
            int(usage.percent),
            part.fstype,
            part.mountpoint))



def proc_metrics():
    for proc in psutil.process_iter():
        try:
            pinfo = proc.as_dict(attrs=['pid', 'name', 'username'])
        except psutil.NoSuchProcess:
            pass
        else:
            print(' -- '.join(f"{k}:{v}" for k, v in pinfo.items()))


if args.a == 'cpu':
    cpu_metrics()
elif args.a == 'mem':
    mem_metrics()
elif args.a == 'proc':
    proc_metrics()
elif args.a == 'disk':
    disk_metrics()
else:
    print("No such argument!Choose one of: cpu/mem/disk/proc")

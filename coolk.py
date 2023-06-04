import time
import argparse

parser = argparse.ArgumentParser(description='基于命令行的专注时钟')
parser.add_argument('-t', '--time', type=int, default=25, help='专注时间（单位：分钟）')
parser.add_argument('-b', '--break_time', type=int, default=5, help='休息时间（单位：分钟）')

args = parser.parse_args()

def focus_timer():
    print("开始专注！")
    for i in range(args.time):
        time.sleep(60)
    print("休息一下！")
    time.sleep(args.break_time*60)
    print("休息结束！")

if __name__ == "__main__":
    focus_timer()

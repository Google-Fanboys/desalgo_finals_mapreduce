import os
import subprocess

def producemarket(input_dir):
    output_file = os.path.join(input_dir, 'output.csv')
    input_files = [os.path.join(input_dir, f) for f in os.listdir(input_dir)]
    print(f"{'python'}, {'mapreduce.py'} + {input_files} + {output_file}")
    subprocess.call(['python', 'mapreduce.py'] + input_files + [output_file])

def main():
    producemarket()

main()
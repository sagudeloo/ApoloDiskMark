#/usr/bin/python3
import sys
import os
import subprocess
import json
import humanfriendly
from pathlib import Path
import logging

resource_path = os.path.dirname(__file__)

class Benchmark():
    logger = logging.getLogger(__name__)
    bw_bytes = ''                                       #Badn width
    target = '.'                                        #Drirectory where are going to make the benchmark
    loops = '--loops=1'
    size = '--size=1024m'
    tmpFile = 'fiomark.tmp'
    stoneWall = '--stonewall'
    ioEngine = '--ioengine=libaio'
    direct = '--direct=1'
    zeroBuffers = '--zero_buffers=0'
    outputFormat = '--output-format=json'
    fioWhich = subprocess.getoutput('which fio')
    
    operations = [
        {
            "prefix": 'seq1mq8t1',
            "rw": 'read',
            'bs': '1m',
            'ioDepth': '8',
            'numJobs': '1',
        },
        {
            "prefix": 'seq1mq8t1',
            "rw": 'write',
            'bs': '1m',
            'ioDepth': '8',
            'numJobs': '1',
        },
        {
            "prefix": 'seq1mq1t1',
            "rw": 'read',
            'bs': '1m',
            'ioDepth': '1',
            'numJobs': '1',

        },
        {
            "prefix": 'seq1mq1t1',
            "rw": 'write',
            'bs': '1m',
            'ioDepth': '1',
            'numJobs': '1',
        },
        {
            "prefix": 'rnd4kq32t16',
            "rw": 'randread',
            'bs': '4k',
            'ioDepth': '32',
            'numJobs': '16',
        },
        {
            "prefix": 'rnd4kq32t16',
            "rw": 'randwrite',
            'bs': '4k',
            'ioDepth': '32',
            'numJobs': '16',
        },
        {
            "prefix": 'rnd4kq1t1',
            "rw": 'randread',
            'bs': '4k',
            'ioDepth': '1',
            'numJobs': '1',

        },
        {
            "prefix": 'rnd4kq1t1',
            "rw": 'randwrite',
            'bs': '4k',
            'ioDepth': '1',
            'numJobs': '1',
        }
    ]

    def __init__(self):
        pass
    
    #This functions remove the temporal benchmark files
    def finish (self):
        self.logger.info('Benchmark Finished, garbage collection now...')
        targetFilename = f'{self.target}/{self.target}'
        self.logger.info(f'Verifying if temp file exists: [{targetFilename}]')
        if os.path.isfile(targetFilename):
            self.logger.info(f'Yes, removing the file: [{targetFilename}]')
            os.remove(targetFilename)
    
    #This function execute the benchmark
    def run(self):
        self.logger.info('Executing Benchmarks...')
        for index, operation in enumerate(self.operations):
            self.logger.info(f'Running index [{index}]\tprefix:\t[{operation["prefix"]}] rw:[{operation["rw"]}]')
            
            fileName = f'--filename={self.target}/{self.tmpFile}'
            name = f'--name={operation["prefix"]}{operation["rw"]}'
            currentCmd = [self.fioWhich, self.loops, self.size, fileName, self.stoneWall, self.ioEngine, self.direct, self.zeroBuffers, name, f'--bs={operation["bs"]}', f'--iodepth={operation["ioDepth"]}', f'--numjobs={operation["numJobs"]}', f'--rw={operation["rw"]}', f'{self.outputFormat}']
            output = subprocess.Popen(currentCmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            jsonOutput, err = output.communicate()
            dictOutput = json.loads(jsonOutput)
            if 'read' in operation['rw']:
                self.bw_bytes = ('{}/s'.format(humanfriendly.format_size(dictOutput['jobs'][0]['read']['bw_bytes'])))
            else:
                self.logger.info('Type Write')
                self.bw_bytes = ('{}/s'.format(humanfriendly.format_size(dictOutput['jobs'][0]['write']['bw_bytes'])))
            result(operation["prefix"], operation["rw"] , self.bw_bytes)

def result(testName, testType, result):
        output = '{:<15}'.format(testName) + '{:<10}'.format(testType) + '{:>15}'.format(result)
        print(output)

def main():
    benchmark = Benchmark()
    benchmark.run()

if __name__ == '__main__':
    main()
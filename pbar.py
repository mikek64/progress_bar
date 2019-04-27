# -*- coding: utf-8 -*-
"""
Created on Fri Aug 24 12:45:52 2018
Function to show a progress bar
@author: mike_
"""

from timeit import default_timer as timer
from sys import stdout

#%%

class ProgressBar():
    ''' show progress bar for a loop, inspired by the keras progress bar '''
    def __init__(self, total, update_every = 0.1):
        ''' total is the size of the loop
        update every, how often to report in seconds '''
        assert type(total) == int, 'total must be int'
        assert type(update_every) == float, 'Update every must be float'
        assert update_every >= 0.0, 'Update every must be >= 0.0'
        self.start_time = timer()
        self.report_time = timer()
        self.total = total
        self.update_every = update_every
        self.counter = 0 # number of steps already processed
        
    def reset(self, total = None, update_every = None):
        ''' Reset the progress bar '''
        if total is None:
            total = self.total
        if update_every is None:
            update_every = self.update_every
        self.__init__(total, update_every)
        
        
    
    def show(self, i = None, stats = ''):
        ''' Display a progress bar based on number processed i
        Note i must reach self.total at end for finished '''

        assert type(stats) == str, 'stats must be formatted as string'
        if i is None:
            i = self.counter + 1
        assert type(i) == int, 'i must be int, or None for next item'
        
        finished = i == self.total
        self.counter = i # record current position        
        if i == 0:
            return
        
        # report every update_every seconds        
        t = timer()
        if t - self.report_time < self.update_every and not finished:
            # do nothing
            return   
        self.report_time = t

        # Num batches
        if finished:
            batch_line = str(self.total) + '/' + str(self.total)
        else:
            batch_line = str(i) + '/' + str(self.total)
        
        # generate progress line
        line_len = 30
        progress = int(line_len * i / self.total)
        if finished: # Finished [===========================]
            progress_line = ' [' + '=' * line_len + ']'
        else: # in progress  [===============>..............]
            progress_line = ' [' + '=' * progress + '>' + '.' * (line_len - progress - 1) + ']'

        
        # generate time line
        tm = t - self.start_time # time elapsed
        if finished:  # total time plus time per step
            tm_step = int(tm / self.total * 1000000) # in micro seconds
            time_line = ' - ' + str(int(tm)) + 's ' + str(tm_step) + 'us/step'
        else: # show ETA
            eta = int(tm * (self.total - i) / i)
            time_line = ' - ETA: ' + str(eta) +'s'

        if stats != '' and stats[0] != ' ':
            stats = ' ' + stats
    
        line = batch_line + progress_line + time_line + stats 
        
        stdout.write('\r' + line)
        stdout.flush() # apparently needed on some systems
        if finished:
            stdout.write('\n') # for newline

#%%

def demo():
    ''' demo of the progress bar and prove it works '''
    import time

    print('Loop 1')
    looplength = 50
    pb = ProgressBar(looplength)
    for i in range(looplength):
        time.sleep(0.1)
        pb.show()

    print('Loop 2')
    looplength = 30
    pb.reset(looplength, update_every = 0.5)
    for i in range(looplength):
        time.sleep(0.1)
        pb.show(i+1, stats = 'some statistics')
    
    print('Done')


if __name__ == '__main__':
    demo()
            
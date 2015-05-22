#!/usr/bin/env python

import os
import hashlib as hl

# def split_file(fp, marker, blkSize):
#     result = []
#     current = ''
#     for block in iter(lambda: fp.read(blkSize), ''):
#         current += block
#         while 1:
#             markerpos = current.find(marker)
#             if markerpos == -1:
#                 break
#             result.append(currentp:markerpos])
#             current = current[markerpos + len(marker):]
#     result.append(current)
#     return result

def blockHash(filename, blkSize):
    # Get file:
    fid = open(filename, 'rb')
    fileStats = os.stat(filename)
    
    # Get the last block (offset)
    blockNum = fileStats.st_size / blkSize
    offset = fileStats.st_size % blkSize
    blockAddress = fid.seek(blockNum*blkSize, 0)
    if offset != 0:
        block = fid.read(offset)
    else:
        block = fid.read(blkSize)
        
    currentHash = hl.sha256(block)
    while (blockNum > 0) :
        blockNum -= 1
        blockAddress = fid.seek(blockNum*blkSize)
        block = fid.read(blkSize) + currentHash.digest()
        currentHash = hl.sha256(block)
        
    return currentHash
    
if __name__ == '__main__':
    BLOCKSIZE = 1024
    filename = 'VIDS/solved.mp4'
    # Test:
    assert blockHash(filename, BLOCKSIZE).hexdigest() == '03c08f4ee0b576fe319338139c045c89c3e8e9409633bea29442e21425006ea8', "The results don't match!!! Please, check"

    # Solution:
    filename = 'VIDS/toSolve.mp4'
    print blockHash(filename, BLOCKSIZE).hexdigest()
    

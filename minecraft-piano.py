#www.stuffaboutcode.com
#Raspberry Pi, Minecraft Piano - Different blocks back different tones when hit!

#import the minecraft.py module from the minecraft directory
import minecraft.minecraft as minecraft
#import minecraft block module
import minecraft.block as block
#import time, so delays can be used
import time
#import pygame to use the mixer to play wav file
import pygame

if __name__ == "__main__":
    
    #Connect to minecraft by creating the minecraft object
    # - minecraft needs to be running and in a game
    mc = minecraft.Minecraft.create()

    #Initialise pygame and the mixer
    pygame.init()
    pygame.mixer.init()
    #load WAVS files
    noteF3= pygame.mixer.Sound("notes/f3.wav")
    noteG3= pygame.mixer.Sound("notes/g3.wav")
    noteA3= pygame.mixer.Sound("notes/a3.wav")
    noteB3= pygame.mixer.Sound("notes/b3.wav")
    noteC4= pygame.mixer.Sound("notes/c4.wav")
    noteD4= pygame.mixer.Sound("notes/d4.wav")
    noteE4= pygame.mixer.Sound("notes/e4.wav")
    noteF4= pygame.mixer.Sound("notes/f4.wav")
    noteG4= pygame.mixer.Sound("notes/g4.wav")
    noteA4= pygame.mixer.Sound("notes/a4.wav")
    noteB4= pygame.mixer.Sound("notes/b4.wav")

    #block type to sound obj
    blocksToWavs = {block.STONE.id: noteF3,
                    block.GRASS.id: noteG3,
                    block.WOOD.id: noteA3,
                    block.DIRT.id: noteB3,
                    block.SAND.id: noteC4,
                    block.GRAVEL.id: noteD4,
                    block.LEAVES.id: noteE4,
                    block.COBBLESTONE.id: noteF4,
                    block.BRICK_BLOCK.id: noteG4,
                    block.WOOD_PLANKS.id: noteA4,
                    block.WOOL.id: noteB4}
    
    #Post a message to the minecraft chat window 
    mc.postToChat("Minecraft Piano, www.stuffaboutcode.com")
    
    #loop until Ctrl C
    try:
        while True:
            #Get the block hit events
            blockHits = mc.events.pollBlockHits()
            # if a block has been hit
            if blockHits:
                # for each block that has been hit
                for blockHit in blockHits:
                    #If the block hit type (DIRT, WOOD, etc) is in the
                    # blocksToWavc dictionary - play the WAV
                    blockType = mc.getBlock(blockHit.pos.x, blockHit.pos.y, blockHit.pos.z)
                    if (blockType in blocksToWavs.keys()):
                        noteToPlay = blocksToWavs[blockType]
                        noteToPlay.play()
            #sleep for a short time        
            time.sleep(0.1)
    except KeyboardInterrupt:
        print("stopped")

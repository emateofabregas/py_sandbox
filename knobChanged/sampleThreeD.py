import nuke

n = nuke.thisNode()
k = nuke.thisKnob()

def sampleThreeD(picker_knob, pos_knob,nodeSample):
    """
    This function takes the 2d knob (picker_knob) using nodeSample as a reference for setting up 3D position info (pos_knob).
    
    Args:
        picker_knob(x,y): 2d knob to use for search the position.
        pos_knob(x,y,z): 3d knob put the values of the sampled for nodeSample.    
        nodeSample(r,g,b): node to use the reference for sample values.    
        
    Returns:
        Sampled values of nodeSample to pos_knob using picker_knob.
    """

    pos = n[picker_knob].value()  # The position picker_knob
    animated = k.isAnimated() # If the knob is animated
            
    # Check if proxy mode is active
    if nuke.root().knob('proxy').value():
        nuke.message('You have to disable proxy mode to use this feature.')
        
    #Sample the nodeSample to get the position
    else:
        r = nodeSample.sample('red',  pos[0], pos[1],)
        g = nodeSample.sample('green', pos[0], pos[1])
        b = nodeSample.sample('blue',  pos[0], pos[1])
    
    # Check the knob if it's animated               
    if animated:
        if not n.knob(pos_knob).isAnimated():
            n.knob(pos_knob).setAnimated()
        else:
            n.knob(pos_knob).clearAnimated()
                        
    # Set the end_3d knob with the sampled values
    n[pos_knob].setValue([r, g, b])


"""
EXAMPLE HOW TO USE IT:
# Assuming that you copied import nuke and n and k var:

if k.name('matte_type'): #Example of pulldown choice
    if n.knob('matte_type').value() == 'Shape': # Example item of pulldown choice 
        if k.name() == 'position': # 2d knob
            sampleThreeD('position', 'position_3d', sampleP) # function
"""

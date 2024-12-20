import nuke

def removeNode(node):
    """
    This function removes a custom node. This is useful when you want to remove only one specific node: eg: Input created before.
    
    Args:
        node(str): The node that you want to remove. You can do nuke.toNode() command because it returns a str.
    
    Returns:
        Input removed if it's created.
    """

    if node:
        nuke.delete(node)  # Delete node if it exists 

"""
EXAMPLE HOW TO USE IT:
#Assuming you copied import nuke

input = nuke.toNode('InputCustom') # you can create this var or just put it in the function brackets directly but I suggest using the var in case you want to use it in another part of your script. 

if input:
    removeNode(input)

"""

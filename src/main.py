from textnode import TextNode, TextType

from static_pieces import*


    
static = pathlib.Path("/home/elguero/workspace/github/clydesdalecoder/Site_Generator/static")
public =  pathlib.Path("/home/elguero/workspace/github/clydesdalecoder/Site_Generator/public")

def main():
   
    print("Deleting public directory...")
    if os.path.exists(public):
        shutil.rmtree(public)

    print ("Copying static files to public directory...")    
    stat_to_pub_copy(static, public) 

if __name__ == "__main__": 
    main()

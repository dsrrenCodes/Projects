import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


def change_brightness(image, value):
    new_img=image.copy()
    #clip for extra precaution but the menu1 should check for proper user input
    new_img=np.clip(new_img+value,0,255)
    
    return new_img
  
def change_contrast(image, value):
    new_img=image.copy()
    contrast_f= (259*(value+255))/(255*(259-value))
    new_img=contrast_f*(new_img-128)+128
    #clipping for extraprecaution
    new_img=np.clip(new_img,0,255)
    return new_img
    

def grayscale(image):
    new_img=image.copy()
    #need to iter the entire array to get RGB, then apply the formula
    for i in range(new_img.shape[0]): #rows
        for j in range(new_img.shape[1]): #cols
            r,g,b=new_img[i,j]
            gray_value=int(0.3*r+0.59*g+0.11*b)
            new_r,new_g,new_b=gray_value,gray_value,gray_value
            #replacing original values to gray values
            new_img[i,j]=[new_r,new_g,new_b]

    return new_img
    

def blur_effect(image):
    new_img=image.copy()
    k=np.array([[0.0625, 0.125, 0.0625],[0.125, 0.25, 0.125],[0.0625, 0.125, 0.0625]])
    #iter the entire array and we excluding the borders CUZ we do not wan to blur the frame so -1 !
    for i in range(1, new_img.shape[0]-1):
        for j in range(1,new_img.shape[1]-1):
            #the 3x3 matrix around the current pixel to get the M 
            M =image[i-1:i+2,j-1:j+2] #3x3 region
            #c for color channe;ls
            for c in range(new_img.shape[2]):
                #not mat mul is element wise multiplication
                new_img[i, j, c] =np.sum(M[:,:,c]*k)
    return new_img
    

def edge_detection(image):
    new_img=image.copy()
    k=np.array([[-1,-1,-1],[-1,8,-1],[-1,-1,-1]])
    #iter the entire array and we excluding the borders CUZ we do not wan to blur the frame so -1 !
    for i in range(1, new_img.shape[0]-1):
        for j in range(1,new_img.shape[1]-1):
            #the 3x3 matrix around the current pixel to get M in the pdf doc
            M = image[i-1:i+2,j-1:j+2] #3x3 region
            
            for c in range(new_img.shape[2]):
                new_img[i, j, c] = np.sum(M[:,:,c]*k)+128
    #new_img+=128
    #cuz q need clip ;p
    new_img=np.clip(new_img,0,255)
    return new_img
    

def embossed(image):
    new_img=image.copy()
    k=np.array([[-1,-1,0],[-1,0,1],[0,1,1]])
    #iter the entire array and we excluding the borders CUZ we do not wan to blur the frame so -1 !
    for i in range(1, new_img.shape[0]-1):
        for j in range(1,new_img.shape[1]-1):
            #the 3x3 matrix around the current pixel to get M in the pdf doc
            M = image[i-1:i+2,j-1:j+2] #3x3 region
            
            for c in range(new_img.shape[2]):
                new_img[i, j, c] = np.sum(M[:,:,c]*k)+128
    #new_img+=128
    new_img=np.clip(new_img,0,255)
    return new_img
    

def rectangle_select(image, x, y):
    #top left
    x1,y1=x
    #bot right
    x2,y2=y
    #zero matrix
    new_mask=np.zeros((image.shape[0],image.shape[1]))
    #apply filter with slicing
    new_mask[x1:x2+1,y1:y2+1]=1
    return new_mask
    

def magic_wand_select(image, x, thres):                
    return np.array([]) # to be removed when filling this function

def compute_edge(mask):           
    rsize, csize = len(mask), len(mask[0]) 
    edge = np.zeros((rsize,csize))
    if np.all((mask == 1)): return edge        
    for r in range(rsize):
        for c in range(csize):
            if mask[r][c]!=0:
                if r==0 or c==0 or r==len(mask)-1 or c==len(mask[0])-1:
                    edge[r][c]=1
                    continue
                
                is_edge = False                
                for var in [(-1,0),(0,-1),(0,1),(1,0)]:
                    r_temp = r+var[0]
                    c_temp = c+var[1]
                    if 0<=r_temp<rsize and 0<=c_temp<csize:
                        if mask[r_temp][c_temp] == 0:
                            is_edge = True
                            break
    
                if is_edge == True:
                    edge[r][c]=1
            
    return edge

def save_image(filename, image):
    img = image.astype(np.uint8)
    mpimg.imsave(filename,img)

def load_image(filename):
    img = mpimg.imread(filename)
    if len(img[0][0])==4: # if png file
        img = np.delete(img, 3, 2)
    if type(img[0][0][0])==np.float32:  # if stored as float in [0,..,1] instead of integers in [0,..,255]
        img = img*255
        img = img.astype(np.uint8)
    mask = np.ones((len(img),len(img[0]))) # create a mask full of "1" of the same size of the laoded image
    img = img.astype(np.int32)
    return img, mask

def display_image(image, mask):
    # if using Spyder, please go to "Tools -> Preferences -> IPython console -> Graphics -> Graphics Backend" and select "inline"
    tmp_img = image.copy()
    edge = compute_edge(mask)
    for r in range(len(image)):
        for c in range(len(image[0])):
            if edge[r][c] == 1:
                tmp_img[r][c][0]=255
                tmp_img[r][c][1]=0
                tmp_img[r][c][2]=0
 
    plt.imshow(tmp_img)
    plt.axis('off')
    plt.show()
    print("Image size is",str(len(image)),"x",str(len(image[0])))

def menu():

    def menu1(img,mask):
        
        while True:
            n=str(input("""
    What do you want to do?
------------------------------------------------
                      MENU
------------------------------------------------
Input    Function
------------------------------------------------
e          Exit the Program 
l          Load a Picture
s          Save the current picture
1          Adjust the Brightness
2          Adjust Contrast 
3          Apply Grayscale
4          Apply Blur
5          Edge Detection
6          Embossed
7          Rectangle Select
8          Magic Wand Select
""").lower())
                                
        
            match n:
                
                case 'e':
                    print('\nProgram Ended\n')
                    
                    return 'exit'
                    

                case 'l':
                    filename=input("\nEnter the filename of the image to load: \n")

                    try:

                        img,mask= load_image(filename)

                    except FileNotFoundError:
                        print(f'\n{filename} file name not found, please enter a valid file name.\n------------------------------------------------ ')
                        menu1(img,mask)
                    
                    
                    break

                case 's':
                    try:
                        location=input('\nEnter a filename (ending with .png/.jpg/.jpeg) you want to save to: \n')
                        save_image(location,img)
                        print('\nImage Succesfully Saved!\n')
                    except:
                        print('Something Went Wrong! Ensure your file ends with ".png/.jpg/.jpeg! Bringing you back to menu...')
                        menu1(img,mask)
                    

                    break
                
                case '1':
                    num=input('\nEnter Brightness Value (+/-): \n')
                    try:
                        
                        num=int(num)
                        if num<=-255 or num>=255:
                            print(f'\n{num} is not a valid input! Please ensure your input is between -255 and +255. Bringing you back to menu...\n')
                            menu1(img,mask)
                        
                        
                    except:
                        print(f'\n{num} is not a valid input! Bringing you back to menu...\n')
                        menu1(img,mask)

                    
                    
                    img = change_brightness(img,num)
                    print('\nBrightness Changed Successfully!\n')
                    break

                case '2':
                    num=input('\nEnter Contrast Value (+/-): \n')
                    try:
                        
                        num=int(num)
                        if num<=-255 or num>=255:
                            print(f'\n{num} is not a valid input! Please ensure your input is between -255 and +255. Bringing you back to menu...\n')
                            menu1(img,mask)
                        
                        
                    except:
                        print(f'\n{num} is not a valid input! Bringing you back to menu...\n')
                        menu1(img,mask)
                    img = change_contrast(img,num)
                    print('\nContrast Changed Successfully!\n')
                    break
                
                case '3':
                    try:
                        img = grayscale(img)
                        print('\nGrayScaled Effect Is Successful!\n')
                        menu1(img,mask)
                    except:
                        print('\nSomething went wrong! Bring you back to menu...\n')
                        menu1(img,mask)
                    break
                
                case '4':
                    try:
                        img=blur_effect(img)
                        print('Blur Effect Is Successful!\n')
                        menu1(img,mask)
                    except:
                        print('\nSomething went wrong! Bring you back to menu...\n')
                        menu1(img,mask)

                    break

                case '5':
                    try:
                        img=edge_detection(img)
                        print('\n Edge Detection Effect Is Successful!\n')
                        menu1(img,mask)
                    except:
                        print('\nSomething went wrong! Bring you back to menu...\n')
                        menu1(img,mask)

                    break

                case '6':
                    try:
                        img=embossed(img)
                        print('\n Embossed Effect Is Successful!\n')
                        menu1(img,mask)
                    except:
                        print('\nSomething went wrong! Bring you back to menu...\n')
                        menu1(img,mask)

                    break

                case '7':
                    try:
                        x=input('Enter Your top left X coordinate x1,y1: ')
                        resX =[int(x) for x in (x.split(','))]
                        resX=tuple(resX)
                    except:
                        print('Invalid X coordinate input!(include the coma, if u have not)')
                        print('Bringing you back to menu...\n')
                        menu1(img,mask)
                    try:
                        Y=input('Enter Your bottom right Y coordinate x2,y2: ')
                        resY =[int(Y) for Y in (Y.split(','))]
                        resY=tuple(resY)
                    except:
                        print('Invalid Y coordinate input!(include the coma, if u have not)')
                        print('Bringing you back to menu...\n')
                        menu1(img,mask)
                    if resX[0]<0 or resX[0]<0 or resY[0]>=img.shape[0] or resY[1]>=img.shape[1]:
                        print('Coordinates are out of bounds!')
                        print('Bringing you back to menu...\n')
                        menu1(img,mask)
                    if resX[0]>resY[0] or resX[1]>resY[1]:
                        print('Your X coordinate must be top left and Y coordinate must be bottom left!')
                        print('Bringing You back to menu...\n') 
                        menu1(img,mask)

                    try:
                        mask=rectangle_select(img,resX,resY)
                        print('\nRectangle Select Done Successfully!\n')
                        menu1(img,mask)
                    except:
                        print('\nSomething went wrong! Bring you back to menu...\n')
                        menu1(img,mask)

                        
                    break

                case '8':
                    pass
                    break

                case _:
                    print('\n\n')
                    print('Please enter a valid Input\n')
                    menu1()

                    break

#FIRST STEP_____________________________________

    img = mask = np.array([]) 
    
    while True:
        if img.size == 0:
            m=str(input("""
What do you want to do?
------------------------------------------------
                      MENU
------------------------------------------------
Input    Function
------------------------------------------------
e          Exit the Program 
l          Load a Picture
Your choice: \n""").lower())
            
            if m!='e' and m!='l':
                print('''\n
Please enter a correct input
------------------------------------------------                      
''')
                continue
            elif m=='e':
                print('\nProgram Ended\n')
                return None
            
            elif m=='l':
            
                filename=input("\nEnter the filename of the image to load: \n")

            try:
                
                img,mask= load_image(filename)
                print('\nFile Loaded Successfully!\n')

            except:
                print(f'\n{filename} file name not found, please enter a valid file name.\n------------------------------------------------ ')
                continue

        
        
        status=menu1(img,mask)
        if status=='exit':
            break
        


        


    
                
            



    
  
       
if __name__ == "__main__":
    menu()







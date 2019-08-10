#!/usr/bin/env python

# Hello World in GIMP Python

from gimpfu import *

def makePoster(file0, file1, file2, file3, backgroundImageFile):
    

    
              # Make a new image. 
              posterW, posterH = 2480, 3508
              poster = gimp.Image(2480, 3508, RGB)
              gimp.message("new image created")


              #start undo group
              pdb.gimp_image_undo_group_start(poster)

              # Can't add this first because we don't know the size of the text layer.
              background = gimp.Layer(poster, "Background", posterW, posterH,
                                    RGB_IMAGE, 100, NORMAL_MODE)

              colorF = gimpcolor.RGB(221, 240, 232)
              colorB = gimpcolor.RGB(86, 94, 91)

              pdb.gimp_context_set_foreground(colorF)
              pdb.gimp_context_set_background(colorB)

              background.fill(FOREGROUND_FILL)
              poster.add_layer(background, 0)

              # create a image layer

              backgroundImage = pdb.file_png_load(backgroundImageFile, backgroundImageFile)
              
              image0 = pdb.file_png_load(file0, file0)              
              image1 = pdb.file_png_load(file1, file1)

              image2 = pdb.file_png_load(file2, file2)
              image3 = pdb.file_png_load(file3, file3)
              
              #make layer 0
              backgroundLayer = gimp.Layer(poster, "backgroundLayer", posterW, posterH, RGBA_IMAGE, 100, NORMAL_MODE)
              
              layer0 = gimp.Layer(poster, "Layer 0", 2480, 1000, RGBA_IMAGE, 100, NORMAL_MODE)
              layer1 = gimp.Layer(poster, "Layer 1", 2172, 800, RGBA_IMAGE, 100, NORMAL_MODE)

              layer2 = gimp.Layer(poster, "Layer 2", 2172, 800, RGBA_IMAGE, 100, NORMAL_MODE)
              layer3 = gimp.Layer(poster, "Layer 3", 2172, 800, RGBA_IMAGE, 100, NORMAL_MODE)

              
              # add the layer to the image
              poster.add_layer(backgroundLayer, 0)
              pdb.gimp_edit_copy(backgroundImage.layers[0]) #cannot copy image 0, only layers
              backgroundLayer.update(0, 0, posterW, posterH) #use if not visible to force an update
              backgroundLayer.translate(0, 0)
              pdb.gimp_edit_paste(backgroundLayer, True)
              
              # add the layer to the image
              poster.add_layer(layer0, 0)
              pdb.gimp_layer_set_opacity(layer0, 60)
              pdb.gimp_edit_copy(image0.layers[0]) #cannot copy image 0, only layers
              layer0.update(0, 0, 2480, 1000) #use if not visible to force an update
              layer0.translate(0, 0)
              pdb.gimp_edit_paste(layer0, True)
              

              # add the layer to the image
              poster.add_layer(layer1, 0)
              pdb.gimp_edit_copy(image1.layers[0]) #cannot copy image 0, only layers
              layer1.update(0, 0, 2172, 800) #use if not visible to force an update
              layer1.translate((posterW-2172)/2, 550)
              pdb.gimp_edit_paste(layer1, True)

              # add the layer to the image
              poster.add_layer(layer2, 0)
              pdb.gimp_edit_copy(image2.layers[0]) #cannot copy image 0, only layers
              layer2.update(0, 0, 2172, 800) #use if not visible to force an update
              layer2.translate((posterW-2172)/2, 1370)
              pdb.gimp_edit_paste(layer2, True)

              # add the layer to the image
              poster.add_layer(layer3, 0)
              pdb.gimp_edit_copy(image3.layers[0]) #cannot copy image 0, only layers
              layer3.update(0, 0, 2172, 800) #use if not visible to force an update
              layer3.translate((posterW-2172)/2, 2190)
              pdb.gimp_edit_paste(layer3, True)


              # Create a new text layer (-1 for the layer means create a new layer)
              s1TextLayer = pdb.gimp_text_fontname(poster, None, 0, 0, "WHEN YOU SET IN THE WATER", 10,
                                           True, 109, PIXELS, 'Avenir Next')
              s1TextLayer.translate(154,1200)

              s2TextLayer = pdb.gimp_text_fontname(poster, None, 0, 0, "YOU HAVE TO WAIT FOR", 10,
                                           True, 109, PIXELS, 'Avenir Next')
              s2TextLayer.translate(1050,2000)

              s3TextLayer = pdb.gimp_text_fontname(poster, None, 0, 0, "THE WAVE", 10,
                                           True, 109, PIXELS, 'Avenir Next')
              s3TextLayer.translate(154,2800)

              titleTextLayer = pdb.gimp_text_fontname(poster, None, posterW/2, posterH/2, "A MILLION WAVES", 10,
                                           True, 120, PIXELS, 'Trebuchet MS')
              titleTextLayer.translate(-titleTextLayer.width/2, 1350)

              
              # Create a new image window
              gimp.Display(poster)
              # Show the new image window
              gimp.displays_flush()
              
              #end undo group
              pdb.gimp_image_undo_group_end(poster)

register(
              "python_fu_makePoster",
              "Make Poster",
              "Make a poster for [A Million Waves]",
              "Qiuyang",
              "Copyright@Qiuyang",
              "2018",
              "Make a poster...",
              "", # Create a new image, don't work on an existing one
              [
                  (PF_FILE, "file0", "Choose image1.png", ""),
                  (PF_FILE, "file1", "Choose image2.png", ""),
                  (PF_FILE, "file2", "Choose image3.png", ""),
                  (PF_FILE, "file3", "Choose image4.png", ""),
                  (PF_FILE, "backgroundImageFile", "Choose image background.png", "")
                  
              ],
              [],
              makePoster, menu="<Image>/File/Create/CS6102"
)

main()

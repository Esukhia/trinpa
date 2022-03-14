from trinpa import gen_word_cloud


# mandatory arguments
text = 'space_segmented_text.txt'
out_file = 'wordcloud_with_background.png'
mask_file = 'colored_mask_file.png'
background = 'background.jpeg'
gen_word_cloud(text, out_file, mask_file, background_file=background)

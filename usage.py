from trinpa import gen_word_cloud


# mandatory arguments
text = 'space_segmented_text.txt'
out_file = 'wordcloud.png'
mask_file = 'colored_mask_file.png'
gen_word_cloud(text, out_file, mask_file)

# trinpa

Wordcloud generator for Tibetan

## usage

```python
from trinpa import gen_word_cloud

text = 'space_segmented_text.txt'
out_file = 'wordcloud.png'
mask_file = 'colored_mask_file.png'
gen_word_cloud(text, out_file, mask_file)
```

## Output

### Mask:

![maskfile](colored_mask_file.png)

### Wordcloud:

![wordcloud](wordcloud.png)

### After-mask:

![image](https://user-images.githubusercontent.com/17675331/158207681-5ec910dd-ffed-40d6-b1e2-6992931943eb.png)
